# Generated by Django 4.0.3 on 2022-04-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindepaginas', '0004_jawabanpeserta_score1_jawabanpeserta_score2'),
    ]

    operations = [
        migrations.AddField(
            model_name='soal',
            name='idEH',
            field=models.CharField(default='', max_length=50),
        ),
    ]
