

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=True)),
                ('profile_photo', models.ImageField(upload_to='media_/profile_pic/')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email_id', models.CharField(max_length=250)),
                ('mobile_no', models.BigIntegerField()),
                ('speciality', models.CharField(choices=[('ORTHOPAEDIC', 'ORTHOPAEDIC'), ('GYNACEOLOGIST', 'GYNACEOLOGIST'), ('ONCOLOGIST', 'ONCOLOGIST'), ('NEUROLOGIST', 'NEUROLOGIST')], max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('locality', models.CharField(max_length=250)),
                ('hospital', models.CharField(max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(blank=True, choices=[('09:00:00', '9 am'), ('12:00:00', '12 pm'), ('16:00:00', '4 pm')], max_length=200, null=True)),
                ('slot_status', models.BooleanField(default=False)),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.BookingDate')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='bookingdate',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='slot',
            unique_together={('doctor', 'start_time', 'date')},
        ),
    ]
