# Generated by Django 4.2.5 on 2024-01-27 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('leave_from', models.DateField()),
                ('leave_to', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leave.users')),
            ],
        ),
    ]
