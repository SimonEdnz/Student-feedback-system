# Generated by Django 4.2.3 on 2023-08-05 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilityfeedback',
            name='cleanliness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='facilityfeedback',
            name='facility_accessibility',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='facilityfeedback',
            name='facility_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='facilityfeedback',
            name='maintenance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='facilityfeedback',
            name='resource_availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='facilityfeedback',
            name='safety',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='instructorfeedback',
            name='communication',
            field=models.IntegerField(choices=[(5, 'Excellent'), (4, 'Very Good'), (3, 'Good'), (2, 'Fair'), (1, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='instructorfeedback',
            name='knowledge',
            field=models.IntegerField(choices=[(5, 'Excellent'), (4, 'Very Good'), (3, 'Good'), (2, 'Fair'), (1, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='instructorfeedback',
            name='responsiveness',
            field=models.IntegerField(choices=[(5, 'Excellent'), (4, 'Very Good'), (3, 'Good'), (2, 'Fair'), (1, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='instructorfeedback',
            name='teachingStyle',
            field=models.IntegerField(choices=[(5, 'Excellent'), (4, 'Very Good'), (3, 'Good'), (2, 'Fair'), (1, 'Poor')]),
        ),
    ]
