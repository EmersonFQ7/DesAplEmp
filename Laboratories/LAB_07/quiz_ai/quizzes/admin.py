from django.contrib import admin
from .models import Quiz, Question, Choice

# --- Inlines (Para edición anidada en el Admin) ---

class ChoiceInline(admin.TabularInline):
    """📝 Permite editar Choices directamente en el formulario de Question"""
    model = Choice
    extra = 4  # Muestra 4 campos de opciones vacíos

class QuestionInline(admin.TabularInline):
    """❓ Permite editar Questions directamente en el formulario de Quiz"""
    model = Question
    extra = 2  # Muestra 2 campos de preguntas vacíos

# --- Clases Admin ---

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'questions_count']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    inlines = [QuestionInline]  # 🆕 Editar preguntas inline
    
    def questions_count(self, obj):
        # Muestra el número de preguntas
        return obj.questions.count()
    questions_count.short_description = 'Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'quiz', 'choices_count']
    list_filter = ['quiz']
    search_fields = ['text']
    inlines = [ChoiceInline]  # 🆕 Editar opciones inline
    
    def text_preview(self, obj):
        # Muestra una vista previa corta del texto
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Question'
    
    def choices_count(self, obj):
        # Muestra el número de opciones
        return obj.choices.count()
    choices_count.short_description = 'Choices'

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question_preview', 'is_correct']
    list_filter = ['is_correct', 'question__quiz']
    search_fields = ['text']
    
    def question_preview(self, obj):
        # Muestra una vista previa de la pregunta a la que pertenece
        return obj.question.text[:30] + "..." if len(obj.question.text) > 30 else obj.question.text
    question_preview.short_description = 'Question'