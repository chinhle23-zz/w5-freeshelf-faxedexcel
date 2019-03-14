# Generated by Django 2.1.7 on 2019-03-14 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('freeshelfapp', '0007_auto_20190312_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeshelfapp.Book'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]