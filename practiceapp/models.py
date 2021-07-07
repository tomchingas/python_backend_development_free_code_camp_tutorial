from django.db import models

# Create your models here.
class Feature:
    id: int
    name: str
    details: str
    is_true: bool #checks if something is true or false