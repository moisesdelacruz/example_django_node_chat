from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# login required
from django.contrib.auth.mixins import LoginRequiredMixin
# class based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# models
from publishings.models import Publishing
from core.models import Comment
from users.models import User
# forms
from publishings.forms import PublishingModelForm

# Create your views here.

class PublishingListView(LoginRequiredMixin, ListView):
    model = Publishing

class PublishingCreateView(LoginRequiredMixin, CreateView):
    model = Publishing
    form_class = PublishingModelForm

    def form_valid(self, form):
        print form
        user = User.objects.get(id=self.request.user.id)
        # format form
        __object = form.save(commit=False)
        __object.user = user
        __object.save()
        return super(PublishingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('publishings:detail', args=(self.object.pk,))

class PublishingUpdateView(LoginRequiredMixin, UpdateView):
    model = Publishing
    form_class = PublishingModelForm

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        # format form
        __object = form.save(commit=False)
        __object.user = user
        __object.save()
        return super(PublishingUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('publishings:detail', args=(self.object.pk,))

class PublishingDetailView(LoginRequiredMixin, DetailView):
    model = Publishing

    def get_context_data(self, **kwargs):
        context = super(PublishingDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(publishing=self.kwargs['pk'])[::-1]
        return context