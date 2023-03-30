from .models import *
from django.forms import ModelForm, DateTimeInput, TextInput, Textarea, DateInput
from django import forms
from django.contrib.auth.models import User
import re
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите адрес электронной почты',
        'type': 'email',
        'name': 'email',
        'id': 'id_email',
        }))

class UserSetPasswordForm(SetPasswordForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите новый пароль',
        'type': 'password',
        'name': 'password1',
        'id': 'id_pass1',
        'strip': 'False',
        })
    )

    new_password2 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль еще раз',
        'type': 'password',
        'name': 'password2',
        'id': 'id_pass2',
        })
    )

# Форма для профиля   
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email']
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', "id" : "last_name", "placeholder" : "Введите Имя"}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', "id" : "first_name", "placeholder" : "Введите Фамилию"}))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', "id" : "username", "placeholder" : "Введите Имя Пользователя"}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', "id" : "email", "placeholder" : "Введите E-mail"}))

    class Meta:
        model = User
        fields = ['username', 'email']


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'category']
    
    name = forms.CharField(max_length=80, required=True, widget=TextInput(
            attrs={"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Введите наименование ингредиента", "size" : 80},
            ))
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "types"},
            ))
    
class IngredientsCategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['Name_of_category', 'Region']
    
    Name_of_category = forms.CharField(max_length=80, required=True, widget=TextInput(
            attrs={"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Введите категорию ингредиента", "size" : 80},
            ))
    Region = forms.ChoiceField(
                                choices=RegionChoice.choices,
                                widget= forms.Select(
                                        attrs={"class" : "form-control", "id" : "Region"}
                                    ),
                                required=True
                            )


class FatAcidsIngredientsForm(ModelForm):
    class Meta:
        model = FatAcidsIngredients
        fields = ['ingredient', 'type_of_acid', 'value']
    
    ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "ingredient"},
            ))
    
    type_of_acid = forms.CharField(max_length=50,
                                widget= forms.Select(
                                        attrs={"class" : "form-control", "id" : "type_of_acid"},
                                        choices=FatAcidsTypeChoice.choices
                                    )
                            )
    
    value = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    
class MineralsIngredientsForm(ModelForm):
    class Meta:
        model = MineralsIngredients
        fields = ['ingredient', 'Ca', 'Na', 'K', 'P', 'Mn',
                    'Zn', 'Se', 'Cu', 'Fe', 'I', 'B', 'Li',
                    'Al', 'Mg', 'V', 'Ni', 'Co', 'Cr', 'Sn']
    
    ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "ingredient"},
            ))
    
    Ca = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Na = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    K = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    P = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Mn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Zn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Se = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Cu = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Fe = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    I = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    B = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Li = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Al = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Mg = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    V = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Ni = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Co = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Cr = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Sn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    

class AminoAcidsIngredientsForm(ModelForm):
    class Meta:
        model = AminoAcidCompOfIng
        fields = ['ingredient', 'asparing', 'glutamin', 'serin', 'gistidin', 'glitsin', 'treonin', 'arginin', 'alanin',
                  'tirosin', 'tsistein', 'valin', 'metionin', 'triptofan', 'fenilalalin', 'izoleitsin', 'leitsin', 'lisin', 'prolin']
    
    ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "ingredient"},
            ))
    
    asparing = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    glutamin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    serin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    gistidin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    glitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    treonin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    arginin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    alanin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    tirosin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    tsistein = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    valin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    metionin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    triptofan = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    fenilalalin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    izoleitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    leitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    lisin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    prolin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))

class ChemicalsIngredientsForm(ModelForm):
    class Meta:
        model = ChemicalsIngredients
        fields = ['ingredient', 'soluable_solids', 'ascorbic_acids', 'ash_content', 'moisture', 'protein', 'fat']
    
    ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "ingredient"},
            ))
    
    soluable_solids = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    ascorbic_acids = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    ash_content = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    moisture = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    protein = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    fat = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))



class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['attribute_name', 'types', 'date_analis']
    
    attribute_name = forms.CharField(max_length=80, required=True, widget=TextInput(
            attrs={"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Введите наименование ингредиента", "size" : 80},
            ))
    types = forms.ModelChoiceField(queryset=Types.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "types"},
            ))
    date_analis = forms.DateField(required=False, 
                               widget=DateInput(
                                   attrs={"type" : "date", "class" : "form-control", "id" : "date_analis"}
                                   )
                               )
    

class TypesForm(ModelForm):
    class Meta:
        model = Types
        fields = ['Name_of_type', 'Category']
    
    Name_of_type = forms.CharField(max_length=80, required=True, widget=TextInput(
            attrs={"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Введите наименование продукта", "size" : 80},
            ))
    Category = forms.ModelChoiceField(queryset=Categories.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "types"},
            ))
    
class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['Name_of_category', 'Region']
    
    Name_of_category = forms.CharField(max_length=80, required=True, widget=TextInput(
            attrs={"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Введите категорию ингредиента", "size" : 80},
            ))
    Region = forms.ChoiceField(
                                choices=RegionChoice.choices,
                                widget= forms.Select(
                                        attrs={"class" : "form-control", "id" : "Region"}
                                    ),
                                required=True
                            )


class FatAcidsForm(ModelForm):
    class Meta:
        model = FatAcids
        fields = ['product', 'type_of_acid', 'value']
    
    product = forms.ModelChoiceField(queryset=Products.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "product"},
            ))
    
    type_of_acid = forms.CharField(max_length=50,
                                widget= forms.Select(
                                        attrs={"class" : "form-control", "id" : "type_of_acid"},
                                        choices=FatAcidsTypeChoice.choices
                                    )
                            )
    
    value = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    
class MineralForm(ModelForm):
    class Meta:
        model = MineralComposition
        fields = ['product', 'Ca', 'Na', 'K', 'P', 'Mn',
                    'Zn', 'Se', 'Cu', 'Fe', 'I', 'B', 'Li',
                    'Al', 'Mg', 'V', 'Ni', 'Co', 'Cr', 'Sn']
    
    product = forms.ModelChoiceField(queryset=Products.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "product"},
            ))
    
    Ca = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Na = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    K = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    P = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Mn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Zn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Se = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Cu = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Fe = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    I = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    B = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Li = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Al = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Mg = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    V = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Ni = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Co = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Cr = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    Sn = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    

class AminoAcidsForm(ModelForm):
    class Meta:
        model = AminoAcidComposition
        fields = ['product', 'asparing', 'glutamin', 'serin', 'gistidin', 'glitsin', 'treonin', 'arginin', 'alanin',
                  'tirosin', 'tsistein', 'valin', 'metionin', 'triptofan', 'fenilalalin', 'izoleitsin', 'leitsin', 'lisin', 'prolin']
    
    product = forms.ModelChoiceField(queryset=Products.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "product"},
            ))
    
    asparing = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    glutamin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    serin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    gistidin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    glitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    treonin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    arginin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    alanin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    tirosin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    tsistein = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    valin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    metionin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    triptofan = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    fenilalalin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    izoleitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    leitsin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    lisin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    prolin = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    
class ChemicalsForm(ModelForm):
    class Meta:
        model = Chemicals
        fields = ['product', 'soluable_solids', 'ascorbic_acids', 'ash_content', 'moisture', 'protein', 'fat']
    
    product = forms.ModelChoiceField(queryset=Products.objects.all(), 
                                     widget=forms.Select(attrs={"class": "form-control", 'required': True, "id" : "product"},
            ))
    
    soluable_solids = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    ascorbic_acids = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    ash_content = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    moisture = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    protein = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))
    fat = forms.FloatField(widget=forms.widgets.NumberInput(attrs={'step': 0.01, 'max': 100.0, 'min': 0.0}))