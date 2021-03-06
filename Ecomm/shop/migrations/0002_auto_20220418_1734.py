# Generated by Django 2.2.12 on 2022-04-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shape',
            field=models.CharField(choices=[('CIRCLE', 'Circle'), ('TRIANGLE', 'Triangle'), ('SQUARE', 'Square')], default='', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('Extra Small', 'XS'), ('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Extra Large', 'XL'), ('Double Large', 'XXL'), ('Triple Large', 'XXXL')], max_length=120, null=True),
        ),
    ]
