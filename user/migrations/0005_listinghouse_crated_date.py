# Generated by Django 4.1.3 on 2023-12-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_listinghouse_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='listinghouse',
            name='crated_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]