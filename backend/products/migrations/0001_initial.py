# Generated by Django 4.2.2 on 2023-07-06 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=255)),
                ('product_image', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('parent_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('value', models.CharField(max_length=50)),
                ('variation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.variation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('sku', models.CharField(blank=True, max_length=255, null=True, verbose_name='SKU')),
                ('qty_in_stock', models.PositiveIntegerField()),
                ('img', models.URLField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('variations', models.ManyToManyField(blank=True, to='products.variationoption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
    ]
