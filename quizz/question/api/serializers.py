from ..models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question_text', 'max_marks', 'level')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('pk', 'question', 'choice')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'slevel', 'score')