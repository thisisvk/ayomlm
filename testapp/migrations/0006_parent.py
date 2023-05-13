# Generated by Django 4.2 on 2023-05-12 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_remove_userprofile_left_remove_userprofile_right'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.left')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.right')),
            ],
        ),
    ]
