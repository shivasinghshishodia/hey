from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190117_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.TextField(),
        ),
    ]
