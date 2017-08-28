from django.views.generic import CreateView
from .forms import UserCreateForm
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
