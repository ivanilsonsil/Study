# Generated by Django 4.1.3 on 2022-12-08 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0019_content_subject_alter_content_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_list', to='studies.subject'),
        ),
    ]
