# Generated by Django 3.2.13 on 2022-05-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('date_of_retirement', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('marital_status', models.BooleanField(default=False)),
                ('salutation', models.CharField(choices=[('MR', 'Mr'), ('MRS', 'Mrs'), ('MISS', 'Miss')], default='MR', max_length=4)),
                ('highest_qualification', models.CharField(choices=[('BTECH', 'BTech'), ('MTECH', 'MTech'), ('BSC', 'BSc'), ('MSC', 'MSc'), ('MBA', 'MBA'), ('BBA', 'BBA')], max_length=5)),
            ],
        ),
    ]
