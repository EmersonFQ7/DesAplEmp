from rest_framework import serializers
from .models import Quiz, Question, Choice

# --- Existing Serializers (Part 1 & 2) ---

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'created_at']
        read_only_fields = ['created_at']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']

# --- New Serializers (Part 3) ---

class ChoiceDetailSerializer(serializers.ModelSerializer):
    """For displaying choices without revealing correct answers"""
    class Meta:
        model = Choice
        # IMPORTANT: is_correct is NOT included here to prevent cheating
        fields = ['id', 'text'] 

class QuestionDetailSerializer(serializers.ModelSerializer):
    """Question with all its choices"""
    # Nested serializer for the choices related to this question
    choices = ChoiceDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    """Complete quiz with questions and choices"""
    # Nested serializer for the questions related to this quiz
    questions = QuestionDetailSerializer(many=True, read_only=True)
    
    # Custom field to show the count of questions
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'question_count', 'questions']
    
    def get_question_count(self, obj):
        # Accesses the related manager 'questions' (defined in models.py)
        return obj.questions.count()

class SubmitAnswerSerializer(serializers.Serializer):
    """For validating submitted answers structure"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()