from datetime import date, datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

data = {
    "programlama":"programlama kurs listesi",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db = {
    "courses" : [
        {
            "title" : "javascript kursu",
            "description" : "javascript kurs açıklaması",
            "imageUrl" : "1.jpg",
            "slug" : "javascript-kursu",
            "date" : date(2022,10,10),
            "isActive" : True,
            "isUpdate" : False
        },
        {
            "title" : "python kursu",
            "description" : "python kurs açıklaması",
            "imageUrl" : "2.jpg",
            "slug" : "python-kursu",
            "date" : date(2022,9,10),
            "isActive" : False,
            "isUpdate" : False
        },
        {
            "title" : "web geliştirme kursu",
            "description" : "web geliştirme kurs açıklaması",
            "imageUrl" : "3.jpg",
            "slug" : "web-gelistirme-kursu",
            "date" : date(2022,8,10),
            "isActive" : True,
            "isUpdate" : True
        },
    ],
    "categories" : [
        {"id" : 1, "name" : "programlama", "slug" : "programlama"},
        {"id" : 2, "name" : "web geliştirme", "slug" : "web-gelistirme"},
        {"id" : 3, "name" : "mobil uygulamalar", "slug" : "mobil-uygulamalar"},
    ] 
}
# Create your views here.

def index(request):
    courses = Course.objects.filter(isActive=1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories' : categories,
        'courses' : courses
    })

def details(request, _slug):
    course = get_object_or_404(Course, slug=_slug)
    context = {
        'course' : course
    }
    return render(request, 'courses/details.html', context)


def getCoursesByCategory(request, _slug):
    courses = Course.objects.filter(category__slug=_slug, isActive=True)
    categories = Category.objects.all()
    return render(request, 'courses/index.html', {
        'categories' : categories,
        'courses' : courses,
        'selectedCategory' : _slug
    })
