from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model


User = get_user_model()


class Section(models.Model):
    section_name = models.CharField(max_length=150)

    def __str__(self):
        return self.section_name

class Answer(models.Model):
    answer_text = models.CharField(max_length=150)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=150)
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE,
                                  related_name='correct_answer', null=True, blank=True)
    choices = models.ManyToManyField(Answer, related_name='choices')

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=150)
    question = models.ManyToManyField(Question, blank=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.quiz_name
