# Generated by Django 4.2 on 2023-04-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='selection',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
