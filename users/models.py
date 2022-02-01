# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_admin_geomap import GeoItem


class AdminApplications(models.Model):
    application = models.ForeignKey('Applications', models.DO_NOTHING)
    administration = models.ForeignKey('ExecutiveAuthority', models.DO_NOTHING)
    task_type = models.IntegerField()
    explanation = models.CharField(max_length=255, blank=True, null=True)
    estimated_date_work = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    media_data = models.TextField(db_collation='utf8mb4_bin')
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_applications'


class ApplicationStatus(models.Model):
    title = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'application_status'

    def __str__(self):
        return self.title

class Applications(models.Model, GeoItem):
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='user')
    redirect_to_application = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.ForeignKey(ApplicationStatus, models.DO_NOTHING, blank=True, null=True)
    media_data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    applicants_details = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
    is_moderate = models.IntegerField()
    moderator = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True, related_name='moderator')
    problem_desc = models.CharField(max_length=255, blank=True, null=True)
    base_rate = models.IntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    views_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        db_table = 'applications'
        ordering = ("status", 'user')


    def __str__(self):
        return f"{self.status} - {self.status.title}"


    @property
    def geomap_longitude(self):
        return str(self.longitude)


    @property
    def geomap_latitude(self):
        return str(self.latitude)


    @property
    def geomap_icon(self):
        return self.default_icon

          
    # @property
    # def geomap_popup_view(self):
    #     return "<strong>{}</strong>".format(str(str(application_status[int(self.status.title)-1][1])))


    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view




     

class ApplicationsCategories(models.Model):
    application = models.ForeignKey(Applications, models.DO_NOTHING)
    category = models.ForeignKey('ProblemCategories', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'applications_categories'


class ContractorsProblems(models.Model):
    problem = models.ForeignKey('ProblemCategories', models.DO_NOTHING)
    contractor = models.ForeignKey('ExecutiveAuthority', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contractors_problems'


class ExecutiveAuthority(models.Model):
    title = models.CharField(max_length=255)
    mnemomic_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    hash_tag = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    contact_email_administration = models.CharField(max_length=255, blank=True, null=True)
    tg_id = models.CharField(max_length=255, blank=True, null=True)
    web_site_link = models.CharField(max_length=255, blank=True, null=True)
    additional_information = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20)
    work_schedule = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    is_email_alert = models.IntegerField()
    is_sms_alert = models.IntegerField()
    is_generate_daily_report = models.IntegerField()
    is_visible = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'executive_authority'
        unique_together = (('title', 'hash_tag', 'tg_id'),)


class MailingQueue(models.Model):
    mailing_address = models.CharField(max_length=30)
    mailing_type = models.IntegerField()
    status = models.IntegerField()
    template_name = models.CharField(max_length=30, blank=True, null=True)
    template_object = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    application = models.ForeignKey(Applications, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_queue'


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField()
    author_name = models.CharField(max_length=30)
    type = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    life_time = models.DateTimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    admin = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    is_visible = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)
    stories_type = models.IntegerField()
    views_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class ProblemCategories(models.Model):
    title = models.CharField(max_length=100)
    mnemonic_name = models.CharField(max_length=100)
    hash_tag = models.CharField(max_length=100)
    icon_file_path = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_visible = models.IntegerField()
    priority = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem_categories'
        unique_together = (('title', 'hash_tag'),)


class Regions(models.Model):
    title = models.CharField(max_length=255)
    is_available = models.SmallIntegerField()
    position = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class Roles(models.Model):
    title = models.CharField(max_length=50)
    mnemomic_name = models.CharField(max_length=50, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class SavedCoord(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    latitude = models.FloatField()
    longitude = models.IntegerField()
    explanation = models.CharField(max_length=255, blank=True, null=True)
    media_data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_coord'


class TokenBlocklist(models.Model):
    jti = models.CharField(max_length=36)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'token_blocklist'


class UserProfiles(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_email_alert = models.IntegerField()
    is_sms_alert = models.IntegerField()
    is_anonym = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_profiles'


class Users(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    sms_code = models.CharField(max_length=4, blank=True, null=True)
    email_code = models.CharField(max_length=255, blank=True, null=True)
    phone_confirm_date = models.DateTimeField(blank=True, null=True)
    email_confirm_date = models.DateTimeField(blank=True, null=True)
    ban_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    is_stuff = models.IntegerField()
    delete_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('login', 'email_code'),)
