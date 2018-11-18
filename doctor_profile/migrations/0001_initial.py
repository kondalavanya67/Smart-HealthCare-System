
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=200)),
                ('profile_photo', models.ImageField(upload_to='media_/profile_pic/')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),

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
    ]
