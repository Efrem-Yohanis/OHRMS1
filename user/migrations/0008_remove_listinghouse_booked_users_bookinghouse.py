# Generated by Django 4.1.3 on 2023-12-17 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_unapproved_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listinghouse',
            name='booked_users',
        ),
        migrations.CreateModel(
            name='BookingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Request_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_booking', to=settings.AUTH_USER_MODEL)),
                ('house_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.listinghouse')),
            ],
        ),
    ]