# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..models import Category, Page


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category).order_by('-views')
        category.views += 1
        category.save()
        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    # print(context_dict)
    # return HttpResponse(context_dict)
    return render(request, 'rango/category.html', context_dict)
