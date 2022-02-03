# Generated by Django 4.0.2 on 2022-02-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizes',
            name='clot',
        ),
        migrations.RemoveField(
            model_name='quizes',
            name='nausea',
        ),
        migrations.RemoveField(
            model_name='quizes',
            name='sti',
        ),
        migrations.AlterField(
            model_name='quizes',
            name='allergy',
            field=models.CharField(choices=[('sulphur', 'sulphur'), ('copper', 'copper'), ('anesthesia', 'anesthesia')], max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
