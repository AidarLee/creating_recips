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
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect, HttpResponse
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
from django.db.models import Count


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
            messages.error(request, "Неверный логин или пароль!")
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
                messages.error(request, "Неверный логин или пароль!")
                return redirect('login_page')
   
def password_reset_request(request):
    settings.EMAIL_HOST_USER='kyrgyzindustry.portal.01@gmail.com'
    settings.EMAIL_HOST_PASSWORD='jenpktauntyqbeum'
    if request.method == "POST":
        
        password_reset_form = UserPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Запрос на сброс данных"
                    email_template_name = "admin/pages/user/forgot-password-email.html"
                    c = {
                        "email":user.email,
                        'domain':'http://127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                    email = render_to_string(email_template_name, c)
                    
                    try:
                        send_mail(subject, email, 'zenisbekovk04@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        
                        return HttpResponse('Invalid header found.')
                    
                    return redirect ("/accounts/password_reset/done/")
    password_reset_form = UserPasswordResetForm()
    return render(request=request, template_name="admin/pages/user/forgot-password-email.html", context={"password_reset_form":password_reset_form})



def logout_page(request):
    logout(request)
    return redirect('login_page')

class ProfileView(View):
    login_url = "login_page"
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('update_profile')
    

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, ProfileView, UpdateView):
    success_message = "Данные успешно изменены"
    template_name = 'admin/pages/user/update.html'
    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user
    
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'admin/pages/user/forgot-password-email.html'
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
    template_name = "admin/admin.html"

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username
    context = {
        "user" : user_name
    }
    return render(request, template_name, context)


#       Admin-panel
 

def test(request):
    context = {}

    return render(request, 'admin/pages/cards.html')




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


def value_sum(value, sum) -> None:
        return value / sum
 

class aminoAc():
    
    def __init__(self, asparing, glutamin, serin, gistidin, glitsin, treonin, arginin, alanin, tirosin, tsistein, valin, metionin, triptofan, fenilalalin, izoleitsin, leitsin, lisin, prolin):
        self.asparing = asparing
        self.glutamin = glutamin
        self.serin = serin
        self.gistidin = gistidin
        self.glitsin = glitsin
        self.treonin = treonin
        self.arginin = arginin
        self.alanin = alanin
        self.tirosin = tirosin
        self.tsistein = tsistein
        self.valin = valin
        self.metionin = metionin
        self.triptofan = triptofan
        self.fenilalalin = fenilalalin
        self.izoleitsin = izoleitsin
        self.leitsin = leitsin
        self.lisin = lisin
        self.prolin = prolin


class ChemlProd():
    
    def __init__(self, product, soluable_solids, ascorbic_acids, ash_content, moisture, protein, fat):
        self.product = product
        self.soluable_solids = soluable_solids
        self.ascorbic_acids = ascorbic_acids
        self.ash_content = ash_content
        self.moisture = moisture
        self.protein = protein
        self.fat = fat

    


#Meels Recips
def meels(request):
    ingredient = Ingredients.objects.all()

    MyClass = ChemlProd

    chemics = ChemlProd.__dict__
    amoinacids = aminoAc.__dict__

    types = Types.objects.all()
    cat = Categories.objects.values('Name_of_category').annotate(total=Count('Name_of_category'))

    protein = 0
    check = None
    region_choices = RegionChoice.choices
    # print(type(region_choices))
    hide_ingredients = None
    size = 0
    size = request.POST.get("counter")
    product = request.POST.get("product-name")

    prod_reg = request.GET.get("region_prod")
   
    arr = 0
    sum = 0
    ss = 0

    soluables_value = 0
    ascorbics_value = 0
    ash_contents_value = 0
    moisture_value = 0
    Proteins_value = 0
    summ_price = 0
    price_100 = 0
    price_1kg = 0
    fatacids_value = 0

    if request.method == "POST":
        if size is not None and size != 0:
            for i in range(0, int(size)+1):
                reg = request.POST.get(f'region_{i}')
                ing = request.POST.get(f'ing_{i}')
                mass_fraction = request.POST.get(f'massfraction_{i}')
                price = request.POST.get(f'price_{i}')

                try:
                    chemical_comp = ChemicalsIngredients.objects.get(ingredient=ing)
                    soluables_value += chemical_comp.soluable_solids
                    ascorbics_value += chemical_comp.ascorbic_acids
                    ash_contents_value += chemical_comp.ash_content
                    moisture_value += chemical_comp.moisture
                    summ_price = summ_price + float(price)
                    Proteins_value += float(mass_fraction) * chemical_comp.protein
                    fatacids_value += float(mass_fraction) * chemical_comp.fat

                    summ_price = float(price) * float(mass_fraction) / 1000         

                    price_100 += float(summ_price) * (100 / float(mass_fraction))
                    price_100 = round(price_100, 3)
                    price_1kg += float(summ_price) * (1000 / float(mass_fraction))
                    price_1kg = round(price_1kg, 3)

                    MyClass.product = product
                    
                    ss += float(mass_fraction)

                    Proteins_value = value_sum(Proteins_value, ss)
                    fatacids_value = value_sum(fatacids_value, ss)
                    Proteins_value = float("{:.2f}".format(3.8956))
                    fatacids_value = float("{:.2f}".format(3.6785))

                    MyClass.soluable_solids = soluables_value
                    MyClass.ascorbic_acids = ascorbics_value
                    MyClass.ash_content = ash_contents_value
                    MyClass.ash_content = soluables_value
                    MyClass.moisture = moisture_value
                    MyClass.protein = Proteins_value
                    MyClass.fat = fatacids_value
                    

                except Chemicals.DoesNotExist:
                    check = True

                context= {
                    'price_100' : price_100,
                    'price_1kg' : price_1kg,
                    'ingredient': ingredient,
                    'Protein_value': Proteins_value,
                    "MyClass": chemics,
                    "regions" : region_choices,
                    "hide_ingredients" : hide_ingredients,
                }

            return render(request, 'client/pages/meels.html', context)
        elif size == 0:
            reg = request.POST.get(f'region_0', None)

    
    not_exist = False
   
    try:
        chemical_comp = Chemicals.objects.all()
        # protein = (float(mass_fraction) * float(Chemicals.model.protein)) / float(mass_fraction)
        
    except Chemicals.DoesNotExist:
        check = True
    # if chemical_comp is None:
    #     check = True
    # else:

    context= {
        'ingredient': ingredient,
        "hide_result" : check,
        "categories": cat,
        "types": types,
        "amoinacids": amoinacids,
        "MyClass": chemics,
        "regions" : region_choices,
        "hide_ingredients" : hide_ingredients,
    }

    return render(request, 'client/pages/meels.html', context)


# Milks Recips
def milks(request):
    products = Products.objects.order_by('id')
    protein = 0
    check = None
    regions = Categories.objects.all()
    hide_ingredients = None

    region = request.GET.get('region')
    milk = request.GET.get('milk')
    mass_fraction = request.GET.get('massfraction')
    price = request.GET.get('price')

    not_exist = False
    
    try:
        chemical_comp = Chemicals.objects.get(product=milk)
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

    return render(request, 'client/pages/milks.html', context)

# Bakery Recips
def bakery(request):
    products = Products.objects.order_by('id')
    protein = 0
    check = None
    regions = Categories.objects.all()
    hide_ingredients = None

    region = request.GET.get('region')
    baker = request.GET.get('bakery')
    mass_fraction = request.GET.get('massfraction')
    price = request.GET.get('price')

    not_exist = False
    
    try:
        chemical_comp = Chemicals.objects.get(product=baker)
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

    return render(request, 'client/pages/bakery.html', context)


def list(request):
    list_of_products = Products.objects.order_by('id')
    
    context= {
        'list_of_products':list_of_products
    }

    return render(request, 'client/pages/list.html', context)








# Products CRUD operations

class ProductsView(View):
    model = Products
    form_class = ProductsForm
    active_panel = "products-panel"
    login_url = "login_page"
    success_url = reverse_lazy("products_create")
    extra_context = {
        "is_active" : active_panel,
        "active_products" : "active",
        "expand_products" : "show",
        }
    
class ProductsListView(LoginRequiredMixin, ProductsView, ListView):
    template_name = "admin/pages/products/products_list.html"
    paginate_by = 10

class ProductsCreateView(LoginRequiredMixin, SuccessMessageMixin, ProductsView, CreateView):
    template_name = 'admin/pages/products/products_form.html'
    success_message = "Запись успешно Добавлена!"  

class ProductsUpdateView(LoginRequiredMixin, SuccessMessageMixin, ProductsView, UpdateView):
    template_name = "admin/pages/products/products_form.html"
    success_url = reverse_lazy("products_all")
    success_message = "Запись успешно Обновлена!"

def products_delete(request, id):
    context = {
            "is_active" : "products-panel",
            "active_products" : "active",
            "expand_products" : "show",
    }
    obj = get_object_or_404(Products, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("products_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("products_delete")
 
    return render(request, "admin/pages/products/products_delete_confirm.html", context)  


# Categories CRUD operations

class CategoriesView(View):
    model = Categories
    form_class = CategoriesForm
    active_panel = "categories-panel"
    login_url = "login_page"
    success_url = reverse_lazy("categories_create")
    extra_context = {
        "is_active" : active_panel,
        "active_categories" : "active",
        "expand_categories" : "show",
        }
    
class CategoriesListView(LoginRequiredMixin, CategoriesView, ListView):
    template_name = "admin/pages/categories/categories_list.html"
    paginate_by = 10

class CategoriesCreateView(LoginRequiredMixin, SuccessMessageMixin, CategoriesView, CreateView):
    template_name = 'admin/pages/categories/categories_form.html'
    success_message = "Запись успешно Добавлена!"  

class CategoriesUpdateView(LoginRequiredMixin, SuccessMessageMixin, CategoriesView, UpdateView):
    template_name = "admin/pages/categories/categories_form.html"
    success_url = reverse_lazy("categories_all")
    success_message = "Запись успешно Обновлена!"

def categories_delete(request, id):
    context = {
            "is_active" : "categories-panel",
            "active_categories" : "active",
            "expand_categories" : "show",
    }
    obj = get_object_or_404(Categories, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("categories_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("categories_delete")
 
    return render(request, "admin/pages/categories/categories_delete_confirm.html", context)  



# Ingredients CRUD operations

class IngredientsView(View):
    model = Ingredients
    form_class = IngredientsForm
    active_panel = "ingredients-panel"
    login_url = "login_page"
    success_url = reverse_lazy("ingredients_create")
    extra_context = {
        "is_active" : active_panel,
        "active_ingredients" : "active",
        "expand_ingredients" : "show",
        }
    
class IngredientsListView(LoginRequiredMixin, IngredientsView, ListView):
    template_name = "admin/pages/ingredients/ingredients_list.html"
    paginate_by = 10

class IngredientsCreateView(LoginRequiredMixin, SuccessMessageMixin, IngredientsView, CreateView):
    template_name = 'admin/pages/ingredients/ingredients_form.html'
    success_message = "Запись успешно Добавлена!"  

class IngredientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, IngredientsView, UpdateView):
    template_name = "admin/pages/ingredients/ingredients_form.html"
    success_url = reverse_lazy("ingredients_all")
    success_message = "Запись успешно Обновлена!"

def ingredients_delete(request, id):
    context = {
            "is_active" : "ingredients-panel",
            "active_ingredients" : "active",
            "expand_ingredients" : "show",
    }
    obj = get_object_or_404(Ingredients, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("ingredients_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("ingredients_delete")
 
    return render(request, "admin/pages/ingredients/ingredients_delete_confirm.html", context)  


# Typs CRUD operations

class TypesView(View):
    model = Types
    form_class = TypesForm
    active_panel = "types-panel"
    success_url = reverse_lazy("types_create")
    extra_context = {
        "is_active" : active_panel,
        "active_types" : "active",
        "expand_types" : "show",
        }
    
class TypesListView(LoginRequiredMixin, TypesView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/types/types_list.html"
    paginate_by = 10

class TypesCreateView(LoginRequiredMixin, SuccessMessageMixin, TypesView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/types/types_form.html'
    success_message = "Запись успешно Добавлена!"  

class TypesUpdateView(LoginRequiredMixin, SuccessMessageMixin, TypesView, UpdateView):
    login_url = "login_page"
    template_name = "admin/pages/types/types_form.html"
    success_url = reverse_lazy("types_all")
    success_message = "Запись успешно Обновлена!"

def types_delete(request, id):
    context = {
            "is_active" : "types-panel",
            "active_types" : "active",
            "expand_types" : "show",
    }
    obj = get_object_or_404(Types, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("types_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("types_delete")
 
    return render(request, "admin/pages/types/types_delete_confirm.html", context)   



# Ingredients categpries CRUD operations



# Typs CRUD operations

class IngredientsCategoryView(View):
    model = Categories
    form_class = IngredientsCategoriesForm
    login_url = "login_page"
    active_panel = "ingredients_category-panel"
    success_url = reverse_lazy("ingredients_category_create")
    extra_context = {
        "is_active" : active_panel,
        "active_ingredients_category" : "active",
        "expand_ingredients_category" : "show",
        }
    
class IngredientsCategoryListView(LoginRequiredMixin, IngredientsCategoryView, ListView):
    template_name = "admin/pages/ingredients_category/ingredients_category_list.html"
    paginate_by = 10

class IngredientsCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, IngredientsCategoryView, CreateView):
    template_name = 'admin/pages/ingredients_category/ingredients_category_form.html'
    success_message = "Запись успешно Добавлена!"  

class IngredientsCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, IngredientsCategoryView, UpdateView):
    template_name = "admin/pages/ingredients_category/ingredients_category_form.html"
    success_url = reverse_lazy("ingredients_category_all")
    success_message = "Запись успешно Обновлена!"

def ingredients_category_delete(request, id):
    context = {
            "is_active" : "ingredients_category-panel",
            "active_ingredients_category" : "active",
            "expand_ingredients_category" : "show",
    }
    obj = get_object_or_404(Categories, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("ingredients_category_all")
        except models.RestrictedError as e:
            messages.error(request, "Нельзя удалить категорию, потому что имеется запись ингредиента в данной категории!")
            return redirect("chemicals_delete")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("ingredients_category_delete")
 
    return render(request, "admin/pages/ingredients_category/ingredients_category_delete_confirm.html", context)   


# FatAcidsIngredients CRUD operations

class FatAcidsIngredientsView(View):
    model = FatAcidsIngredients
    form_class = FatAcidsIngredientsForm
    active_panel = "fatacids_ingredients-panel"
    login_url = "login_page"
    success_url = reverse_lazy("fatacids_ingredients_create")
    extra_context = {
        "is_active" : active_panel,
        "active_fatacids_ingredients" : "active",
        "expand_fatacids_ingredients" : "show",
        }
    
class FatAcidsIngredientsListView(LoginRequiredMixin, FatAcidsIngredientsView, ListView):
    template_name = "admin/pages/fatacids_ingredients/fatacids_ingredients_list.html"
    paginate_by = 10

class FatAcidsIngredientsCreateView(LoginRequiredMixin, SuccessMessageMixin, FatAcidsIngredientsView, CreateView):
    template_name = 'admin/pages/fatacids_ingredients/fatacids_ingredients_form.html'
    success_message = "Запись успешно Добавлена!"  

class FatAcidsIngredientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, FatAcidsIngredientsView, UpdateView):
    template_name = "admin/pages/fatacids_ingredients/fatacids_ingredients_form.html"
    success_url = reverse_lazy("fatacids_ingredients_create")
    success_message = "Запись успешно Обновлена!"

def fatacids_ingredients_delete(request, id):
    context = {
            "is_active" : "fatacids_ingredients-panel",
            "active_fatacids_ingredients" : "active",
            "expand_fatacids_ingredients" : "show",
    }
    obj = get_object_or_404(FatAcidsIngredients, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("fatacids_ingredients_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("fatacids_ingredients_delete")
 
    return render(request, "admin/pages/fatacids_ingredients/fatacids_ingredients_delete_confirm.html", context) 


# Mineral composition Ingredients  CRUD operations

class MineralsIngredientsView(View):
    model = MineralsIngredients
    form_class = MineralsIngredientsForm
    active_panel = "minerals_ingredients-panel"
    success_url = reverse_lazy("minerals_ingredients_create")
    extra_context = {
        "is_active" : active_panel,
        "active_minerals_ingredients" : "active",
        "expand_minerals_ingredients" : "show",
        }
    
class MineralsIngredientsListView(LoginRequiredMixin, MineralsIngredientsView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/minerals_ingredients/minerals_ingredients_list.html"
    paginate_by = 10

class MineralsIngredientsCreateView(LoginRequiredMixin, SuccessMessageMixin, MineralsIngredientsView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/minerals_ingredients/minerals_ingredients_form.html'
    success_message = "Запись успешно Добавлена!" 

class MineralsIngredientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, MineralsIngredientsView, UpdateView):
    login_url = "login_page"
    template_name = "admin/pages/minerals_ingredients/minerals_ingredients_form.html"
    success_url = reverse_lazy("minerals_all")
    success_message = "Запись успешно Обновлена!"

def minerals_ingredients_delete(request, id):
    context = {
            "is_active" : "minerals_ingredients-panel",
            "active_minerals_ingredients" : "active",
            "expand_minerals_ingredients" : "show",
    }
    obj = get_object_or_404(MineralsIngredients, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("minerals_ingredients_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("minerals_ingredients_delete")
 
    return render(request, "admin/pages/minerals_ingredients/minerals_ingredients_delete_confirm.html", context) 


# AminoAcids Ingredients CRUD operations

class AminoAcidsIngredientsView(View):
    model = AminoAcidCompOfIng
    form_class = AminoAcidsIngredientsForm
    login_url = "login_page"
    active_panel = "aminoacids_ingredients-panel"
    success_url = reverse_lazy("aminoacids_ingredients_create")
    extra_context = {
        "is_active" : active_panel,
        "active_aminoacids_ingredients" : "active",
        "expand_aminoacids_ingredients" : "show",
        }
    
class AminoAcidsIngredientsListView(LoginRequiredMixin, AminoAcidsIngredientsView, ListView):
    template_name = "admin/pages/aminoacids_ingredients/aminoacids_ingredients_list.html"
    paginate_by = 10

class AminoAcidsIngredientsCreateView(LoginRequiredMixin, SuccessMessageMixin, AminoAcidsIngredientsView, CreateView):
    template_name = 'admin/pages/aminoacids_ingredients/aminoacids_ingredients_form.html'
    success_message = "Запись успешно Добавлена!" 

class AminoAcidsIngredientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, AminoAcidsIngredientsView, UpdateView):
    template_name = "admin/pages/aminoacids_ingredients/aminoacids_ingredients_form.html"
    success_message = "Запись успешно Обновлена!"

def aminoacids_ingredients_delete(request, id):
    context = {
            "is_active" : "aminoacids_ingredients-panel",
            "active_aminoacids_ingredients" : "active",
            "expand_aminoacids_ingredients" : "show",
    }
    obj = get_object_or_404(AminoAcidCompOfIng, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("aminoacids_ingredients_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("aminoacids_ingredients_delete")
 
    return render(request, "admin/pages/aminoacids_ingredients/aminoacids_ingredients_delete_confirm.html", context)

# Chemical compositions ingredients CRUD operations

class ChemicalsIngredientsView(View):
    model = ChemicalsIngredients
    form_class = ChemicalsIngredientsForm
    login_url = "login_page"
    active_panel = "chemicals_ingredients-panel"
    success_url = reverse_lazy("chemicals_ingredients_create")
    extra_context = {
        "is_active" : active_panel,
        "active_chemicals_ingredients" : "active",
        "expand_chemicals_ingredients" : "show",
        }
    
class ChemicalsIngredientsListView(LoginRequiredMixin, ChemicalsIngredientsView, ListView):
    template_name = "admin/pages/chemicals_ingredients/chemicals_ingredients_list.html"
    paginate_by = 10

class ChemicalsIngredientsCreateView(LoginRequiredMixin, SuccessMessageMixin, ChemicalsIngredientsView, CreateView):
    template_name = 'admin/pages/chemicals_ingredients/chemicals_ingredients_form.html'
    success_message = "Запись успешно Добавлена!" 

class ChemicalsIngredientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, ChemicalsIngredientsView, UpdateView):
    template_name = "admin/pages/chemicals_ingredients/chemicals_ingredients_form.html"
    success_message = "Запись успешно Обновлена!"

def chemicals_ingredients_delete(request, id):
    context = {
            "is_active" : "chemicals_ingredients-panel",
            "active_chemicals_ingredients" : "active",
            "expand_chemicals_ingredients" : "show",
    }
    obj = get_object_or_404(ChemicalsIngredients, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("chemicals_ingredients_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("chemicals_ingredients_delete")
 
    return render(request, "admin/pages/chemicals_ingredients/chemicals_ingredients_delete_confirm.html", context)


# FatAcids CRUD operations

class FatAcidsView(View):
    model = FatAcids
    form_class = FatAcidsForm
    active_panel = "fatacids-panel"
    login_url = "login_page"
    success_url = reverse_lazy("fatacids_create")
    extra_context = {
        "is_active" : active_panel,
        "active_fatacids" : "active",
        "expand_fatacids" : "show",
        }
    
class FatAcidsListView(LoginRequiredMixin, FatAcidsView, ListView):
    template_name = "admin/pages/fatacids/fatacids_list.html"
    paginate_by = 10

class FatAcidsCreateView(LoginRequiredMixin, SuccessMessageMixin, FatAcidsView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/fatacids/fatacids_form.html'
    success_message = "Запись успешно Добавлена!"  

class FatAcidsUpdateView(LoginRequiredMixin, SuccessMessageMixin, FatAcidsView, UpdateView):
    template_name = "admin/pages/fatacids/fatacids_form.html"
    success_url = reverse_lazy("fatacids_create")
    success_message = "Запись успешно Обновлена!"

def fatacids_delete(request, id):
    context = {
            "is_active" : "fatacids-panel",
            "active_fatacids" : "active",
            "expand_fatacids" : "show",
    }
    obj = get_object_or_404(FatAcids, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("fatacids_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("fatacids_delete")
 
    return render(request, "admin/pages/fatacids/fatacids_delete_confirm.html", context) 


# Mineral compositions CRUD operations

class MineralsView(View):
    model = MineralComposition
    form_class = MineralForm
    active_panel = "minerals-panel"
    success_url = reverse_lazy("minerals_create")
    extra_context = {
        "is_active" : active_panel,
        "active_minerals" : "active",
        "expand_minerals" : "show",
        }
    
class MineralsListView(LoginRequiredMixin, MineralsView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/minerals/minerals_list.html"
    paginate_by = 10

class MineralsCreateView(LoginRequiredMixin, SuccessMessageMixin, MineralsView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/minerals/minerals_form.html'
    success_message = "Запись успешно Добавлена!" 

class MineralsUpdateView(LoginRequiredMixin, SuccessMessageMixin, MineralsView, UpdateView):
    login_url = "login_page"
    template_name = "admin/pages/minerals/minerals_form.html"
    success_url = reverse_lazy("minerals_all")
    success_message = "Запись успешно Обновлена!"

def minerals_delete(request, id):
    context = {
            "is_active" : "minerals-panel",
            "active_minerals" : "active",
            "expand_minerals" : "show",
    }
    obj = get_object_or_404(MineralComposition, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("minerals_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("minerals_delete")
 
    return render(request, "admin/pages/minerals/minerals_delete_confirm.html", context) 

# AminoAcids CRUD operations

class AminoAcidsView(View):
    model = AminoAcidComposition
    form_class = AminoAcidsForm
    login_url = "login_page"
    active_panel = "aminoacids-panel"
    success_url = reverse_lazy("aminoacids_create")
    extra_context = {
        "is_active" : active_panel,
        "active_aminoacids" : "active",
        "expand_aminoacids" : "show",
        }
    
class AminoAcidsListView(LoginRequiredMixin, AminoAcidsView, ListView):
    template_name = "admin/pages/aminoacids/aminoacids_list.html"
    paginate_by = 10

class AminoAcidsCreateView(LoginRequiredMixin, SuccessMessageMixin, AminoAcidsView, CreateView):
    template_name = 'admin/pages/aminoacids/aminoacids_form.html'
    success_message = "Запись успешно Добавлена!" 

class AminoAcidsUpdateView(LoginRequiredMixin, SuccessMessageMixin, AminoAcidsView, UpdateView):
    template_name = "admin/pages/aminoacids/aminoacids_form.html"
    success_message = "Запись успешно Обновлена!"

def aminoacids_delete(request, id):
    context = {
            "is_active" : "aminoacids-panel",
            "active_aminoacids" : "active",
            "expand_aminoacids" : "show",
    }
    obj = get_object_or_404(AminoAcidComposition, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("aminoacids_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("aminoacids_delete")
 
    return render(request, "admin/pages/aminoacids/aminoacids_delete_confirm.html", context)


# Chemical compositions CRUD operations

class ChemicalsView(View):
    model = Chemicals
    form_class = ChemicalsForm
    login_url = "login_page"
    active_panel = "chemicals-panel"
    success_url = reverse_lazy("chemicals_create")
    extra_context = {
        "is_active" : active_panel,
        "active_chemicals" : "active",
        "expand_chemicals" : "show",
        }
    
class ChemicalsListView(LoginRequiredMixin, ChemicalsView, ListView):
    template_name = "admin/pages/chemicals/chemicals_list.html"
    paginate_by = 10

class ChemicalsCreateView(LoginRequiredMixin, SuccessMessageMixin, ChemicalsView, CreateView):
    template_name = 'admin/pages/chemicals/chemicals_form.html'
    success_message = "Запись успешно Добавлена!" 

class ChemicalsUpdateView(LoginRequiredMixin, SuccessMessageMixin, ChemicalsView, UpdateView):
    template_name = "admin/pages/chemicals/chemicals_form.html"
    success_message = "Запись успешно Обновлена!"

def chemicals_delete(request, id):
    context = {
            "is_active" : "chemicals-panel",
            "active_chemicals" : "active",
            "expand_chemicals" : "show",
    }
    obj = get_object_or_404(Chemicals, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("chemicals_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("chemicals_delete")
    
    return render(request, "admin/pages/chemicals/chemicals_delete_confirm.html", context)


def product_details(request, id):
        
    product_id = Products.objects.get(id=id)
    fatacids = FatAcids.objects.filter(product=id)
    mineracomp = MineralComposition.objects.filter(product=id)
    amoinacids = AminoAcidComposition.objects.filter(product=id)
    chemicals = Chemicals.objects.filter(product=id)
    context= {
        'product_id': product_id,
        'fatacids': fatacids,
        'mineracomp': mineracomp ,
        'amoinacids': amoinacids,
        'chemicals': chemicals,
    }
        
    return render(request, 'client/pages/details.html',context)
