# Generated by Django 4.2 on 2023-04-30 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('total_shopping_amount', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('last_shoped_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.RenameModel(
            old_name='Role',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.location'),
        ),
        migrations.AddField(
            model_name='customer',
            name='prefferred_shopping_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.category'),
        ),
    ]
