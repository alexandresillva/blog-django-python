from django.urls import path
from .views import hello_blog, save_form

urlpatterns = [
    path('', hello_blog),
    path('save-form/', save_form, name='save_form'),
]
