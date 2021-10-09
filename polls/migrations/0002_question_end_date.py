"""Question and end date for migration file."""
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    """Migration for the polls."""

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now,
                                       verbose_name='date time ended'),
            preserve_default=False,
        ),
    ]
