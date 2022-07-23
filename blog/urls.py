from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update', views.post_update_view, name='post_update'),
    path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
]
