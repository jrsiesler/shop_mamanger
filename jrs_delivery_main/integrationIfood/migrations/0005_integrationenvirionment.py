# Generated by Django 4.2 on 2023-05-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrationIfood', '0004_alter_integrationconfig_integration_environment'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrationEnvirionment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
