import random

from django.db.models import Max
from django.http import Http404
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Section , Quiz
from .serializers import SectionSerializer, QuestionSerializer


class ListSections(generics.ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class StartQuiz(APIView):

    def get(self, request, category_id=None):
        try:
            quiz = Quiz.objects.get(category__id=category_id)
        except Quiz.DoesNotExist:
            raise Http404
        serializer = QuestionSerializer(quiz.question.all(), many=True)
        return  Response(serializer.data)
