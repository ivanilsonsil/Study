# Generated by Django 4.1.3 on 2022-12-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0013_alter_subject_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[('blue', 'azul'), ('orange', 'Laranja'), ('red', 'vermelho'), ('pink', 'Rosa'), ('purple', 'Roxo'), ('green', 'verde'), ('yellow', 'amarelo')], default='azul', max_length=8),
        ),
    ]
