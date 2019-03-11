# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CityArrests(models.Model):
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    violent_crime_total = models.TextField(db_column='Violent Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter = models.TextField(db_column='Murder and Nonnegligent Manslaughter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape = models.TextField(db_column='Rape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    robbery = models.TextField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggravated_assault = models.TextField(db_column='Aggravated Assault', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_total = models.TextField(db_column='Property Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary = models.TextField(db_column='Burglary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    larceny_theft = models.TextField(db_column='Larceny-Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vehicle_theft = models.TextField(db_column='Motor Vehicle Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bjs_city'


class StateArrests(models.Model):
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    population = models.TextField(db_column='Population', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    violent_crime_total = models.TextField(db_column='Violent Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter = models.TextField(db_column='Murder and Nonnegligent Manslaughter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape = models.TextField(db_column='Rape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    robbery = models.TextField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggravated_assault = models.TextField(db_column='Aggravated Assault', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_total = models.TextField(db_column='Property Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary = models.TextField(db_column='Burglary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    larceny_theft = models.TextField(db_column='Larceny-Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vehicle_theft = models.TextField(db_column='Motor Vehicle Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bjs_national'


class ChiCrime2018(models.Model):
    id_c = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    case_number = models.TextField(db_column='Case Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    block = models.TextField(db_column='Block', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iucr = models.TextField(db_column='IUCR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    primary_type = models.TextField(db_column='Primary Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location_description = models.TextField(db_column='Location Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    arrest = models.TextField(db_column='Arrest', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    domestic = models.TextField(db_column='Domestic', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    beat = models.TextField(db_column='Beat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    district = models.TextField(db_column='District', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ward = models.TextField(db_column='Ward', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    community_area = models.TextField(db_column='Community Area', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    fbi_code = models.TextField(db_column='FBI Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    x_coordinate = models.TextField(db_column='X Coordinate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    y_coordinate = models.TextField(db_column='Y Coordinate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    updated_on = models.TextField(db_column='Updated On', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chi_crime_2018'


class ChiWeather2015(models.Model):
    station_name = models.TextField(db_column='Station Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    measurement_timestamp = models.TextField(db_column='Measurement Timestamp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    air_temperature = models.TextField(db_column='Air Temperature', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wet_bulb_temperature = models.TextField(db_column='Wet Bulb Temperature', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    humidity = models.TextField(db_column='Humidity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rain_intensity = models.TextField(db_column='Rain Intensity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    interval_rain = models.TextField(db_column='Interval Rain', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    total_rain = models.TextField(db_column='Total Rain', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    precipitation_type = models.TextField(db_column='Precipitation Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wind_direction = models.TextField(db_column='Wind Direction', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wind_speed = models.TextField(db_column='Wind Speed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    maximum_wind_speed = models.TextField(db_column='Maximum Wind Speed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    barometric_pressure = models.TextField(db_column='Barometric Pressure', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    solar_radiation = models.TextField(db_column='Solar Radiation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    heading = models.TextField(db_column='Heading', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_life = models.TextField(db_column='Battery Life', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    measurement_timestamp_label = models.TextField(db_column='Measurement Timestamp Label', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    measurement_id = models.TextField(db_column='Measurement ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chi_weather_2015'


class CityCrimes(models.Model):
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    population = models.TextField(db_column='Population', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    violent_crime_total = models.TextField(db_column='Violent Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter = models.TextField(db_column='Murder and Nonnegligent Manslaughter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape = models.TextField(db_column='Rape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    robbery = models.TextField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggravated_assault = models.TextField(db_column='Aggravated Assault', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_total = models.TextField(db_column='Property Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary = models.TextField(db_column='Burglary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    larceny_theft = models.TextField(db_column='Larceny-Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vehicle_theft = models.TextField(db_column='Motor Vehicle Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    violent_crime_rate = models.TextField(db_column='Violent Crime Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter_rate = models.TextField(db_column='Murder and Nonnegligent Manslaughter Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape_rate = models.TextField(db_column='Rape Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    robbery_rate = models.TextField(db_column='Robbery Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    aggravated_assault_rate = models.TextField(db_column='Aggravated Assault Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_rate = models.TextField(db_column='Property Crime Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary_rate = models.TextField(db_column='Burglary Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    larceny_theft_rate = models.TextField(db_column='Larceny-Theft Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vechicle_theft_rate = models.TextField(db_column='Motor Vechicle Theft Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cities_data'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NationalArrests(models.Model):
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coverage_indicator = models.TextField(db_column='Coverage Indicator', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    total_arrests = models.TextField(db_column='Total Arrests', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    violent_crime_index = models.TextField(db_column='Violent Crime Index', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_nonneg_mans_field = models.TextField(db_column='Murder/nonneg. mans.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    rape = models.TextField(db_column='Rape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    robbery = models.TextField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggravated_assault = models.TextField(db_column='Aggravated assault', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_index = models.TextField(db_column='Property Crime Index', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary = models.TextField(db_column='Burglary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    larceny_theft = models.TextField(db_column='Larceny-theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vehicle_theft = models.TextField(db_column='Motor vehicle theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    arson = models.TextField(db_column='Arson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_assaults = models.TextField(db_column='Other assaults', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    forgery_and_counterfeiting = models.TextField(db_column='Forgery and counterfeiting', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    fraud = models.TextField(db_column='Fraud', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    embezzlement = models.TextField(db_column='Embezzlement', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stolen_property = models.TextField(db_column='Stolen property', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    vandalism = models.TextField(db_column='Vandalism', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weapons = models.TextField(db_column='Weapons', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prostitution_commercialized_vice = models.TextField(db_column='Prostitution/commercialized vice', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    sex_offenses_other_field = models.TextField(db_column='Sex offenses (other)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    drug_abuse_violations = models.TextField(db_column='Drug abuse violations', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    gambling = models.TextField(db_column='Gambling', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offenses_against_family = models.TextField(db_column='Offenses against family', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    driving_under_influence = models.TextField(db_column='Driving under influence', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    liquor_laws = models.TextField(db_column='Liquor laws', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    drunkenness = models.TextField(db_column='Drunkenness', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disorderly_conduct = models.TextField(db_column='Disorderly conduct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    vagrancy = models.TextField(db_column='Vagrancy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    all_other_offenses = models.TextField(db_column='All other offenses', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    curfew_and_loitering = models.TextField(db_column='Curfew and loitering', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    runaways = models.TextField(db_column='Runaways', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_population = models.TextField(db_column='Total Population', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'national_arrests'


class StateCrimes(models.Model):
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    population = models.TextField(db_column='Population', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    violent_crime_total = models.TextField(db_column='Violent Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter = models.TextField(db_column='Murder and Nonnegligent Manslaughter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape = models.TextField(db_column='Rape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    robbery = models.TextField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggravated_assault = models.TextField(db_column='Aggravated Assault', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_total = models.TextField(db_column='Property Crime Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary = models.TextField(db_column='Burglary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    larceny_theft = models.TextField(db_column='Larceny-Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vehicle_theft = models.TextField(db_column='Motor Vehicle Theft', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    violent_crime_rate = models.TextField(db_column='Violent Crime Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    murder_and_nonnegligent_manslaughter_rate = models.TextField(db_column='Murder and Nonnegligent Manslaughter Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rape_rate = models.TextField(db_column='Rape Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    robbery_rate = models.TextField(db_column='Robbery Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    aggravated_assault_rate = models.TextField(db_column='Aggravated Assault Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    property_crime_rate = models.TextField(db_column='Property Crime Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    burglary_rate = models.TextField(db_column='Burglary Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    larceny_theft_rate = models.TextField(db_column='Larceny-Theft Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    motor_vechicle_theft_rate = models.TextField(db_column='Motor Vechicle Theft Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'states_data'
