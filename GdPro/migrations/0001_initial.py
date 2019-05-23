# Generated by Django 2.2 on 2019-05-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Expclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'expclass',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('expid', models.AutoField(primary_key=True, serialize=False)),
                ('classid', models.CharField(blank=True, max_length=120, null=True)),
                ('courseid', models.CharField(blank=True, max_length=120, null=True)),
                ('teacherid', models.CharField(blank=True, max_length=120, null=True)),
                ('addressid', models.CharField(blank=True, max_length=120, null=True)),
                ('term', models.CharField(blank=True, max_length=20, null=True)),
                ('weeknumber', models.IntegerField(blank=True, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'experiment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('account', models.CharField(blank=True, max_length=6, null=True)),
                ('password', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]
