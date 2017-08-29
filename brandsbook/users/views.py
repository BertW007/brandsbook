from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, FormView, ListView
from django.views.generic import UpdateView
from .forms import UserCreateForm, UserLoginForm, UserUpdateForm, SearchForm, SearchBrandsForm


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
        return redirect(self.request.GET.get('next', '/home'))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/home')


class UserShowAllView(ListView):
    model = User
    template_name = 'users/user_list.html'


class UserDetailView(View):
    model = User

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'users/user_detail.html', {
            "us": user,
        })


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update_form.html'


class SearchView(FormView):
    template_name = 'users/search_form.html'
    form_class = SearchForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def form_valid(self, form):
        company_name = form.cleaned_data['company_name']
        user_list = User.objects.filter(
            company_name__icontains=company_name,
        )
        return render(self.request, 'users/search_form.html', {
            'form': form,
            'results': user_list,
        })


class HomeView(View):
    model = User

    def get(self, request):
        user = User.objects.all()

        return render(request, 'users/home.html', {
            "us": user,
        })


class BrandsAutocompleteView(FormView):
    template_name = 'users/autocomplete.html'
    form_class = SearchBrandsForm


class BrandsFavView(View):
    pass


class UserMsgView(View):
    pass


class BrandsCooperationView(View):
    pass
