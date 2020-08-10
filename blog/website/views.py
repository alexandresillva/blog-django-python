from django.shortcuts import render
from .models import Post
import datetime


def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'HTML3', 'CSS3', 'PostgeSQL',
             'Linux', 'Nginx']

    list_posts = Post.objects.filter(active=True)

    x = datetime.datetime.now()
    year = x.year
    data = {'name': 'Curso de Django 3',
            'lista_tecnologias': lista, 'posts': list_posts, 'year': year}

    return render(request, 'index.html', data)
