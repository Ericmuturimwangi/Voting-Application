# Generated by Django 5.0.6 on 2024-07-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quetion_text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Default Question Text', max_length=300),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='Choice Text'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Vote Count'),
        ),
    ]
