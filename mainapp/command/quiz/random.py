from django.core.management.base import BaseCommand, CommandError

from mainapp.models import Section, Question, Quiz


class QuizCommand(BaseCommand):
    help = 'Creates random quizes based on available sections'

    def handle(self, *args, **options):
        if not Section.objects.count():
            raise CommandError('No sections are available')
        Quiz.objects.all().delete()
        for section in Section.objects.all():
            quiz = Quiz(quiz_name='{} quiz'.format(section.section_name),
                        category=section)
            quiz.save()
            questions = list(Question.objects.filter(category=section))
            quiz.question.add(*questions)
            quiz.save()
        self.stdout.write(self.style.SUCCESS('Quiz Created'))
