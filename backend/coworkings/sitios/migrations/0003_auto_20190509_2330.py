# Generated by Django 2.2.1 on 2019-05-10 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_auto_20190509_1658'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='sitios',
            name='serviciosP',
        ),
    ]
