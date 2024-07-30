# Generated by Django 4.2.13 on 2024-07-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_image',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
        migrations.AddField(
            model_name='company',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('month', 'Monthly'), ('quarter', 'Quarterly'), ('half', 'Half Yearly')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='quarterly_price',
            field=models.IntegerField(default=100),
        ),
    ]
