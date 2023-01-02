# Generated by Django 4.1.3 on 2022-12-06 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studies', '0011_alter_study_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_subject', to=settings.AUTH_USER_MODEL),  # noqa: E501
        ),
    ]