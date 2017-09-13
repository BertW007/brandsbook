from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import FormView, ListView
from .models import Detail, Brands, InterestingBrands
from .forms import UserLoginForm, SearchForm, SearchBrandsForm, AddBrandsForm, \
                   UserCreateDetailForm, BrandsCooperationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = UserCreationForm()
    return render(request, 'users/user.html', {'form': form})


@receiver(post_save, sender=User)
def create_detail(sender, instance, created, **kwargs):
    if created:
        Detail.objects.create(person=instance, company_name='company_name', post_code='00-000',
                              city='city', street='street', nr='nr', phone='phone', nip='nip')


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'users/user_login.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.request.GET.get('next', '/'))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class UserShowAllView(ListView):
    model = Detail
    template_name = 'users/user_list.html'


class UserDetailView(View):
    model = Detail

    def get(self, request, pk):
        user = Detail.objects.get(person=pk)
        my_brands = Brands.objects.filter(company=user)
        brands = InterestingBrands.objects.filter(company=user)

        return render(request, 'users/user_detail.html', {
            "us": user,
            "my_brands": my_brands,
            "brands": brands,
        })


class UserUpdateDetailView(FormView):
    model = Detail
    form_class = UserCreateDetailForm
    template_name = 'users/user_update_form.html'

    def post(self, request, pk):
        form = UserCreateDetailForm(data=request.POST)
        if form.is_valid():
            detal =Detail.objects.get(person_id=pk)

            detal.nip = form.cleaned_data['nip']
            detal.company_name=form.cleaned_data['company_name']
            detal.post_code = form.cleaned_data['post_code']
            detal.city = form.cleaned_data['city']
            detal.street = form.cleaned_data['street']
            detal.nr = form.cleaned_data['nr']
            detal.phone = form.cleaned_data['phone']
            detal.save(update_fields=['company_name', 'post_code', 'city', 'street', 'nr', 'phone', 'nip'])
            return redirect('http://127.0.0.1:8000/home/')

        else:
            return render(request, self.template_name, {
                'form': form,
             })


class SearchView(FormView):
    template_name = 'users/search_form.html'
    form_class = SearchForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def form_valid(self, form):
        company_name = form.cleaned_data['company_name']
        user_list = Detail.objects.filter(
            company_name__icontains=company_name,
        )
        return render(self.request, 'users/search_form.html', {
            'form': form,
            'results': user_list,
        })


class HomeView(View):
    model = Detail

    def get(self, request):
        user = Detail.objects.latest("id")

        return render(request, 'users/home.html', {
            "us": user,
        })


class BrandsAutocompleteView(FormView):
    template_name = 'users/search_brands.html'
    form_class = SearchBrandsForm


class BrandsAddView(FormView):
    template_name = 'users/add_brands.html'
    form_class = AddBrandsForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def post(self, request, pk):
        form = AddBrandsForm(data=request.POST)
        if form.is_valid():
            b = Brands.objects.create(name=form.cleaned_data['name'])
            d = Detail.objects.get(id=pk)
            b.company.add(d)

            return redirect('http://127.0.0.1:8000/home/')
        else:
            return render(request, self.template_name, {
                'form': form,
             })


class InterestingBrandsAddView(BrandsAddView):

    def post(self, request, pk):
        form = AddBrandsForm(data=request.POST)
        if form.is_valid():
            b = InterestingBrands.objects.create(name=form.cleaned_data['name'])
            d = Detail.objects.get(id=pk)
            b.company.add(d)

            return redirect('http://127.0.0.1:8000/home/')
        else:
            return render(request, self.template_name, {
                'form': form,
             })


class UserBrandsDetailView(View):
    model = Brands

    def get(self, request, pk):
        brands = Brands.objects.filter(company=pk)
        return render(request, 'users/user_detail.html', {
            "br": brands,
        })


class BrandsCooperationView(View):
    model = Detail

    def post(self, request, pk):
        form = BrandsCooperationForm(pk=pk, data=request.POST)
        if form.is_valid():
            value = form.cleaned_data['brands'].id
            b = InterestingBrands.objects.get(id=value).name
            bb = Brands.objects.filter(name=b)
            if bb is not None:
                br = set()
                for brand in bb:
                    for company in brand.company.all():
                        br.add(company)
                return render(request, 'users/cooperation.html', {
                    "form": form,
                    "brands": br,
                })
        return render(request, 'users/cooperation.html', {
            "form": form,
        })

    def get(self, request, pk):
        form = BrandsCooperationForm(pk=pk)
        return render(request, 'users/cooperation.html', {
            "form": form,
        })
