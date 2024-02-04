# Generated by Django 4.1.1 on 2024-02-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursePortal', '0007_alter_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('W', 'Web Design'), ('D', 'Graphic design'), ('V', 'Video Editing'), ('O', 'Online Marketing')], default='W', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AddField(
            model_name='course',
            name='to_be_listed',
            field=models.BooleanField(default=True),
        ),
    ]