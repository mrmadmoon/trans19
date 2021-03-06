# Generated by Django 3.0.6 on 2020-05-16 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_comfirmed', models.DateField()),
                ('case_number', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=127)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(choices=[('Central and Western', 'Central and Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai'), ('Sham Shui Po', 'Sham Shui Po'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long')], default='Central and Western', max_length=20)),
                ('x_coord', models.DecimalField(decimal_places=4, max_digits=22, null=True)),
                ('y_coord', models.DecimalField(decimal_places=4, max_digits=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('detail', models.CharField(blank=True, max_length=127, null=True)),
                ('category', models.CharField(max_length=30)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.CaseRecord')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.LocationRecord')),
            ],
        ),
    ]
