# Generated by Django 4.0.4 on 2022-04-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindepaginas', '0005_soal_ideh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soal',
            name='idEH',
        ),
        migrations.AddField(
            model_name='jawabanpeserta',
            name='idEH',
            field=models.CharField(default='', max_length=50),
        ),
    ]
