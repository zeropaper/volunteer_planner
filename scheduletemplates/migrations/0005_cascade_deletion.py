# Generated by Django 2.0.5 on 2019-07-18 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduletemplates', '0004_shifttemplate_members_only'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifttemplate',
            name='workplace',
            field=models.ForeignKey(verbose_name='workplace', to='organizations.Workplace',
                                    null=True, blank=True,
                                    on_delete=django.db.models.deletion.CASCADE),
        ),
    ]