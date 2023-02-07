# Generated by Django 3.2.16 on 2023-02-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_subscription_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='field_a',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='subscription',
            name='field_b',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['field_a', 'field_b'], name='services_su_field_a_155836_idx'),
        ),
    ]
