from django.db import models

# Create your models here.
class MyModelName(models.Model):
''' A typical class defining a model, derived from the Model class.
'''

# Fields
my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

