from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# class based views
from django.views.generic import ListView, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# models
from users.models import User
from themes.models import Theme
# forms
from users.forms import UserCreateForm, UserUpdateForm

# Create your views here.

# public profile
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = 'username'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.username == self.kwargs['slug']:
            return super(UserDetailView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('users:profile'))

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['themes'] = Theme.objects.filter(user=self.object.pk)
        return context

# user register
class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse_lazy('users:profile')

# private profile
class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileTemplateView, self).get_context_data(**kwargs)
        context['object'] = self.model.objects.get(pk=self.request.user.pk)
        context['themes'] = Theme.objects.filter(user=self.request.user.pk)
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('users:detail', args=(self.object.username,))
