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
    model = User
    template_name = 'users/user_detail.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.model.objects.get(username=self.kwargs['slug'])

        query_result = Publishing.objects.filter(user=user).order_by('-created_at')
        # paginator
        paginator = Paginator(query_result, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['publishings'] = object_list
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
