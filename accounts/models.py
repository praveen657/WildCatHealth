# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Patient(models.Model):
    patientid = models.CharField(primary_key=True, max_length=4)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    phoneno = models.IntegerField(blank=True, null=True)
    streetname = models.CharField(max_length=10, blank=True, null=True)
    areaname = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'PATIENT'

class Department(models.Model):
    deptid = models.CharField(primary_key=True, max_length=4)
    deptname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department'


class Employee(models.Model):
    employeeid = models.CharField(primary_key=True, max_length=4)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    deptid = models.CharField(max_length=4, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    dateofjoin = models.DateField(blank=True, null=True)
    ssn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'

class Appointment(models.Model):
    appid = models.CharField(primary_key=True, max_length=4)
    hospitalid = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='hospitalid', blank=True, null=True)
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientid', blank=True, null=True)
    appointment_time = models.CharField(max_length=10, blank=True, null=True)
    appointment_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class AppointmentSuggestDiagnosis(models.Model):
    appid = models.OneToOneField(Appointment, models.DO_NOTHING, db_column='appid', primary_key=True)
    diagid = models.ForeignKey('Diagnosis', models.DO_NOTHING, db_column='diagid')

    class Meta:
        managed = False
        db_table = 'appointment_suggest_diagnosis'
        unique_together = (('appid', 'diagid'),)


class AppointmentsWithMedicalstaff(models.Model):
    appid = models.OneToOneField(Appointment, models.DO_NOTHING, db_column='appid', primary_key=True)
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeid')

    class Meta:
        managed = False
        db_table = 'appointments_with_medicalstaff'
        unique_together = (('appid', 'employeeid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)




class Diagnosis(models.Model):
    diagid = models.CharField(primary_key=True, max_length=4)
    diagresult = models.CharField(max_length=50, blank=True, null=True)
    diagname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


       
class Hospital(models.Model):
    hospitalid = models.CharField(primary_key=True, max_length=4)
    hospitalname = models.CharField(max_length=50)
    streetname = models.CharField(max_length=50, blank=True, null=True)
    areaname = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital'





class MedicalRecord(models.Model):
    recordid = models.CharField(primary_key=True, max_length=4)
    recorddate = models.DateField(blank=True, null=True)
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    knowndisease = models.CharField(max_length=100, blank=True, null=True)
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_record'


class Medicalstaff(models.Model):
    employeeid = models.OneToOneField(Employee, models.DO_NOTHING, db_column='employeeid', primary_key=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    meetinglink = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicalstaff'





class NonMedicalStaff(models.Model):
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    worktype = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_medical_staff'


class OfflineAppointment(models.Model):
    appid = models.OneToOneField(Appointment, models.DO_NOTHING, db_column='appid', primary_key=True)
    cabinno = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offline_appointment'


class OnlineAppointment(models.Model):
    appid = models.OneToOneField(Appointment, models.DO_NOTHING, db_column='appid', primary_key=True)
    meetinglink = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_appointment'


class PatientBill(models.Model):
    pbid = models.CharField(primary_key=True, max_length=4)
    pbstatus = models.CharField(max_length=20, blank=True, null=True)
    billdate = models.DateTimeField(blank=True, null=True)
    pbamount = models.IntegerField(blank=True, null=True)
    transactiontype = models.CharField(max_length=20, blank=True, null=True)
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_bill'


