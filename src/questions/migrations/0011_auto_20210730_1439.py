# Generated by Django 3.2.5 on 2021-07-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20210730_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesinttype',
            name='question',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='quesmcq',
            name='question',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
