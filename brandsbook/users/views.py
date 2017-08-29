from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.views.generic import UpdateView

from .forms import UserCreateForm, UserLoginForm, UserUpdateForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/user_form.html'
    success_url = 'users/user_detail.html'


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'users/login_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.request.GET.get('next', '/users'))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/users')


class UserShowAllView(ListView):
    model = User
    template_name = 'users/user_list.html'


class UserDetailView(View):
    model = User

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'users/user_detail.html', {
            "user": user,
        })


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update_form.html'
