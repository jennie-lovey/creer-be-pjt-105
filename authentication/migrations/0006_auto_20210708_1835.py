# Generated by Django 3.2.5 on 2021-07-08 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_auth_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
