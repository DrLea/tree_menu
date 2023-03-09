from django.db import models
from django.utils.text import slugify


class Meal(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time_to_cook = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)


class Restaurant(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    meals = models.ManyToManyField(Meal, through='RestaurantMeal')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Restaurant, self).save(*args, **kwargs)


class Recipe(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    ingredients = models.JSONField()
    description = models.TextField(null=True, blank=True)


class RestaurantMeal(models.Model):
    restaurant = models.ForeignKey(Restaurant, models.CASCADE, null=True)
    meal = models.ForeignKey(Meal, models.CASCADE, null=True)

