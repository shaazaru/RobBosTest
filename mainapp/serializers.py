from rest_framework import serializers

from .models import Answer, Section, Question


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ('__all__',)

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text')


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    def get_choices(self, obj):
        ordered_queryset = Answer.objects.filter(choices__id=obj.id).order_by('?')
        return ChoiceSerializer(ordered_queryset, many=True, context=self.context).data
    class Meta:
        model = Question
        fields = ('question_text', 'choices')
