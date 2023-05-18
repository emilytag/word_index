from django.db import models

class WordIndex(models.Model):
	word = models.CharField(max_length=200)
	index_data = models.JSONField(default=dict)

	def __str__(self):
		return self.word


