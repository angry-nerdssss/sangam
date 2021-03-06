# Generated by Django 2.2.20 on 2021-04-10 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phn', models.CharField(max_length=100)),
                ('pro', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phn', models.CharField(max_length=100)),
                ('pro', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('NGOs', 'NGOs'), ('ORPHANAGE', 'ORPHANAGE'), ('OLD AGE HOMES', 'OLD AGE HOMES')], default='NGOs', max_length=20)),
                ('certificate', models.FileField(null=True, upload_to='certificate/', verbose_name='')),
                ('city', models.CharField(choices=[('LUCKNOW', 'LUCKNOW'), ('MUMBAI', 'MUMBAI'), ('KOLKATA', 'KOLKATA'), ('CHENNAI', 'CHENNAI'), ('HYDERABAD', 'HYDERABAD'), ('JAIPUR', 'JAIPUR'), ('PUNE', 'PUNE'), ('BANGLORE', 'BANGLORE'), ('DELHI', 'DELHI'), ('PATNA', 'PATNA'), ('DEHRADUN', 'DEHRADUN'), ('COIMBATORE', 'COIMBATORE'), ('PRAYAGRAJ', 'PRAYAGRAJ'), ('AYODHYA', 'AYODHYA'), ('GANGTOK', 'GANGTOK')], default='LUCKNOW', max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_or_not', models.BooleanField(default=False)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_invitation', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invitation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField()),
                ('venue', models.CharField(max_length=100)),
                ('feedback_done', models.BooleanField(default=False)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_r', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_s', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_after_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_day', models.CharField(max_length=100)),
                ('how_other', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('feedback_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_r', to='first.Organisation')),
                ('feedback_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_s', to='first.Organisation')),
            ],
        ),
    ]
