# Generated by Django 2.2.12 on 2022-04-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220418_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shape',
            field=models.CharField(choices=[('ROUND', 'Round'), ('BOTTOM', 'Bottom'), ('SQUARE', 'Square')], default='', max_length=8, null=True),
        ),
    ]
