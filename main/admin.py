from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Types)
admin.site.register(Ingredients)
admin.site.register(Products)
admin.site.register(FatAcids)
admin.site.register(MineralComposition)
admin.site.register(AminoAcidComposition)
admin.site.register(Chemicals)