from django.contrib.postgres.fields import JSONField
from django.db import models

class WordIndex(models.Model):
	word = models.CharField(max_length=200)
	index_data = JSONField()

	def __str__(self):
		return self.word


