# Generated by Django 4.1.3 on 2022-11-21 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0006_subject_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[('azul', 'azul'), ('verde', 'verde'), ('vermelho', 'vermelho'), ('amarelo', 'amarelo')], default='azul', max_length=8),
        ),
    ]
