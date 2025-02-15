# Generated by Django 2.2.3 on 2022-03-23 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0015_add_priority_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Higher value = higher priority",
                null=True,
                verbose_name="priority",
            ),
        ),
        migrations.AlterField(
            model_name="workplace",
            name="priority",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Higher value = higher priority",
                null=True,
                verbose_name="priority",
            ),
        ),
    ]
