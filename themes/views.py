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
from users.models import User
# forms
from themes.forms import ThemeModelForm

# Create your views here.

class ThemeListView(LoginRequiredMixin, ListView):
    model = Theme

class ThemeCreateView(LoginRequiredMixin, CreateView):
    model = Theme
    form_class = ThemeModelForm

    def form_valid(self, form):
        print form
        user = User.objects.get(id=self.request.user.id)
        # format form
        __object = form.save(commit=False)
        __object.user = user
        __object.save()
        return super(ThemeCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('themes:detail', args=(self.object.pk,))

class ThemeUpdateView(LoginRequiredMixin, UpdateView):
    model = Theme
    form_class = ThemeModelForm

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        # format form
        __object = form.save(commit=False)
        __object.user = user
        __object.save()
        return super(ThemeUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('themes:detail', args=(self.object.pk,))

class ThemeDetailView(LoginRequiredMixin, DetailView):
    model = Theme

    def get_context_data(self, **kwargs):
        context = super(ThemeDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(theme=self.kwargs['pk'])[::-1]
        return context
