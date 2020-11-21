# Generated by Django 3.0.5 on 2020-11-19 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('about', models.TextField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(default='http://dfoundation.moneylife.in/media/uploads/video_thumbnails/default-image.png', upload_to='pins/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest.ImageFile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]