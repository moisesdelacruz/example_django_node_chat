from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# login required
from django.contrib.auth.mixins import LoginRequiredMixin
# class based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# models
from themes.models import Theme
from core.models import Comment

# Create your views here.

class ThemeListView(ListView):
    model = Theme

class ThemeDetailView(DetailView):
    model = Theme

    def get_context_data(self, **kwargs):
        context = super(ThemeDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(theme=self.kwargs['pk'])[::-1]
        return context
