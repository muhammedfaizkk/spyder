# Generated by Django 4.1.7 on 2023-02-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cutomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('customer_phonenumber', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=500)),
                ('customer_password', models.CharField(max_length=150)),
                ('customer_image', models.ImageField(upload_to='customer/')),
            ],
            options={
                'db_table': 'customer_tb',
            },
        ),
    ]
