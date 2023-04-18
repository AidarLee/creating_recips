import json
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


#Designing Recips
def meels(request):
    ingredient = Ingredients.objects.all()
    check = False
    region_choices = RegionChoice.choices
    hide_ingredients = None

    context= {
        'ingredient': ingredient,
        "hide_result" : check,
        "regions" : region_choices,
        "hide_ingredients" : hide_ingredients,
    }

    return render(request, 'client/pages/meels.html', context)

class Result:

    def __init__(self, 
                 protein, fatacid, carbohydrates, price_100, price_1kg, isolecin, leitsin, valin,
                met_tsist2, fenilalalin_tirosin2, triptofan, lisin, treonin, isolecin2, leitsin2, 
                valin2, met_tsist3, fenilalalin_tirosin3, triptofan2, lisin2, treonin2, isolecin_a,
                leitsin_a, valin_a, met_tsist_a, fenilalalin_tirosin_a, triptofan_a, lisin_a, treonin_a,
                Cmin, power_kkal, power_kDj, kras, bc, U, G
                 ):
        self.protein = protein
        self.fatacid = fatacid
        self.carbohydrates = carbohydrates
        self.price_100 = price_100
        self.price_1kg = price_1kg
        self.isolecin = isolecin
        self.leitsin = leitsin
        self.valin = valin
        self.met_tsist2 = met_tsist2
        self. fenilalalin_tirosin2 = fenilalalin_tirosin2
        self.triptofan = triptofan
        self.lisin = lisin
        self.treonin = treonin
        self.isolecin2 = isolecin2
        self.leitsin2 = leitsin2
        self.valin2 = valin2
        self.met_tsist3 = met_tsist3
        self.fenilalalin_tirosin3 = fenilalalin_tirosin3
        self.triptofan2 = triptofan2
        self.lisin2 = lisin2
        self.treonin2 = treonin2
        self.isolecin_a = isolecin_a
        self.leitsin_a = leitsin_a
        self.valin_a = valin_a
        self.met_tsist_a = met_tsist_a
        self.fenilalalin_tirosin_a = fenilalalin_tirosin_a
        self.triptofan_a = triptofan_a
        self.lisin_a = lisin_a
        self.treonin_a = treonin_a
        self.Cmin = Cmin
        self.power_kkal = power_kkal
        self.power_kDj = power_kDj
        self.kras = kras
        self.bc = bc
        self.U = U
        self.G = G



#Ajax Region
def load_courses(request):
    reg = request.GET.get('regionId')
    ingredient = Ingredients.objects.filter(category__Region = reg)
    return render(request, 'client/pages/dropdown_list_options.html', {'ingredients': ingredient})

#Ajax calculations
def load_calculation(request):
    
    res = Result
    result = Result.__dict__

    mass_fractions = 0
    
    protein = 0.0
    prot = 0
    chemicals_prot = None
    
    chemicals_fat = None
    fatacid = 0
    fat = 0

    chemicals_carbo = None
    carbohydrates = 0
    carbo = 0

    # price.i 
    price_i = 0
    
    #price_1kg * mass_fraction / 1000
    pr = 0

    #price sum
    prplus = 0
    price_100 = 0
    price_1kg = 0

    #isoleicin
    amino_isoleicin = 0
    isol = 0
    isolecin = 0

    #leitsin
    amino_leitsin = 0
    leit = 0
    leitsin = 0

    #valin
    amino_valin = 0
    val = 0
    valin = 0

    #metionin
    amino_met = 0
    met = 0
    met_tsist1 = 0

    #tsistein
    amino_tsistein = 0
    tsist = 0
    met_tsist2 = 0

    #fenilalalin
    amino_fenilalalin = 0
    fenil = 0
    fenilalalin_tirosin1 = 0

    #tirosin
    amino_tirosin = 0
    tir = 0
    fenilalalin_tirosin2 = 0

    #triptofan
    amino_triptofan = 0
    tripto = 0
    triptofan = 0

    #lisin
    amino_lisin = 0
    lis = 0
    lisin = 0

    #treonin
    amino_treonin = 0
    treon = 0
    treonin = 0

    error_message = ""
    
    reg = json.loads(request.GET.get(('Regions')))
    ingredient = json.loads(request.GET.get('Ingredients'))
    mass_fraction = json.loads(request.GET.get('MassFractions'))
    price = json.loads(request.GET.get('Prices'))
    size = request.GET.get('counters')

    for i in range(0, int(size)+1):
        try:
            ing = ingredient[i]
            ingred = Ingredients.objects.get(id=ing)
            
            chemical_comp = ChemicalsIngredients.objects.get(ingredient=ing)
            aminocaid_comp = AminoAcidCompOfIng.objects.get(ingredient=ing)

            #protein
            chemicals_prot = chemical_comp.protein
            mass = float(mass_fraction[i])
            mass_fractions += mass
            prot += (float(mass) * chemicals_prot)

            #price
            price_i = price[i]
            pr = (float(price_i) * mass) / 1000
            prplus += pr

            #fatacid
            chemicals_fat = chemical_comp.fat
            fat +=(float(mass)) * chemicals_fat

            #carbohydrates
            chemicals_carbo = chemical_comp.carbohydrates
            carbo +=(float(mass)*chemicals_carbo)

            #isoleicin
            amino_isoleicin = aminocaid_comp.izoleitsin
            isol += amino_isoleicin

            #leitsin
            amino_leitsin = aminocaid_comp.leitsin
            leit += amino_leitsin

            #valin
            amino_valin = aminocaid_comp.valin
            val += amino_valin

            #amino_met
            amino_met = aminocaid_comp.metionin
            met += amino_met

            #tsistein
            amino_tsistein = aminocaid_comp.tsistein
            tsist += amino_tsistein

            #amino_fenilalalin
            amino_fenilalalin = aminocaid_comp.fenilalalin
            fenil += amino_fenilalalin

            #amino_tirosin
            amino_tirosin = aminocaid_comp.tirosin
            tir += amino_tirosin

            #amino_triptofan
            amino_triptofan = aminocaid_comp.triptofan
            tripto = amino_triptofan

            #amino_lisin
            amino_lisin = aminocaid_comp.lisin
            lis = amino_lisin

            #amino_treonin
            amino_treonin = aminocaid_comp.treonin
            treon = amino_treonin

        except ChemicalsIngredients.DoesNotExist:
            error_message = "Не удалось найти ингредиент с таким названием!"
    
    protein = prot / mass_fractions
    fatacid = fat / mass_fractions
    carbohydrates = carbo / mass_fractions
    price_100 = (prplus * 100) / mass_fractions
    price_1kg = price_100 * 10
    isolecin = (isol * prot * mass_fractions) / (prot * mass_fractions)
    isolecin2 = isolecin / 4 * 100
    leitsin = (leit * prot * mass_fractions) / (prot * mass_fractions)
    leitsin2 = leitsin / 7 * 100
    valin = (val * prot * mass_fractions) / (prot * mass_fractions)
    valin2 = valin / 5 * 100

    met_tsist1 = met + tsist
    fenilalalin_tirosin1 = fenil + tir

    met_tsist2 = (met_tsist1 * prot * mass_fractions) / (prot * mass_fractions)
    met_tsist3 = met_tsist2 / 3.5 * 100
    fenilalalin_tirosin2 = (fenilalalin_tirosin1 * prot * mass_fractions) / (prot * mass_fractions)
    fenilalalin_tirosin3 = fenilalalin_tirosin2 / 6 * 100

    triptofan = (tripto * prot * mass_fractions) / (prot * mass_fractions)
    triptofan2 = triptofan / 1 * 100
    lisin = (lis * prot * mass_fractions) / (prot * mass_fractions)
    lisin2 = lisin / 4 * 100
    treonin = (treon * prot * mass_fractions) / (prot * mass_fractions)
    treonin2 = treonin / 5.5 * 100
    Cmin = min(isolecin2, leitsin2, valin2, met_tsist3, fenilalalin_tirosin3, triptofan2, lisin2, treonin2)

    isolecin_a = Cmin/isolecin2
    leitsin_a = Cmin/leitsin2
    valin_a = Cmin/valin2
    met_tsist_a = Cmin/met_tsist3
    fenilalalin_tirosin_a = Cmin/fenilalalin_tirosin3
    triptofan_a = Cmin/triptofan2
    lisin_a = Cmin/lisin2
    treonin_a = Cmin/treonin2

    power_kkal = protein * 4 + fatacid * 9 + carbohydrates * 4
    power_kDj = protein * 17 + fatacid * 37 + carbohydrates * 4

    kras = (isolecin2 - Cmin + leitsin2 - Cmin + valin2 - Cmin + met_tsist3 - Cmin + fenilalalin_tirosin3 - Cmin + triptofan2 - Cmin + lisin2 - Cmin + treonin2 - Cmin) / 8
    bc = 100 - kras
    U = isolecin * isolecin_a + leitsin * leitsin_a + valin * valin_a + met_tsist2 * met_tsist_a + fenilalalin_tirosin2 * fenilalalin_tirosin_a + triptofan * triptofan_a + treonin * treonin_a + lisin * lisin_a
    G = isolecin * (1 - isolecin_a) + leitsin * (1 - leitsin_a) + valin * (1 - valin_a) + met_tsist2 * (1 - met_tsist_a) + fenilalalin_tirosin2 * (1 - fenilalalin_tirosin_a) + triptofan * (1 - triptofan_a) + treonin * (1 - treonin_a) + lisin * (1 - lisin_a)

    res.protein = round(protein, 3)
    res.fatacid = round(fatacid, 3)
    res.carbohydrates = round(carbohydrates, 3)
    res.price_100 = round(price_100, 3)
    res.price_1kg = round(price_1kg, 3)
    res.isolecin = round(isolecin, 3)
    res.isolecin2 = round(isolecin2, 3)
    res.leitsin = round(leitsin, 3)
    res.leitsin2 = round(leitsin2, 3)
    res.valin = round(valin, 3)
    res.valin2 = round(valin2, 3)
    res.met_tsist2 = round(met_tsist2, 3)
    res.met_tsist3 = round(met_tsist3, 3)
    res.fenilalalin_tirosin2 = round(fenilalalin_tirosin2, 3)
    res.fenilalalin_tirosin3 = round(fenilalalin_tirosin3, 3)
    res.triptofan = round(triptofan, 3)
    res.triptofan2 = round(triptofan2, 3)
    res.lisin = round(lisin, 3)
    res.lisin2 = round(lisin2, 3)
    res.treonin = round(treonin, 3)
    res.treonin2 = round(treonin2, 3)
    res.Cmin = round(Cmin, 3)
    res.isolecin_a = round(isolecin_a, 3)
    res.leitsin_a = round(leitsin_a, 3)
    res.valin_a = round(valin_a, 3)
    res.met_tsist_a = round(met_tsist_a, 3)
    res.fenilalalin_tirosin_a = round(fenilalalin_tirosin_a, 3)
    res.triptofan_a = round(triptofan_a, 3)
    res.lisin_a = round(lisin_a, 3)
    res.treonin_a = round(treonin_a, 3)
    res.power_kkal = round(power_kkal, 3)
    res.power_kDj = round(power_kDj, 3)
    res.kras = round(kras, 3)
    res.bc = round(bc, 3)
    res.U = round(U, 3)
    res.G = round(G, 3)

    context = {
        'ingredients': ingredient,
        'region' : reg,
        'error_message' : error_message,
        'chemicals' : result,
    }

    return render(request, 'client/pages/load-calculation.html', context)



def list(request):
    actual_url = request.path.split('/')[2]
    list_of_products = Products.objects.order_by('id')
    
    context= {
        'list_of_products':list_of_products,
        'actual_url':actual_url,
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
