# Generated by Django 4.1.2 on 2022-12-04 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_login_id', models.CharField(max_length=255)),
                ('admin_login_pass', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('breed_id', models.AutoField(primary_key=True, serialize=False)),
                ('breed_name', models.CharField(max_length=255)),
                ('bred_for', models.CharField(default='', max_length=1000)),
                ('life_span', models.CharField(default='', max_length=1000)),
                ('temperament', models.CharField(default='', max_length=1000)),
                ('origin', models.CharField(default='', max_length=1000)),
                ('breed_image_path', models.ImageField(blank=True, upload_to='images/breeds')),
                ('breed_article', models.CharField(default='', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('dog_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_adopted', models.BooleanField()),
                ('dog_name', models.CharField(max_length=255)),
                ('dog_color', models.CharField(max_length=255)),
                ('dog_age', models.IntegerField()),
                ('dog_image', models.ImageField(upload_to='images/dogs')),
                ('is_disable', models.BooleanField()),
                ('disabilty', models.CharField(blank=True, max_length=5000)),
                ('unique_identification', models.CharField(max_length=5000)),
                ('is_adoption_ready', models.BooleanField()),
                ('is_featured', models.BooleanField(default=False)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.breed')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_location', models.CharField(max_length=5000)),
                ('event_time', models.DateTimeField()),
                ('event_duration', models.IntegerField()),
                ('event_capacity', models.IntegerField()),
                ('event_description', models.CharField(max_length=5000)),
                ('event_image', models.ImageField(default='images/default_event.jpg', upload_to='images/events')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('member_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('member_image', models.CharField(default='', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_address', models.CharField(blank=True, max_length=5000)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_known_location', models.CharField(max_length=5000)),
                ('category', models.CharField(max_length=255)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.breed')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.dogs')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='EventSubscriptions',
            fields=[
                ('subscription_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.user')),
            ],
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
