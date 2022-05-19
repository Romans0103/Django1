from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the Url patterns

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

class Book(models.Model):
    '''
    Model representing a book (but not a specific copy of a book).
    '''
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NUL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books./
    # Внешний ключ используется, потому что у книги может быть только один автор, но у авторов может быть несколько книг
    # Author as a string rather than object because it hasn't been declared yet in the file./
    # Автор в виде строки, а не объекта, потому что он еще не был объявлен в файле
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the books')
    isbn = models.CharField('ISBN', max_length=13,help_text='13 Character <a'
'href="https://www.isbn-international.org/content/what-jsbn">JSBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genry for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defind so we can specify the object above.
    def __str__(self):
        '''
        String for representing Model object.
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Returns the url to access a particular books instance.
        '''
        return reverse('book-detail', args=[str(self.id)])