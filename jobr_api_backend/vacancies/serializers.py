from rest_framework import serializers
from accounts.models import Employee
from .models import Vacancy, ApplyVacancy, VacancyLanguage, VacancyDescription, VacancyQuestion, Weekday
from .models import ContractType, Function, Question, Skill, Language, Location
from common.models import Extra

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


class VacancyLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyLanguage
        fields = ['language', 'mastery']

class VacancyDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyDescription
        fields = ['question', 'description']

class VacancyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyQuestion
        fields = ['question']

class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = ['name']

class VacancySerializer(serializers.ModelSerializer):
    contract_type = serializers.PrimaryKeyRelatedField(queryset=ContractType.objects.all(), allow_null=True)
    function = serializers.PrimaryKeyRelatedField(queryset=Function.objects.all(), allow_null=True)
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), allow_null=True)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    languages = VacancyLanguageSerializer(many=True)
    descriptions = VacancyDescriptionSerializer(many=True)
    questions = VacancyQuestionSerializer(many=True)
    week_day = WeekdaySerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ['employer', 'expected_mastery', 'contract_type', 'location', 'function', 'week_day', 'job_date',
                  'salary', 'languages', 'descriptions', 'questions', 'skill']


    def create(self, validated_data):
        languages_data = validated_data.pop('languages')
        descriptions_data = validated_data.pop('descriptions')
        questions_data = validated_data.pop('questions')
        week_days_data = validated_data.pop('week_day')
        skills_data = validated_data.pop('skill')

        vacancy = Vacancy.objects.create(**validated_data)

        for language_data in languages_data:
            VacancyLanguage.objects.create(**language_data, vacancy=vacancy)

        for description_data in descriptions_data:
            VacancyDescription.objects.create(**description_data, vacancy=vacancy)

        for question_data in questions_data:
            VacancyQuestion.objects.create(**question_data, vacancy=vacancy)

        for week_day_data in week_days_data:
            week_day = Weekday.objects.get(**week_day_data)
            vacancy.week_day.set(week_day)

        vacancy.skill.set(skills_data)

        return vacancy


class ApplySerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=False)
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all(), many=False)

    class Meta:
        model = ApplyVacancy
        fields = ['employee', 'vacancy']
