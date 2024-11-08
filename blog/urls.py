from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='get_posts'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='get_post_details'),
    path('author/<str:author>/', views.PostsByAuthorView.as_view(), name='posts_by_author'),
    path('create/', views.create_post, name='create_post'),
]
