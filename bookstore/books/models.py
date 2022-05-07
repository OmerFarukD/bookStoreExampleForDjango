from unicodedata import name
from django.db import models
class Author(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200,blank=False,null=False)
    created=models.DateTimeField('Oluşturuldu.')
class Book(models.Model):
    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=200,blank=False,null=False)
    created=models.DateTimeField('Oluşturuldu.')
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2,max_digits=4,null=True)