from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField('Category')
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    date_published = models.DateTimeField()
    author = models.ManyToManyField('Author')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{} {}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ('date_published',)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
