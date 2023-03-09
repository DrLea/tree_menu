from django.shortcuts import render, HttpResponse
from django.views import View
from django.db.models import Q

from tree.models import Restaurant, Meal, Recipe


class RestaurantView(View):

    def get(self, request, slug=None):
        query_filter = Q()
        context = {}

        if slug:
            query_filter.add(Q(slug=slug), Q.AND)

        restaurants = Restaurant.objects.filter(query_filter)
        if restaurants.exists():
            context['restaurants'] = restaurants

        return render(request, 'index.html', context)
