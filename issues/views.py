from typing import Any
from django.shortcuts import render
from .models import Issues, Status
from django.views.generic import ListView
# Create your views here.


class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = Super().get_context_data(**kwargs)
        to_do = Status.objects.get(name='to do')
        in_prog = Status.objects.get(name='inprogress')
        done = Status.objects.get(name='done')
        context["to_do_list"] = Issue.objects.filter(
            status=to_do
        ).order_by('created_on').reverse()
        context["in_prog_list"] = Issue.objects.filter(
            status=in_prog
        ).order_by("created_on").reverse()
        context["done_list"] = Issue.objects.filter(
            statuse=done
        ).order_by("created_on").reverse()
        return context
