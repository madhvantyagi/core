from django.contrib import admin

from questions.models import QuesMcq, QuesIntType

# Register your models here.

class QuesMcqInline(admin.ModelAdmin):
    search_fields = ('subject', 'question')
    list_display = ('question', 'answer', 'subject', 'publish')
    list_filter = ('subject', 'publish')

class QuesIntTypeInline(admin.ModelAdmin):
    search_fields = ('subject', 'question')
    list_display = ('question', 'correct_answer', 'subject', 'publish')
    list_filter = ('subject', 'publish')

admin.site.register(QuesMcq, QuesMcqInline)
admin.site.register(QuesIntType, QuesIntTypeInline)