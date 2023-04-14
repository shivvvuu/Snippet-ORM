from django.db import models

# Create your models here.

class Teacher(models.Model):
    
    firstname= models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    

class Student(models.Model):
    
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    

# Abstract Model

class BaseItem(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['title']
        

class ItemA(BaseItem):
    content = models.TextField()
    
    class Meta(BaseItem.Meta): # Meta inheritance
        ordering = ['-created']
    
    
class ItemB(BaseItem):
    file = models.FileField(upload_to='file')
    
class ItemC(BaseItem):
    file = models.FileField(upload_to='file')
    
class ItemD(BaseItem):
    slug = models.SlugField(max_length=255, unique=True)
    

# Multi-table model inheritance

class Book(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
# class ISBN(Book):
#     ISBN = models.TextField()

class ISBN(Book):
    book_ptr = models.OneToOneField( # overriding the ptr given by django
        Book, on_delete=models.CASCADE,
        parent_link=True, # key that defines this relation betwwen ISBN and Book class pr model
        primary_key=True,
    )
    ISBN = models.TextField()
    
# Proxy models

class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
class BookOder(BookContent):
    # object = NewManager()
    class Meta:
        proxy = True
        ordering = ['created']
        
    def created_on(self):
        return timezone.now - self.created