# Generated by Django 4.2.5 on 2023-10-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie_name', models.CharField(max_length=200)),
                ('hobbie_desc', models.CharField(max_length=200)),
                ('hobbie_image', models.CharField(default='data:image/png;base64,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', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_name', models.CharField(max_length=200)),
                ('port_desc', models.CharField(max_length=200)),
                ('new_name_image', models.CharField(default='https://images.pexels.com/photos/14936128/pexels-photo-14936128.jpeg?cs=srgb&dl=pexels-ann-h-14936128.jpg&fm=jpg', max_length=500)),
            ],
        ),
    ]
