# Generated by Django 3.1.1 on 2020-12-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mLogin', '0003_auto_20201226_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
