from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
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
    media_data = models.JSONField()
    create_date = models.DateField()
    update_date = models.IntegerField()

    class Meta:
        db_table = 'admin_applications'



application_status = [
    (1, 'В обработке'),
    (2, 'В рассмотрении'),
    (3, 'Исполнение'),
    (4, 'Проверка исполнения'),
    (5, 'Выполнено'),
    (6, 'Архивная'),
]


class ApplicationStatus(models.Model):
    title = models.CharField(unique=True, max_length=20, choices=application_status)
    def __str__(self):
        return str(application_status[int(self.title)-1][1])

    def get_full_name(self):
        return self.title


    def get_short_name(self):
        return self.title
    

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
        db_table = 'application_status'


class Applications(models.Model, GeoItem):
    user = models.ForeignKey('User', models.DO_NOTHING,related_name='user')
    moderator = models.ForeignKey('User', models.DO_NOTHING,related_name='moderator', blank=True, null=True)
    redirect_to_application_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.ForeignKey(ApplicationStatus, models.DO_NOTHING, blank=True, null=True)
    media_data = models.JSONField(blank=True, null=True)
    applicants_details = models.JSONField(blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    complete_date = models.DateField(blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    is_moderate = models.SmallIntegerField()
    problem_desc = models.CharField(max_length=255, blank=True, null=True)
    base_rate = models.IntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField()
    update_date = models.DateField()
    rate = models.IntegerField()
    views_count = models.IntegerField()

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

          
    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(str(application_status[int(self.status.title)-1][1])))


    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view



    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        db_table = 'applications'
        ordering = ("status", 'user')


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
    work_schedule = models.JSONField(blank=True, null=True)
    is_email_alert = models.IntegerField()
    is_sms_alert = models.IntegerField()
    is_generate_daily_report = models.IntegerField()
    is_visible = models.IntegerField()
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Исполнительный орган'
        verbose_name_plural = 'Исполнительные органы'

        db_table = 'executive_authority'
        unique_together = (('title', 'hash_tag', 'tg_id'),)


class MailingQueue(models.Model):
    mailing_address = models.CharField(max_length=30)
    mailing_type = models.IntegerField()
    status = models.IntegerField()
    template_name = models.CharField(max_length=30, blank=True, null=True)
    template_object = models.JSONField(blank=True, null=True)
    application = models.ForeignKey(Applications, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Очередь'
        verbose_name_plural = 'Очередь рассылки'

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
    admin = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    is_visible = models.IntegerField()
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)
    stories_type = models.IntegerField()
    views_count = models.IntegerField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        
        db_table = 'news'


class ProblemCategories(models.Model):
    title = models.CharField(max_length=100)
    mnemonic_name = models.CharField(max_length=100)
    hash_tag = models.CharField(max_length=100)
    icon_file_path = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_visible = models.IntegerField()
    priority = models.IntegerField()
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Категория проблем'
        verbose_name_plural = 'Категории проблем'

        db_table = 'problem_categories'
        unique_together = (('title', 'hash_tag'),)


class Regions(models.Model):
    title = models.CharField(max_length=255)
    is_available = models.SmallIntegerField()
    position = models.IntegerField()
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

        db_table = 'regions'


class Roles(models.Model):
    title = models.CharField(unique=True, max_length=50)
    mnemomic_name = models.CharField(max_length=50, blank=True, null=True)
    delete_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    create_date = models.DateField()

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        db_table = 'roles'


class SavedCoord(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    latitude = models.FloatField()
    longitude = models.IntegerField()
    explanation = models.CharField(max_length=255, blank=True, null=True)
    media_data = models.JSONField(blank=True, null=True)
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.IntegerField(blank=True, null=True)

    class Meta:

        verbose_name = 'Координаты'
        verbose_name_plural = 'Созраненные координаты'

        db_table = 'saved_coord'


class UserProfiles(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_email_alert = models.IntegerField()
    is_sms_alert = models.IntegerField()
    is_anonym = models.IntegerField()
    create_date = models.DateField()
    update_date = models.DateField()
    delete_date = models.DateField(blank=True, null=True)
    rate = models.IntegerField()

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


        db_table = 'user_profiles'




class UserManager(BaseUserManager):

    def create_user(self, login, password=None):
        if not login:
            raise ValueError('User must have an login')

        user = self.model(
            login=login)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        """
        Creates and saves a superuser with the given login and password.
        """
        user = self.create_user(
            login,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    login = models.CharField(max_length=50, unique=True)
    sms_code = models.CharField(max_length=4, blank=True, null=True)
    email_code = models.CharField(max_length=255, blank=True, null=True)
    phone_confirm_date = models.DateField(blank=True, null=True)
    email_confirm_date = models.DateField(blank=True, null=True)
    ban_date = models.DateField(blank=True, null=True)
    delete_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    def get_full_name(self):
        return self.login


    def get_short_name(self):
        return self.login

        
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




# class User(models.Model):
#     login = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)
#     sms_code = models.CharField(max_length=4, blank=True, null=True)
#     email_code = models.CharField(max_length=255, blank=True, null=True)
#     phone_confirm_date = models.DateField(blank=True, null=True)
#     email_confirm_date = models.DateField(blank=True, null=True)
#     ban_date = models.DateField(blank=True, null=True)
#     delete_date = models.DateField(blank=True, null=True)
#     update_date = models.DateField(blank=True, null=True)
#     create_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'User'
#         unique_together = (('login', 'email_code'),)
