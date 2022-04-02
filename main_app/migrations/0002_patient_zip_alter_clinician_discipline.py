# Generated by Django 4.0.3 on 2022-04-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='zip',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clinician',
            name='discipline',
            field=models.CharField(choices=[('PT', 'Physical Therapist'), ('OT', 'Occupational Therapist'), ('ST', 'Speech Therapist')], max_length=20),
        ),
    ]