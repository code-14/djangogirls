from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #link to another model
    #settings.AUTH_USER_MODEL is a class
    title = models.CharField(max_length=300)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True,null = True)#blank=true->allowing blank values
    #null= true means django willl store empty values as null
        #likes
    '''
    blank = true is different from null = true
    null = true informs the db that if there is empty value store null in db so it is db related
    blank = true is form validation related.So that the browser knows that empty value is allowed
    when we fill a form some fields are marked as asterisk..if we don't fill them we get an error
    it is possibl e due to blank=true not specified for those fields
    Form validation: When you enter data, the browser and/or the web server
    will check to see that the data is in the correct format and within the constraints
     set by the application.
    '''
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #__str__ is called whenever u call str() on an object
    def __str__(self): 
        return self.title
    ''' 
    def clean(self):
        cleaned_data = super().clean()
        creationDate = cleaned_data.get(creation_date)
        publicationDate = cleaned_data.get(publication_date)
        if creationDate < publicationDate:
            raise forms.ValidationError("Publication date should be greater than or equal to creation date.")

    '''



# Create your models here.
