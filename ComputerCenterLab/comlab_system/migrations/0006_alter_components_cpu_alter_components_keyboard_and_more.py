# Generated by Django 5.0.3 on 2024-09-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comlab_system', '0005_alter_unit_component'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='cpu',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='components',
            name='keyboard',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='components',
            name='monitor',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='components',
            name='motherboard',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='components',
            name='mouse',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='components',
            name='ram',
            field=models.CharField(default='No', max_length=50),
        ),
    ]
