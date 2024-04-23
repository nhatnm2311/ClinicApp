# Generated by Django 5.0.4 on 2024-04-23 13:11

import ClinicApp.models
import ckeditor.fields
import cloudinary.models
import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import django_enumfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthdate', models.DateField(default=datetime.date(2024, 1, 1))),
                ('address', models.CharField(default='ABC', max_length=100)),
                ('gender', models.BooleanField(default=True)),
                ('avatar', cloudinary.models.CloudinaryField(default=None, max_length=255, null=True, verbose_name='image')),
                ('role', django_enumfield.db.fields.EnumField(default=2, enum=ClinicApp.models.UserRole)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('symstoms', models.TextField()),
                ('overview', models.TextField(default=None, null=True)),
                ('locked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('amount', models.FloatField()),
                ('unit', django_enumfield.db.fields.EnumField(default=0, enum=ClinicApp.models.Unit)),
                ('period', django_enumfield.db.fields.EnumField(default=0, enum=ClinicApp.models.Period)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_info', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('diploma', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient_info', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='receipt', serialize=False, to='ClinicApp.healthrecord')),
                ('total', models.IntegerField()),
                ('created_date', models.DateField(default=datetime.date(2024, 4, 23))),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('amount', models.FloatField()),
                ('unit', django_enumfield.db.fields.EnumField(default=0, enum=ClinicApp.models.Unit)),
                ('total', models.IntegerField()),
                ('health_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines_detail', to='ClinicApp.healthrecord')),
                ('instructions', models.ManyToManyField(related_name='medicine', to='ClinicApp.instruction')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClinicApp.medicine')),
            ],
            options={
                'unique_together': {('health_record', 'medicine')},
            },
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='medicines',
            field=models.ManyToManyField(related_name='records', through='ClinicApp.MedicineDetails', to='ClinicApp.medicine'),
        ),
        migrations.CreateModel(
            name='MedicinePrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('unit', django_enumfield.db.fields.EnumField(default=2, enum=ClinicApp.models.Unit)),
                ('unit_price', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='ClinicApp.medicine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='services',
            field=models.ManyToManyField(related_name='records', to='ClinicApp.service'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medicines', to='ClinicApp.vendor'),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('employee_info', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor_info', serialize=False, to='ClinicApp.employee')),
                ('departments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='ClinicApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('employee_info', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='nurse_info', serialize=False, to='ClinicApp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_records', to='ClinicApp.patient'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ExpectedDate', models.DateTimeField(default=datetime.datetime(2024, 4, 23, 13, 11, 43, 71856))),
                ('confirmed', models.BooleanField(default=False)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='ClinicApp.department')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='ClinicApp.patient')),
            ],
            options={
                'unique_together': {('patient', 'ExpectedDate')},
            },
        ),
        migrations.CreateModel(
            name='ReceiptDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='ClinicApp.receipt')),
            ],
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_records', to='ClinicApp.doctor'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipt_confirmed', to='ClinicApp.nurse'),
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='confirmation', serialize=False, to='ClinicApp.appointment')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('nurse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment_confirmed', to='ClinicApp.nurse')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ScheduleDate', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='ClinicApp.department')),
                ('employees', models.ManyToManyField(related_name='schedules', to='ClinicApp.employee')),
            ],
            options={
                'unique_together': {('ScheduleDate', 'department')},
            },
        ),
    ]
