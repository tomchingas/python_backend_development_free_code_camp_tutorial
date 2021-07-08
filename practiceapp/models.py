from django.db import models

# Create your models here.
class Feature(models.Model):    # .Model makes it reference the database, see line 100 in index.html file for Feature reference in html
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)