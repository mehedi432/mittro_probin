# Generated by Django 3.2.6 on 2021-09-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_person_child_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_place',
            field=models.CharField(blank=True, default='এখন ও যুক্ত করা হয় নাই', max_length=89, null=True),
        ),
    ]