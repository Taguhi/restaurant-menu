from django.db import models


RESTUARANT_TYPES = (
	('free', 'Free'),
	('asian', 'Asian'),
	('french', 'French'),
)


class Restuarant(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=150)
	type = models.CharField(choices=RESTUARANT_TYPES, null=True, max_length=30)
