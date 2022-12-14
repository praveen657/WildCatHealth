# Generated by Django 4.1.2 on 2022-12-07 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('appointment_time', models.CharField(blank=True, max_length=10, null=True)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('deptname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('diagresult', models.CharField(blank=True, max_length=50, null=True)),
                ('diagname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('designation', models.CharField(blank=True, max_length=10, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('deptid', models.CharField(blank=True, max_length=4, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('dateofjoin', models.DateField(blank=True, null=True)),
                ('ssn', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('hospitalname', models.CharField(max_length=50)),
                ('streetname', models.CharField(blank=True, max_length=50, null=True)),
                ('areaname', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('recordid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('recorddate', models.DateField(blank=True, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=100, null=True)),
                ('knowndisease', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'medical_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NonMedicalStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worktype', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'non_medical_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('phoneno', models.IntegerField(blank=True, null=True)),
                ('streetname', models.CharField(blank=True, max_length=10, null=True)),
                ('areaname', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PATIENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientBill',
            fields=[
                ('pbid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pbstatus', models.CharField(blank=True, max_length=20, null=True)),
                ('billdate', models.DateTimeField(blank=True, null=True)),
                ('pbamount', models.IntegerField(blank=True, null=True)),
                ('transactiontype', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'patient_bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppointmentSuggestDiagnosis',
            fields=[
                ('appid', models.OneToOneField(db_column='appid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.appointment')),
            ],
            options={
                'db_table': 'appointment_suggest_diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppointmentsWithMedicalstaff',
            fields=[
                ('appid', models.OneToOneField(db_column='appid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.appointment')),
            ],
            options={
                'db_table': 'appointments_with_medicalstaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicalstaff',
            fields=[
                ('employeeid', models.OneToOneField(db_column='employeeid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.employee')),
                ('specialization', models.CharField(blank=True, max_length=50, null=True)),
                ('meetinglink', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'medicalstaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfflineAppointment',
            fields=[
                ('appid', models.OneToOneField(db_column='appid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.appointment')),
                ('cabinno', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'offline_appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OnlineAppointment',
            fields=[
                ('appid', models.OneToOneField(db_column='appid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.appointment')),
                ('meetinglink', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'online_appointment',
                'managed': False,
            },
        ),
    ]
