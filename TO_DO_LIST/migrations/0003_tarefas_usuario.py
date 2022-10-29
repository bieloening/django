# Generated by Django 4.1.2 on 2022-10-28 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TO_DO_LIST', '0002_alter_tarefas_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefas',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
