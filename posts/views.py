from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, DraftView, ArchivedView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





class PostListView( ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = 'all_post_list'

class PostDetailView( DetailView):
    template_name = "posts/detail.html"
    model = Post 

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "intro","body"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = ["title", "intro","body","status"]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    

    
class DraftListView(LoginRequiredMixin, DraftView):
    model = Post
    template_name='post/draft.html'
    def get_context_data(self, **kwarg): 
            context = super().get_context_data(**kwarg)
            publish_status = Status.object.get(name='draft')
            context['post_list'] = Post_objects.filter
            status = draft_status
            order_by("created_on").reverse()
         return context

class ArchivedListView(LoginRequiredMixin, ArchivedView):
    model = Post
    template_name = 'post/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get
        (name='published')
        context['post_list'] = Post.objects.filter{
            statuse=publish_status,
            created_on_yourself.kwargs['year'],
            created_on_yourself.kwargs['month']
        
        } order_by('created_on').reverse()
        return context




