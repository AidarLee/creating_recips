import os
import smtplib
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models.deletion import RestrictedError
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.backends import UserModel
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string


# Create your views here.



@csrf_exempt
def login_page(request):
    success_url = reverse_lazy('admin_panel')
    template_name = "admin/pages/login.html"
    if request.user.is_authenticated:
        return redirect(success_url)
    else:
        return render(request, template_name, {})


@csrf_exempt
def authorization(request):
    success_url = reverse_lazy('admin_panel')
    username = request.POST['username']
    password = request.POST['password']
    try:
        account = authenticate(username=UserModel.objects.get(email=username).username, password=password)
        if account is not None and request.method == 'POST':
            login(request, account)
            return redirect(success_url)
        else:
            messages.error(request, "Логин или пароль неправильно")
            return redirect('login_page')
    except:
        if username == "":
            messages.error(request, "Введите Username или E-mail")
            return redirect('login_page')
        elif password == "":
            messages.error(request, "Введите пароль")
            return redirect('login_page')
        else:
            account = authenticate(username=username, password=password)
            if account is not None and request.method == 'POST':
                login(request, account)
                return redirect(success_url)
            else:
                messages.error(request, "Логин или пароль неправильно")
                return redirect('login_page')
   

def logout_page(request):
    logout(request)
    return redirect('login_page')

class ProfileView(View):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('update_profile')
    

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, ProfileView, UpdateView):
    login_url = "login_page"
    success_message = "Данные успешно изменены"
    template_name = 'admin/pages/update.html'
    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user
    
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'admin/pages/forgot-password.html'
    success_message = "Пароль успешно изменён"
    success_url = reverse_lazy('update_profile') 

# Admin-Panel Views
class AdminMain(LoginRequiredMixin, ListView):
    login_url = 'login_page'
    model = User
    paginate_by = 5
    template_name = "admin/admin.html"
    #count = HotNews.objects.count()
    extra_context = {
           "is_active" : "main-panel",
          # "all_entries" : count,
    }

@login_required
def admin_form_page(request):
    template_name = "admin/pages/admin.html"

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username
    context = {
        "user" : user_name
    }
    return render(request, template_name, context)

def index(request):
    context= {

    }

    return render(request, 'client/index.html')

def about(request):
    context= {

    }

    return render(request, 'client/pages/about.html')

def contact(request):
    context= {

    }

    return render(request, 'client/pages/contact.html')

def cart(request):
    context= {

    }

    return render(request, 'client/pages/cart.html')


def meels(request):
    products = Products.objects.order_by('id')
    protein = 0
    check = None
    regions = Categories.objects.all()
    hide_ingredients = None

    region = request.GET.get('region')
    meal = request.GET.get('meal')
    mass_fraction = request.GET.get('massfraction')
    price = request.GET.get('price')

    not_exist = False
    
    try:
        chemical_comp = Chemicals.objects.get(product=meal)
        protein = (float(mass_fraction) * chemical_comp.protein) / float(mass_fraction)
        print(mass_fraction)
        
    except Chemicals.DoesNotExist:
        check = True

    try:
        chemical_comp = Chemicals.objects.all()
        # protein = (float(mass_fraction) * float(Chemicals.model.protein)) / float(mass_fraction)
        
    except Chemicals.DoesNotExist:
        check = True
    # if chemical_comp is None:
    #     check = True
    # else:

    context= {
        'products': products,
        "protein" : protein,
        "hide_result" : check,
        "not_exist" : not_exist,
        "regions" : region,
        "hide_ingredients" : hide_ingredients,
    }

    return render(request, 'client/pages/meels.html', context)

def list(request):
    list_of_products = Products.objects.order_by('id')

    context= {
        'list_of_products':list_of_products,
    }

    return render(request, 'client/pages/list.html', context)


def manufacturers(request):
    context= {

    }

    return render(request, 'client/pages/manufacturers.html')