from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# class based views
from django.views.generic import View

# Create your views here.

# Login
class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return super(LoginView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('users:profile'))

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "auth/login.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
					return redirect(url_next)
                else:
					return redirect('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return redirect('/')

        return render(request)

# Logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')
