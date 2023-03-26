from django.db import models
from PIL import Image
from django.utils import timezone
from django.core.validators import validate_image_file_extension
import uuid, os


# Функция для кодировки название файла
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace(filename,'_f')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join(instance.path_url, filename)

# Регионы
class RegionChoice(models.TextChoices):
    REGION_1 = "Чуйская область", "Чуйская область"
    REGION_2 = "Иссык-кульская область", "Иссык-кульская область"
    REGION_3 = "Ошская область", "Ошская область"
    REGION_4 = "Таласская область", "Таласская область"
    REGION_5 = "Нарынская область", "Нарынская область"
    REGION_6 = "Джалал-Абадская область", "Джалал-Абадская область"
    REGION_7 = "Баткенская область", "Баткенская область"

# Категории продуктов (Мясные, Молочные, Хлебобулочные и т.д.)
class Categories(models.Model):
    Name_of_category = models.CharField(verbose_name='Наименование категории', max_length=75,help_text='(Мясные, Молочные, Хлебобулочные и т.д.)')
    Region = models.CharField(
        max_length = 50,
        choices = RegionChoice.choices,
        default = RegionChoice.REGION_1,
        verbose_name = "Регион"
    )
    class Meta:
        verbose_name = "Категория"
        
        
    def __str__(self):
        return  f"{self.Name_of_category}-{self.Region}"
    
# Тип продуктов (Говядина, Баранина и т.д.)
class Types(models.Model):
    Name_of_type = models.CharField(verbose_name='Наименование типа', max_length=75, help_text='(Мясные, Молочные, Хлебобулочные и т.д.)', null=True)
    Category = models.ForeignKey(Categories, on_delete=models.RESTRICT, null=True)

    
    class Meta:
        verbose_name = "Тип продуктов"
    def __str__(self) -> str:
        return f"{self.Name_of_type} - {self.Category}"
    
# Названия жирно-кислотного состава
class FatAcidsTypeChoice(models.TextChoices):
    TYPE_1 = "Насыщенные жирные кислоты, %", "Насыщенные жирные кислоты, %"
    TYPE_2 = "Мононенасыщенные жирные кислоты, %", "Мононенасыщенные жирные кислоты, %"
    TYPE_3 = "Полиненасыщенные жирные кислоты, %", "Полиненасыщенные жирные кислоты, %"


class IngredientsCategory(models.Model):
    name = models.CharField(verbose_name='Наименование Категории', max_length=40)
    
    class Meta:
        verbose_name = ' -- (Категории ингредиента) -- '
        
    def __str__(self) -> str:
        return self.name
# Ингредиенты
class Ingredients(models.Model):
    name = models.CharField(verbose_name='Наименование ингредиента', max_length=40)
    category = models.ForeignKey(IngredientsCategory, on_delete=models.RESTRICT, verbose_name='Категория', blank=True, null=True)
    
    class Meta:
        verbose_name = ' -- (Наименование ингредиента) -- '
    def __str__(self) -> str:
        return self.name
    
# Аминокислотный состав
class AminoAcidCompOfIng(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.RESTRICT, null=True)
    isolate = models.FloatField(verbose_name='Изолейц', default=0)
    leitz = models.FloatField(verbose_name='Лейцин', default=0)
    valin = models.FloatField(verbose_name='Валин', default=0)
    methylcysteine = models.FloatField(verbose_name='Метилцистеин', default=0)
    fentir = models.FloatField(verbose_name='Фен+Тир', default=0)
    triptophan = models.FloatField(verbose_name='Триптофан', default=0)
    lisin = models.FloatField(verbose_name='Лизин', default=0)
    treon = models.FloatField(verbose_name='Треон', default=0)

    class Meta:
        verbose_name = ' -- (Аминокислотный Состав Ингредиента) -- '
    def __str__(self) -> str:
        return self.ingredient
    
# Жирнокислотный состав Ингредиента
class FatAcidsIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.RESTRICT)
    type_of_acid = models.CharField(
        max_length=75,
        choices = FatAcidsTypeChoice.choices,
                  default = FatAcidsTypeChoice.TYPE_1,
                  verbose_name = "Тип ж-кислоты"
                  )
    value = models.FloatField(verbose_name='Содержание') 
    
    class Meta:
        verbose_name = ' -- (Виды Жирнокислоты) -- '
    def __str__(self) -> str:
        return self.ingredient
    
# Химический состав Ингредиента
class ChemicalsIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.RESTRICT, null=True)
    soluable_solids = models.FloatField(verbose_name='Массовая доля растворимых сухих веществ, %', default=0)
    ascorbic_acids = models.FloatField(verbose_name='Массовая доля аскорбиновой кислоты, г/дм3', default=0)
    ash_content = models.FloatField(verbose_name='Зольность, %', default=0)
    moisture = models.FloatField(verbose_name='Массовая доля влаги, %', default=0)
    protein = models.FloatField(verbose_name='Массовая доля белка, %', default=0)
    fat = models.FloatField(verbose_name='Массовая доля жира, %', default=0)

    class Meta:
        verbose_name = ' -- (Химический состав) -- '


# Минеральный состав
class MineralsIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.RESTRICT, null=True)
    Ca = models.FloatField(verbose_name='Ca (Кальций)', default=0)
    Na = models.FloatField(verbose_name='Na (Натрий)', default=0)
    K = models.FloatField(verbose_name='K (Калий)', default=0)
    P = models.FloatField(verbose_name='P (Фосфор)', default=0)
    Mn = models.FloatField(verbose_name='Mn (Марганец)', default=0)
    Zn = models.FloatField(verbose_name='Zn (Цинк)', default=0)
    Se = models.FloatField(verbose_name='Se (Скандий)', default=0)
    Cu = models.FloatField(verbose_name='Cu (Медь)', default=0)
    Fe = models.FloatField(verbose_name='Fe (Железо)', default=0)
    I = models.FloatField(verbose_name='I (Йод)', default=0)
    B = models.FloatField(verbose_name='B (Бор)', default=0)
    Li = models.FloatField(verbose_name='Li (Литий)', default=0)
    Al = models.FloatField(verbose_name='Al (Алюминий)', default=0)
    Mg = models.FloatField(verbose_name='Mg (Магний)', default=0)
    V = models.FloatField(verbose_name='V (Ванадий)', default=0)
    Ni = models.FloatField(verbose_name='Ni (Нитрий)', default=0)
    Co = models.FloatField(verbose_name='Co (Ковальт)', default=0)
    Cr = models.FloatField(verbose_name='Cr (Хром)', default=0)
    Sn = models.FloatField(verbose_name='Sn (Олово)', default=0)
    
    class Meta:
        verbose_name = ' -- (Минеральный состав) -- '
    
    def __str__(self) -> str:
        return self.ingredient
    

    
        
# Продукты
class Products(models.Model):
    attribute_name = models.CharField(verbose_name='Наименование продукта', max_length=75)
    types = models.ForeignKey(Types, on_delete=models.RESTRICT, verbose_name='Тип продукта')
    date_analis = models.DateField(verbose_name='Дата исследования', default=timezone.now)

    class Meta:
        verbose_name = ' -- Наименование продукта -- '
    def __str__(self) -> str:
        return self.attribute_name
    
# Жирнокислотный состав
class FatAcids(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT)
    type_of_acid = models.CharField(
        max_length=75,
        choices = FatAcidsTypeChoice.choices,
                  default = FatAcidsTypeChoice.TYPE_1,
                  verbose_name = "Тип ж-кислоты"
                  )
    value = models.FloatField(verbose_name='Содержание') 
    
    class Meta:
        verbose_name = ' -- (Виды Жирнокислоты) -- '
    def __str__(self) -> str:
        return self.name
    
# Минеральный состав
class MineralComposition(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT, null=True)
    Ca = models.FloatField(verbose_name='Ca (Кальций)', default=0)
    Na = models.FloatField(verbose_name='Na (Натрий)', default=0)
    K = models.FloatField(verbose_name='K (Калий)', default=0)
    P = models.FloatField(verbose_name='P (Фосфор)', default=0)
    Mn = models.FloatField(verbose_name='Mn (Марганец)', default=0)
    Zn = models.FloatField(verbose_name='Zn (Цинк)', default=0)
    Se = models.FloatField(verbose_name='Se (Скандий)', default=0)
    Cu = models.FloatField(verbose_name='Cu (Медь)', default=0)
    Fe = models.FloatField(verbose_name='Fe (Железо)', default=0)
    I = models.FloatField(verbose_name='I (Йод)', default=0)
    B = models.FloatField(verbose_name='B (Бор)', default=0)
    Li = models.FloatField(verbose_name='Li (Литий)', default=0)
    Al = models.FloatField(verbose_name='Al (Алюминий)', default=0)
    Mg = models.FloatField(verbose_name='Mg (Магний)', default=0)
    V = models.FloatField(verbose_name='V (Ванадий)', default=0)
    Ni = models.FloatField(verbose_name='Ni (Нитрий)', default=0)
    Co = models.FloatField(verbose_name='Co (Ковальт)', default=0)
    Cr = models.FloatField(verbose_name='Cr (Хром)', default=0)
    Sn = models.FloatField(verbose_name='Sn (Олово)', default=0)
    
    class Meta:
        verbose_name = ' -- (Минеральный состав) -- '
    
    def __str__(self) -> str:
        return self.product
    
# Аминокислотный состав
class AminoAcidComposition(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT, null=True)
    asparing = models.FloatField(verbose_name='Аспарагиновая кислота', default=0)
    glutamin = models.FloatField(verbose_name='Глутаминовая кислота', default=0)
    serin = models.FloatField(verbose_name='Серин', default=0)
    gistidin = models.FloatField(verbose_name='Гистидин', default=0)
    glitsin = models.FloatField(verbose_name='Глицин', default=0)
    treonin = models.FloatField(verbose_name='Треонин', default=0)
    arginin = models.FloatField(verbose_name='Аргинин', default=0)
    alanin = models.FloatField(verbose_name='Аланин', default=0)
    tirosin = models.FloatField(verbose_name='Тирозин', default=0)
    tsistein = models.FloatField(verbose_name='Цистеин', default=0)
    valin = models.FloatField(verbose_name='Валин', default=0)
    metionin = models.FloatField(verbose_name='Метионин', default=0)
    triptofan = models.FloatField(verbose_name='Триптофан', default=0)
    fenilalalin = models.FloatField(verbose_name='Фенилаланин', default=0)
    izoleitsin = models.FloatField(verbose_name='Изолейцин', default=0)
    leitsin = models.FloatField(verbose_name='Лейцин', default=0)
    lisin = models.FloatField(verbose_name='Лизин', default=0)
    prolin = models.FloatField(verbose_name='Пролин', default=0)

    class Meta:
        verbose_name = ' -- (Аминокислотный Состав) -- '
    def __str__(self) -> str:
        return self.product
    
# Химический состав 
class Chemicals(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT, null=True)
    soluable_solids = models.FloatField(verbose_name='Массовая доля растворимых сухих веществ, %', default=0)
    ascorbic_acids = models.FloatField(verbose_name='Массовая доля аскорбиновой кислоты, г/дм3', default=0)
    ash_content = models.FloatField(verbose_name='Зольность, %', default=0)
    moisture = models.FloatField(verbose_name='Массовая доля влаги, %', default=0)
    protein = models.FloatField(verbose_name='Массовая доля белка, %', default=0)
    fat = models.FloatField(verbose_name='Массовая доля жира, %', default=0)

    class Meta:
        verbose_name = ' -- (Химический состав) -- '




