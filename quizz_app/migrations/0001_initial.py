# Generated by Django 3.0.2 on 2020-01-17 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_category', models.CharField(default='0', max_length=150)),
                ('quiz_name', models.TextField()),
                ('quiz_description', models.TextField(blank=True)),
                ('quiz_randomizable', models.BooleanField(default=False)),
                ('quiz_penalization', models.IntegerField(default=0)),
                ('quiz_allowed_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_attempts', models.IntegerField(default=0)),
                ('quiz_avg_result', models.IntegerField(default=0)),
                ('quiz_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_quiz', to='quizz_app.Quiz')),
                ('quiz_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_fails', models.IntegerField(default=0)),
                ('question_hits', models.IntegerField(default=0)),
                ('question_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_question', to='quizz_app.Question')),
                ('question_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_quiz', to='quizz_app.Quiz'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('correct_answer', models.BooleanField(default=False)),
                ('answer_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_question', to='quizz_app.Question')),
            ],
        ),
    ]
