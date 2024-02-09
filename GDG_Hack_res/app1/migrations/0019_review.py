# Generated by Django 5.0.2 on 2024-02-09 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_critic_delete_critics_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('critic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.critic')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.judge')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.submission')),
            ],
        ),
    ]
