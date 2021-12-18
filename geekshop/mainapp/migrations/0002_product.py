# Generated by Django 3.2.8 on 2021-10-25 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('image', models.ImageField(blank=True, upload_to='products', verbose_name='картинка')),
                ('short_desc', models.CharField(max_length=255, verbose_name='краткое описание')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='цена')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='количество')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='категория')),
            ],
        ),
    ]