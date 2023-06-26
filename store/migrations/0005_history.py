# Generated by Django 3.2.9 on 2023-06-20 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_items_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('item_name', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=2000, null=True)),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_category', to='store.department')),
            ],
        ),
    ]
