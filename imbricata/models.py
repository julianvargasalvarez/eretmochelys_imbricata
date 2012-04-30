from django.db import models

class Entry(models.Model):
	longitude = models.IntegerField()
	latitude = models.IntegerField()
	family = models.TextField()
	species = models.TextField()
	tribe = models.TextField()
	collector = models.TextField()
	collection_date = models.DateTimeField()
	code = models.CharField(max_length=10)
