from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView
from . import views
urlpatterns = [
    # path('<slug:slug>/', views.details, name='post_detail'),
   
    path("home/", PostListView.as_view(), name="list"),
    path("new/", PostCreateView.as_view(), name='new'),
    path("<int:pk>", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name='edit'),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name='delete'),

]