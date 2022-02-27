# Generated by Django 2.0.5 on 2019-07-18 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_add_timeline_view_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitymembership',
            name='facility',
            field=models.ForeignKey(related_query_name='membership',
                                    related_name='memberships',
                                    verbose_name='facility',
                                    to='organizations.Facility',
                                    on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AlterField(
            model_name='organizationmembership',
            name='organization',
            field=models.ForeignKey(related_query_name='membership',
                                    related_name='memberships',
                                    to='organizations.Organization',
                                    verbose_name='organization',
                                    on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
