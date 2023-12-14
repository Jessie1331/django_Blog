from django.urls import path
from .views import HomePageView, AboutPageView, FrontpagePageView


urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", FrontpagePageView.as_view(), name='frontpage'),
]