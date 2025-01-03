# Generated by Django 5.1.2 on 2024-11-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbots', '0003_chatbot_image_alter_usage_interactions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='default_greeting',
            field=models.TextField(default='Hello! How can I help you today?', max_length=200),
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
