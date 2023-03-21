# Generated by Django 4.1.7 on 2023-03-21 14:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_category', models.CharField(max_length=75, verbose_name='Наименование категории')),
                ('Region', models.CharField(choices=[('Иссык-куль', 'Иссык-куль'), ('Чуй', 'Чуй'), ('Ош', 'Ош'), ('Талас', 'Талас'), ('Нарын', 'Нарын')], default='Иссык-куль', max_length=50, verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Наименование ингредиента')),
            ],
            options={
                'verbose_name': ' -- (Нименование ингредиента) -- ',
            },
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Наименование производителя')),
                ('URL', models.ImageField(null=True, upload_to=main.models.get_file_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='Путь картинки')),
                ('Caption', models.CharField(max_length=200, null=True, verbose_name='Название картинки')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_type', models.CharField(max_length=75, verbose_name='Наименование типа')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=75, null=True, verbose_name='Наименование продукта')),
                ('date_analis', models.DateField(null=True, verbose_name='Дата исследования')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.categories')),
                ('manifacturers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.manufacturers')),
                ('types', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.types')),
            ],
            options={
                'verbose_name': ' -- Наименование продукта -- ',
            },
        ),
        migrations.CreateModel(
            name='MineralComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ca', models.FloatField(default=0, verbose_name='Ca (Кальций)')),
                ('Na', models.FloatField(default=0, verbose_name='Na (Натрий)')),
                ('K', models.FloatField(default=0, verbose_name='K (Калий)')),
                ('P', models.FloatField(default=0, verbose_name='P (Фосфор)')),
                ('Mn', models.FloatField(default=0, verbose_name='Mn (Марганец)')),
                ('Zn', models.FloatField(default=0, verbose_name='Zn (Цинк)')),
                ('Se', models.FloatField(default=0, verbose_name='Se (Скандий)')),
                ('Cu', models.FloatField(default=0, verbose_name='Cu (Медь)')),
                ('Fe', models.FloatField(default=0, verbose_name='Fe (Железо)')),
                ('I', models.FloatField(default=0, verbose_name='I (Йод)')),
                ('B', models.FloatField(default=0, verbose_name='B (Бор)')),
                ('Li', models.FloatField(default=0, verbose_name='Li (Литий)')),
                ('Al', models.FloatField(default=0, verbose_name='Al (Алюминий)')),
                ('Mg', models.FloatField(default=0, verbose_name='Mg (Магний)')),
                ('V', models.FloatField(default=0, verbose_name='V (Ванадий)')),
                ('Ni', models.FloatField(default=0, verbose_name='Ni (Нитрий)')),
                ('Co', models.FloatField(default=0, verbose_name='Co (Ковальт)')),
                ('Cr', models.FloatField(default=0, verbose_name='Cr (Хром)')),
                ('Sn', models.FloatField(default=0, verbose_name='Sn (Олово)')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Минеральный состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='FatAcids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_acid', models.CharField(choices=[('Насыщенные жирные кислоты, %', 'Насыщенные жирные кислоты, %'), ('Мононенасыщенные жирные кислоты, %', 'Мононенасыщенные жирные кислоты, %'), ('Полиненасыщенные жирные кислоты, %', 'Полиненасыщенные жирные кислоты, %')], default='Насыщенные жирные кислоты, %', max_length=75, verbose_name='Тип ж-кислоты')),
                ('value', models.FloatField(verbose_name='Содержание')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Виды Жирнокислоты) -- ',
            },
        ),
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluable_solids', models.FloatField(default=0, verbose_name='Массовая доля растворимых сухих веществ, %')),
                ('ascorbic_acids', models.FloatField(default=0, verbose_name='Массовая доля аскорбиновой кислоты, г/дм3')),
                ('ash_content', models.FloatField(default=0, verbose_name='Зольность, %')),
                ('moisture', models.FloatField(default=0, verbose_name='Массовая доля влаги, %')),
                ('protein', models.FloatField(default=0, verbose_name='Массовая доля белка, %')),
                ('fat', models.FloatField(default=0, verbose_name='Массовая доля жира, %')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Химический состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='AminoAcidComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asparing', models.FloatField(default=0, verbose_name='Аспарагиновая кислота')),
                ('glutamin', models.FloatField(default=0, verbose_name='Глутаминовая кислота')),
                ('serin', models.FloatField(default=0, verbose_name='Серин')),
                ('gistidin', models.FloatField(default=0, verbose_name='Гистидин')),
                ('glitsin', models.FloatField(default=0, verbose_name='Глицин')),
                ('treonin', models.FloatField(default=0, verbose_name='Треонин')),
                ('arginin', models.FloatField(default=0, verbose_name='Аргинин')),
                ('alanin', models.FloatField(default=0, verbose_name='Аланин')),
                ('tirosin', models.FloatField(default=0, verbose_name='Тирозин')),
                ('tsistein', models.FloatField(default=0, verbose_name='Цистеин')),
                ('valin', models.FloatField(default=0, verbose_name='Валин')),
                ('metionin', models.FloatField(default=0, verbose_name='Метионин')),
                ('triptofan', models.FloatField(default=0, verbose_name='Триптофан')),
                ('fenilalalin', models.FloatField(default=0, verbose_name='Фенилаланин')),
                ('izoleitsin', models.FloatField(default=0, verbose_name='Изолейцин')),
                ('leitsin', models.FloatField(default=0, verbose_name='Лейцин')),
                ('lisin', models.FloatField(default=0, verbose_name='Лизин')),
                ('prolin', models.FloatField(default=0, verbose_name='Пролин')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Аминокислотный Состав) -- ',
            },
        ),
    ]
