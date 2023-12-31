from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

MEAL_TYPE = (
    ('starter', 'Starter'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)


class Item(models.Model):
    meals = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.meals)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.meals

    def get_absolute_url(self):
        return reverse('menu_item', kwargs={'meal': self.slug})
