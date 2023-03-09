from django.contrib import admin
from tree.models import Restaurant, Recipe, Meal, RestaurantMeal


class RestaurantMealInline(admin.TabularInline):
    model = RestaurantMeal
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [RestaurantMealInline, ]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('meal', 'ingredients')
