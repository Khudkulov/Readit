from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=123)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=123)
    slug = models.SlugField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    content = RichTextField()
    tags = models.ManyToManyField(Tag)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='subarticles')
    title = models.CharField(max_length=123)
    header_content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    footer_content = RichTextField(null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='articles/comments/', null=True, blank=True)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="50" height="50" /></a>')
        return '-'


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + "-" + str(timezone.now().date()))


pre_save.connect(article_pre_save, sender=Article)

