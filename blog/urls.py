from django.urls import path

from blog import views

urlpatterns = [
    path('', views.get_posts, name='get_posts'),
]
