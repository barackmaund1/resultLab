# Generated by Django 2.1 on 2018-09-30 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_student_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('session', models.CharField(max_length=250)),
                ('term', models.CharField(max_length=250)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('classz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Class')),
            ],
            options={
                'db_table': 'resultsheets',
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='StudentResultSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('total_score', models.IntegerField()),
                ('average', models.DecimalField(decimal_places=2, max_digits=3)),
                ('attendance', models.IntegerField()),
                ('remark', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('result_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_sheet', to='apps.result.ResultSheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student_result_sheet',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='StudentSubjectResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('position', models.IntegerField()),
                ('student_result_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_sheet', to='apps.result.StudentResultSheet')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Subject')),
            ],
            options={
                'db_table': 'subject_result',
            },
        ),
    ]
