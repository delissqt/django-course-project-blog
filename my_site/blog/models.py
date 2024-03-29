from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300) # TextField
    image= models.ImageField(upload_to="posts", null=True) # ImageField , ImageField.height_field, ImageField.width_field , "posts" should be inside "uploads" folder e.i. /uploads/posts
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    comment_text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="comments")


# A comment should be realted to post
# And since it's a one-to-many relation,
# and one comment belongs to one post
# but one post can have multiple comments