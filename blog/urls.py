from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_posts, name='get_posts'),
    path('<int:post_id>/', views.get_post_details, name='get_post_details'),
    path('author/<str:author>/', views.PostsByAuthorView.as_view(), name='posts_by_author'),
]
