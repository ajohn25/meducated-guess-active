# Generated by Django 3.1.5 on 2021-03-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_auto_20210329_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='prev_answer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]