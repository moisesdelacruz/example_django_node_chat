from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
# django paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# class based views
from django.views.generic import ListView, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# models
from users.models import User
from publishings.models import Publishing
# forms
from users.forms import UserUpdateForm

# Create your views here.

# public profile
class UserDetailView(LoginRequiredMixin, ListView):
    model = Publishing
    template_name = 'users/user_detail.html'
    paginate_by = 5

    def get_queryset(self):
        # original qs
        qs = super(UserDetailView, self).get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(user__username=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['slug'])

        context['publishings'] = context['object_list']
        context['object'] = user
        return context

# private profile
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if not self.kwargs['slug'] == request.user.username:
            return redirect(reverse_lazy('users:detail', args=(self.kwargs['slug'],)))
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('users:detail', args=(self.object.username,))
