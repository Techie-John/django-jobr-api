from rest_framework import serializers
from accounts.models import Employer, Employee
from .models import Vacancy, ApplyVacancy
from common.models import ContractType, Function, Question, Skill, Extra, Language, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location']

class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = ['id', 'contract_type']


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['id', 'function']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill', 'category']


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['extra']


class VacancySerializer(serializers.ModelSerializer):
    employer = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all(), many=False)
    contract_type = serializers.PrimaryKeyRelatedField(queryset=ContractType.objects.all(), many=False)
    function = serializers.PrimaryKeyRelatedField(queryset=Function.objects.all(), many=False)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True)
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)

    class Meta:
        model = Vacancy
        fields = ['employer', 'title', 'contract_type', 'function', 'location', 'skill', 'week_day', 'salary', 'description',
                  'language', 'question', 'latitude', 'longitude']


class ApplySerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=False)
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all(), many=False)

    class Meta:
        model = ApplyVacancy
        fields = ['employee', 'vacancy']
