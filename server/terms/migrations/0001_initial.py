# Generated by Django 2.1.12 on 2019-09-29 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(db_index=True)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('content', models.TextField()),
                ('enabled', models.BooleanField()),
            ],
            options={
                'permissions': [('full', '管理用户条款')],
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='agreement',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terms.Terms'),
        ),
    ]
