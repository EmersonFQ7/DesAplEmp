from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, api_root  # ← Updated Import

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)    # ← ADDED
router.register(r'choices', ChoiceViewSet)        # ← ADDED

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]