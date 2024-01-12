# Generated by Django 4.1.3 on 2024-01-12 11:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackthonapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_name',
            old_name='service',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('Passport', 'Passport'), ('Transportation', 'Transportation'), ('Citizenship', 'Citizenship'), ('Municipality', 'Municipality')], max_length=100),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must be 10 digits')])),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=200)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackthonapp.service_name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
