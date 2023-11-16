# Generated by Django 4.2.7 on 2023-11-16 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_eco', '0002_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('image_url', models.TextField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_eco.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_eco.user')),
            ],
        ),
    ]
