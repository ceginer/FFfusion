# Generated by Django 4.0.3 on 2023-09-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('target_image', models.ImageField(upload_to='target_images/')),
                ('source_image', models.ImageField(upload_to='source_images/')),
                ('result_image', models.ImageField(blank=True, null=True, upload_to='result_images/%Y/%m/%d')),
            ],
        ),
    ]