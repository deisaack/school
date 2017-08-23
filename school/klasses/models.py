from django.db import models


class Klass(models.Model):
	name = models.CharField(max_length=20)

	class Meta:
		verbose_name = 'Class'
		verbose_name_plural = 'Classes'

	def __str__(self):
		return self.name
