from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "IEBC"
admin.site.site_title = "Your trusted voting poll"
admin.site.index_title = "Welcome to our Voting Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)