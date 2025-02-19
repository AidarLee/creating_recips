from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Main page index
    path('', views.index, name='index'),


    #Admin urls
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/login/success/', views.authorization, name='authorizate'),
    path('accounts/logout/', views.logout_page, name = 'logout_page'),

    path(r'admin-panel/profile/update/^', views.ProfileUpdateView.as_view(), name = 'update_profile'),
    path(r'admin-panel/profile/update/^/change_password/', views.ChangePasswordView.as_view(), name = 'change_password'),
    path('admin-panel/main/', views.AdminMain.as_view(), name='admin_panel'),
    path('admin-panel/testmethod/', views.test, name='test'),

    path('admin-panel/testmethod/', views.test, name='password_reset'),
    
    # Ingredients View
    path('admin-panel/ingredients/all/', views.IngredientsListView.as_view(), name='ingredients_all'),
    path('admin-panel/ingredients/create/', views.IngredientsCreateView.as_view(), name='ingredients_create'),
    path('admin-panel/ingredients/update/<int:pk>/', views.IngredientsUpdateView.as_view(), name='ingredients_update'),
    path('admin-panel/ingredients/delete/<int:id>/', views.ingredients_delete, name='ingredients_delete'),

    # Types View
    path('admin-panel/types/all/', views.TypesListView.as_view(), name='types_all'),
    path('admin-panel/types/create/', views.TypesCreateView.as_view(), name='types_create'),
    path('admin-panel/types/update/<int:pk>/', views.TypesUpdateView.as_view(), name='types_update'),
    path('admin-panel/types/delete/<int:id>/', views.types_delete, name='types_delete'),

    # Ingredients categories View
    path('admin-panel/ingredients_category/all/', views.IngredientsCategoryListView.as_view(), name='ingredients_category_all'),
    path('admin-panel/ingredients_category/create/', views.IngredientsCategoryCreateView.as_view(), name='ingredients_category_create'),
    path('admin-panel/ingredients_category/update/<int:pk>/', views.IngredientsCategoryUpdateView.as_view(), name='ingredients_category_update'),
    path('admin-panel/ingredients_category/delete/<int:id>/', views.ingredients_category_delete, name='ingredients_category_delete'),

    # FatAcids Ingredients View
    path('admin-panel/fatacids_ingredients/all/', views.FatAcidsIngredientsListView.as_view(), name='fatacids_ingredients_all'),
    path('admin-panel/fatacids_ingredients/create/', views.FatAcidsIngredientsCreateView.as_view(), name='fatacids_ingredients_create'),
    path('admin-panel/fatacids_ingredients/update/<int:pk>/', views.FatAcidsIngredientsUpdateView.as_view(), name='fatacids_ingredients_update'),
    path('admin-panel/fatacids_ingredients/delete/<int:id>/', views.fatacids_ingredients_delete, name='fatacids_ingredients_delete'),

    # Minerals Ingredients View
    path('admin-panel/minerals_ingredients/all/', views.MineralsIngredientsListView.as_view(), name='minerals_ingredients_all'),
    path('admin-panel/minerals_ingredients/create/', views.MineralsIngredientsCreateView.as_view(), name='minerals_ingredients_create'),
    path('admin-panel/minerals_ingredients/update/<int:pk>/', views.MineralsIngredientsUpdateView.as_view(), name='minerals_ingredients_update'),
    path('admin-panel/minerals_ingredients/delete/<int:id>/', views.minerals_ingredients_delete, name='minerals_ingredients_delete'),

    # AminoAcids Ingredients View
    path('admin-panel/aminoacids_ingredients/all/', views.AminoAcidsIngredientsListView.as_view(), name='aminoacids_ingredients_all'),
    path('admin-panel/aminoacids_ingredients/create/', views.AminoAcidsIngredientsCreateView.as_view(), name='aminoacids_ingredients_create'),
    path('admin-panel/aminoacids_ingredients/update/<int:pk>/', views.AminoAcidsIngredientsUpdateView.as_view(), name='aminoacids_ingredients_update'),
    path('admin-panel/aminoacids_ingredients/delete/<int:id>/', views.aminoacids_ingredients_delete, name='aminoacids_ingredients_delete'),

    # Chemicals Ingredients View
    path('admin-panel/chemicals_ingredients/all/', views.ChemicalsIngredientsListView.as_view(), name='chemicals_ingredients_all'),
    path('admin-panel/chemicals_ingredients/create/', views.ChemicalsIngredientsCreateView.as_view(), name='chemicals_ingredients_create'),
    path('admin-panel/chemicals_ingredients/update/<int:pk>/', views.ChemicalsIngredientsUpdateView.as_view(), name='chemicals_ingredients_update'),
    path('admin-panel/chemicals_ingredients/delete/<int:id>/', views.chemicals_ingredients_delete, name='chemicals_ingredients_delete'),


    # Products View
    path('admin-panel/products/all/', views.ProductsListView.as_view(), name='products_all'),
    path('admin-panel/products/create/', views.ProductsCreateView.as_view(), name='products_create'),
    path('admin-panel/products/update/<int:pk>/', views.ProductsUpdateView.as_view(), name='products_update'),
    path('admin-panel/products/delete/<int:id>/', views.products_delete, name='products_delete'),

    # Ingredients categories View
    path('admin-panel/category/all/', views.CategoriesListView.as_view(), name='categories_all'),
    path('admin-panel/category/create/', views.CategoriesCreateView.as_view(), name='categories_create'),
    path('admin-panel/category/update/<int:pk>/', views.CategoriesUpdateView.as_view(), name='categories_update'),
    path('admin-panel/category/delete/<int:id>/', views.categories_delete, name='categories_delete'),

    # FatAcids View
    path('admin-panel/fatacids/all/', views.FatAcidsListView.as_view(), name='fatacids_all'),
    path('admin-panel/fatacids/create/', views.FatAcidsCreateView.as_view(), name='fatacids_create'),
    path('admin-panel/fatacids/update/<int:pk>/', views.FatAcidsUpdateView.as_view(), name='fatacids_update'),
    path('admin-panel/fatacids/delete/<int:id>/', views.fatacids_delete, name='fatacids_delete'),

    # Minerals View
    path('admin-panel/minerals/all/', views.MineralsListView.as_view(), name='minerals_all'),
    path('admin-panel/minerals/create/', views.MineralsCreateView.as_view(), name='minerals_create'),
    path('admin-panel/minerals/update/<int:pk>/', views.MineralsUpdateView.as_view(), name='minerals_update'),
    path('admin-panel/minerals/delete/<int:id>/', views.minerals_delete, name='minerals_delete'),

    # AminoAcids View
    path('admin-panel/aminoacids/all/', views.AminoAcidsListView.as_view(), name='aminoacids_all'),
    path('admin-panel/aminoacids/create/', views.AminoAcidsCreateView.as_view(), name='aminoacids_create'),
    path('admin-panel/aminoacids/update/<int:pk>/', views.AminoAcidsUpdateView.as_view(), name='aminoacids_update'),
    path('admin-panel/aminoacids/delete/<int:id>/', views.aminoacids_delete, name='aminoacids_delete'),

    # Chemicals View
    path('admin-panel/chemicals/all/', views.ChemicalsListView.as_view(), name='chemicals_all'),
    path('admin-panel/chemicals/create/', views.ChemicalsCreateView.as_view(), name='chemicals_create'),
    path('admin-panel/chemicals/update/<int:pk>/', views.ChemicalsUpdateView.as_view(), name='chemicals_update'),
    path('admin-panel/chemicals/delete/<int:id>/', views.chemicals_delete, name='chemicals_delete'),


    #Client urls
    path('about', views.about, name='about-us'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('meels/', views.meels, name='meels'),
    path('list', views.list, name='list-of-products'),
    path('details/<int:id>', views.product_details, name='details'),

    #Ajax-regions choice
    path('load-regions/', views.load_courses, name='ajax_load_region'),
    path('load-calculations/', views.load_calculation, name='ajax_load_calculation'),
]