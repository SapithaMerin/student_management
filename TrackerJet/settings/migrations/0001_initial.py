# Generated by Django 4.2.2 on 2023-06-16 09:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100, null=True, verbose_name='CourseName')),
                ('BatchName', models.CharField(max_length=200, null=True)),
                ('Trainer', models.CharField(choices=[('Anagha', 'Anagha'), ('Gopika', 'Gopika'), ('Neethu', 'Neethu')], max_length=6, null=True)),
                ('StartDate', models.DateField(null=True)),
                ('EndDate', models.DateField(null=True)),
                ('Closed', models.BooleanField(default=False)),
                ('Active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Companies', models.CharField(max_length=200)),
                ('Address1', models.CharField(blank=True, max_length=200)),
                ('Address2', models.CharField(blank=True, max_length=200)),
                ('Address3', models.CharField(blank=True, max_length=200)),
                ('Phone', models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Email', models.EmailField(blank=True, max_length=200)),
                ('Website', models.CharField(blank=True, max_length=200)),
                ('Logo', models.ImageField(null=True, upload_to='image')),
                ('Active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Companies',
                'ordering': ['Companies'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(blank=True, max_length=100, null=True)),
                ('CourseCode', models.CharField(blank=True, max_length=100, null=True)),
                ('Active', models.BooleanField(default=False)),
                ('Fees', models.CharField(blank=True, max_length=20, null=True)),
                ('Syllabus', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100, null=True, verbose_name='CourseName')),
                ('FeesType', models.CharField(choices=[('Two Time', 'Two Time'), ('One Time', 'One Time'), ('Three Time', 'Three Time'), ('Registration', 'Registration')], max_length=100, null=True, verbose_name='FeesType')),
                ('Amount', models.CharField(max_length=10, null=True, verbose_name='Amount')),
                ('Tax', models.CharField(max_length=10, null=True, verbose_name='Tax')),
                ('InstallmentPeriod', models.CharField(max_length=10, null=True, verbose_name='Installment Period')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateName', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'states',
                'ordering': ['StateName'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DistrictName', models.CharField(blank=True, max_length=50, null=True, verbose_name='DistrictName')),
                ('StateName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.state', verbose_name='StateName')),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
                'ordering': ['DistrictName'],
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=200)),
                ('Street', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('Phone', models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Email', models.EmailField(blank=True, max_length=200)),
                ('District', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.district')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.state')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
                'ordering': ['Branch'],
            },
        ),
    ]