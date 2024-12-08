# Generated by Django 5.1.3 on 2024-12-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='GeneroMusical',
            new_name='Albums',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artista',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genero',
        ),
        migrations.RenameField(
            model_name='albums',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.DeleteModel(
            name='Artista',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
