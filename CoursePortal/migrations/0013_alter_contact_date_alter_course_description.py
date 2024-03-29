# Generated by Django 5.0.1 on 2024-02-09 06:02

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursePortal', '0012_course_course_img_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 9)),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
