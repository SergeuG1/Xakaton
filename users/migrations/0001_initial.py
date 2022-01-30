# Generated by Django 4.0.1 on 2022-01-30 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_admin_geomap


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('sms_code', models.CharField(blank=True, max_length=4, null=True)),
                ('email_code', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_confirm_date', models.DateTimeField(blank=True, null=True)),
                ('email_confirm_date', models.DateTimeField(blank=True, null=True)),
                ('ban_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('media_data', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('applicants_details', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('complete_date', models.DateTimeField(blank=True, null=True)),
                ('final_date', models.DateTimeField(blank=True, null=True)),
                ('is_moderate', models.IntegerField()),
                ('problem_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('base_rate', models.IntegerField()),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('views_count', models.IntegerField()),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator', to=settings.AUTH_USER_MODEL)),
                ('redirect_to_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.applications')),
            ],
            options={
                'db_table': 'applications',
            },
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[(1, 'В обработке'), (2, 'В рассмотрении'), (3, 'Исполнение'), (4, 'Проверка исполнения'), (5, 'Выполнено'), (6, 'Архивная')], max_length=20, unique=True)),
            ],
            options={
                'db_table': 'application_status',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_available', models.SmallIntegerField()),
                ('position', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('guest', 'guest'), ('user', 'user'), ('admin', 'admin'), ('superuser', 'superuser')], max_length=50, unique=True)),
                ('mnemomic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='TokenBlocklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jti', models.CharField(max_length=36)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'token_blocklist',
            },
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('is_email_alert', models.IntegerField()),
                ('is_sms_alert', models.IntegerField()),
                ('is_anonym', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('rate', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='SavedCoord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.IntegerField()),
                ('explanation', models.CharField(blank=True, max_length=255, null=True)),
                ('media_data', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'saved_coord',
            },
        ),
        migrations.CreateModel(
            name='ProblemCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mnemonic_name', models.CharField(max_length=100)),
                ('hash_tag', models.CharField(max_length=100)),
                ('icon_file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.IntegerField()),
                ('is_visible', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'problem_categories',
                'unique_together': {('title', 'hash_tag')},
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('group_name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.IntegerField()),
                ('author_name', models.CharField(max_length=30)),
                ('type', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('life_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('is_visible', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('stories_type', models.IntegerField()),
                ('views_count', models.IntegerField()),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='MailingQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_address', models.CharField(max_length=30)),
                ('mailing_type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('template_name', models.CharField(blank=True, max_length=30, null=True)),
                ('template_object', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.applications')),
            ],
            options={
                'db_table': 'mailing_queue',
            },
        ),
        migrations.CreateModel(
            name='ExecutiveAuthority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('mnemomic_name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('responsible_person', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('hash_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email_administration', models.CharField(blank=True, max_length=255, null=True)),
                ('tg_id', models.CharField(blank=True, max_length=255, null=True)),
                ('web_site_link', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_information', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(max_length=20)),
                ('work_schedule', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('is_email_alert', models.IntegerField()),
                ('is_sms_alert', models.IntegerField()),
                ('is_generate_daily_report', models.IntegerField()),
                ('is_visible', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'executive_authority',
                'unique_together': {('title', 'hash_tag', 'tg_id')},
            },
        ),
        migrations.CreateModel(
            name='ContractorsProblems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.executiveauthority')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.problemcategories')),
            ],
            options={
                'db_table': 'contractors_problems',
            },
        ),
        migrations.CreateModel(
            name='ApplicationsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.applications')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.problemcategories')),
            ],
            options={
                'db_table': 'applications_categories',
            },
        ),
        migrations.AddField(
            model_name='applications',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.applicationstatus'),
        ),
        migrations.AddField(
            model_name='applications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AdminApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField()),
                ('explanation', models.CharField(blank=True, max_length=255, null=True)),
                ('estimated_date_work', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('media_data', models.TextField(db_collation='utf8mb4_bin')),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('administration', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.executiveauthority')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.applications')),
            ],
            options={
                'db_table': 'admin_applications',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.roles'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='users',
            unique_together={('login', 'email_code')},
        ),
    ]
