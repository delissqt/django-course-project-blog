from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)


class Tag(models.Model):
    caption = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300) # TextField
    image_name= models.CharField(max_length=100) # ImageField , ImageField.height_field, ImageField.width_field
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinValueValidator(50), MaxValueValidator(500)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)
