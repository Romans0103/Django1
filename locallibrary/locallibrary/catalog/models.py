from django.db import models

# Create your models here.
class MyModelName(models.Model):
    '''
    A typical class defining a model, derived from the Model class.
    '''

# Fields
my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

# Metadata

class Meta:
    ordering = ['-m my_field_name']

#  Methods
def get_absolute_url(self):
    '''
    Returns the url to accses a particular instance of MyModelName
    '''
    return reverse('model-detail-view', args=[str(self.id)])

def __str__(self):
    '''
    String for representing the MyModelName object (in Admin site etc.)
    '''
    return self.field_name


# Create a new record using the model's constructor.
a_record = MyModelName(my_field_name="Instance #1")
# Save the object into the database.
a_record.save()

# Access model field values using Python atributes.
print(a_record.id) #should return 1 for the first record
print(a_record.my_field_name) # should print 'Instance #1"

# Change record by modifying the fields, then calling save().
a_record.my_field_name="New Instance Name"
a_record.save()


class Genre(models.Model):
    '''
    Model representing a book genre (e.g. Science Fiction, Non Fiction)
    '''
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g.Science Fiction, French Poetry etc.)')

    def __str__(self):
        '''
        String for representing the Model object(in Admin site etc)
        '''
        return self.name