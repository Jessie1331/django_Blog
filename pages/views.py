
from django.views.generic import TemplateView
from django.shortcuts import render
from posts.models import Post



def frontpage(request):

    return render(request, 'pages/frontpage.html')

def about(request):
    return render(request, 'pages/about.html')


class HomePageView(TemplateView):
    template_name = "pages/home.html"
    Post = Post.objects.all()
   

