# Generated by Django 4.1.2 on 2022-11-28 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog_community_app', '0009_breed_breed_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='field_user_name',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_address',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.dogs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.user')),
            ],
        ),
    ]
