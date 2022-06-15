from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=10, unique=True)
  slug = models.SlugField(max_length=10, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/blog/category/{self.slug}/'

  class Meta:
    verbose_name_plural = 'Categories'


class Post(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f'{self.pk} / {self.title}'

  def get_absolute_url(self):
    return f'/python/{self.pk}/'
