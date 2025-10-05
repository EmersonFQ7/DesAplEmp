from rest_framework import viewsets, status  # ← Added status
from rest_framework.decorators import api_view, action  # ← Added action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    QuizDetailSerializer, SubmitAnswerSerializer  # ← Added new serializers
)

# --- Updated API Root (Change 3) ---

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': '🧠 Welcome to Quiz.AI API',
        'version': 'v1.0',
        'description': 'Intelligent Quiz Management System',
        'features': [
            '✨ Create and manage quizzes',
            '❓ Add multiple-choice questions',
            '🎓 Submit answers and get instant grading',
            '📊 Track scores and performance'
        ],
        'workflow': [
            '1️⃣ Create a quiz (POST /quizzes/)',
            '2️⃣ Add questions (POST /questions/)',
            '3️⃣ Add choices (POST /choices/)',
            '4️⃣ View complete quiz (GET /quizzes/{id}/)',
            '5️⃣ Submit answers (POST /quizzes/{id}/submit/)'
        ],
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'choices': reverse('choice-list', request=request, format=format),
        },
        'grading_system': {
            '90-100%': 'A 🏆 Outstanding',
            '80-89%': 'B 🎉 Great',
            '70-79%': 'C 👍 Good',
            '60-69%': 'D 📚 Pass',
            '0-59%': 'F 💪 Try Again'
        }
    })

# --- Enhanced QuizViewSet (Change 2) ---

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    
    # Determines which serializer to use based on the action
    def get_serializer_class(self):
        # Use QuizDetailSerializer for 'retrieve' (GET /quizzes/id/)
        if self.action == 'retrieve':
            return QuizDetailSerializer
        # Use QuizSerializer for all other actions (list, create, update)
        return QuizSerializer
    
    # Custom action to submit answers: POST /quizzes/{id}/submit/
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        quiz = self.get_object()
        
        # 1. Validate the structure of the incoming answers list
        # Expects: {'answers': [{'question_id': X, 'choice_id': Y}, ...]}
        serializer = SubmitAnswerSerializer(data=request.data.get('answers', []), many=True)
        
        if not serializer.is_valid():
            return Response({
                'error': '❌ Invalid answer format',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        answers = serializer.validated_data
        results = []
        correct_count = 0
        
        # 2. Process and validate each answer against the database
        for answer in answers:
            try:
                # Ensure question belongs to the specified quiz
                question = Question.objects.get(id=answer['question_id'], quiz=quiz)
                # Ensure choice belongs to the specified question
                choice = Choice.objects.get(id=answer['choice_id'], question=question)
                
                # Check if the choice is correct
                is_correct = choice.is_correct
                if is_correct:
                    correct_count += 1
                
                results.append({
                    'question_id': question.id,
                    'question_text': question.text,
                    'choice_id': choice.id,
                    'choice_text': choice.text,
                    'is_correct': is_correct,
                    'emoji': '✅' if is_correct else '❌'
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                # Handle cases where the ID does not exist or doesn't match the quiz/question context
                results.append({
                    'question_id': answer['question_id'],
                    'error': '⚠️ Invalid question or choice ID submitted for this quiz.'
                })
        
        # 3. Calculate Score and Grade
        total = len(results)
        percentage = round((correct_count / total) * 100, 2) if total > 0 else 0
        
        # Grading system logic
        if percentage >= 90:
            grade, emoji, message = 'A', '🏆', 'Outstanding!'
        elif percentage >= 80:
            grade, emoji, message = 'B', '🎉', 'Great job!'
        elif percentage >= 70:
            grade, emoji, message = 'C', '👍', 'Good work!'
        elif percentage >= 60:
            grade, emoji, message = 'D', '📚', 'Keep studying!'
        else:
            grade, emoji, message = 'F', '💪', 'Try again!'
        
        # 4. Return the comprehensive results
        return Response({
            'quiz_id': quiz.id,
            'quiz_title': quiz.title,
            'total_questions': total,
            'correct_answers': correct_count,
            'incorrect_answers': total - correct_count,
            'score': f"{correct_count}/{total}",
            'percentage': percentage,
            'grade': grade,
            'emoji': emoji,
            'message': f"{emoji} {message} You got {correct_count} out of {total} correct!",
            'results': results
        })

# QuestionViewSet and ChoiceViewSet remain unchanged
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer