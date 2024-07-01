# Generated by Django 4.2.13 on 2024-07-01 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("labels", "0001_labels_init"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("statuses", "0001_statuses_init"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, unique=True, verbose_name="name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tasks_where_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="creator",
                    ),
                ),
                (
                    "executor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tasks_where_executor",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="executor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskToLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="labels.label"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True,
                related_name="tasks",
                through="tasks.TaskToLabel",
                to="labels.label",
                verbose_name="labels",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tasks",
                to="statuses.taskstatus",
                verbose_name="status",
            ),
        ),
    ]