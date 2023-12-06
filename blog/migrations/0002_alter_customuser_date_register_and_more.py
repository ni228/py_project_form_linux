# Generated by Django 4.2.7 on 2023-11-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_register',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
