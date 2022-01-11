# Generated by Django 4.0 on 2022-01-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images')),
                ('contact', models.CharField(max_length=15)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='seller',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
