# Generated by Django 4.0 on 2022-08-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_alter_admin_id_alter_atendence_id_alter_employee_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendence',
            name='attendence',
        ),
        migrations.AddField(
            model_name='atendence',
            name='entry_attendence',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='atendence',
            name='entry_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='atendence',
            name='exit_attendence',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='atendence',
            name='exit_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
