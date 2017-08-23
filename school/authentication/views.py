from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from . import forms
from . models import Profile
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm


User = get_user_model()

class LoginView(bracesviews.AnonymousRequiredMixin,
                authviews.LoginView):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        redirect = super(LoginView, self).form_valid(form)
        remember_me = form.cleaned_data.get('remember_me')
        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)
        return redirect

class LogoutView(authviews.LogoutView):
    url = reverse_lazy('home')


def signup(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('authentication/emails/activate_email.html', {
                'user'  : user,
                'domain': current_site.domain,
                'uid'   : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your school account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.info(request, 'Please verify your email to continue')
            return redirect('home')

    else:
        form = forms.RegistrationForm

    return render(request, 'authentication/user_create.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # profile = Profile.objects.create(user=user)
        # user.profile.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        # login(request, user)
        return redirect('auth:login')
    else:
        messages.error(request, 'The activation link is invalid')
        return redirect('home')


class PasswordChangeView(authviews.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'authentication/password-change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request,
                         "Your password was changed, "
                         "hence you have been logged out. Please relogin")
        return super(PasswordChangeView, self).form_valid(form)


class PasswordResetView(authviews.PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = 'authentication/password-reset.html'
    success_url = reverse_lazy('auth:password-reset-done')
    subject_template_name = 'authentication/emails/password-reset-subject.txt'
    email_template_name = 'authentication/emails/password-reset-email.html'


class PasswordResetDoneView(authviews.PasswordResetDoneView):
    template_name = 'authentication/password-reset-done.html'


class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
    template_name = 'authentication/password-reset-confirm.html'
    form_class = forms.SetPasswordForm
