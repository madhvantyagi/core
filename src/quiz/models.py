from django.db import models
from questions.models import QuesIntType, QuesMcq

## Dont Think that a model for Quiz will be needed.
# Create your models here.
class OneSubjectQuiz(models.Model):
    SUB_CHOICES = (
        ('physics' ,'Physics'),
        ('maths' ,'Maths'),
        ('chem', 'Chemistry')
    )
    
    subject    = models.CharField(max_length=50 ,choices=SUB_CHOICES)
    time       = models.IntegerField(help_text='(In Minutes)')
    no_of_ques = models.IntegerField()
    
    def __str__(self):
        return self.subject + " Quiz"
    
    class Meta:
        verbose_name_plural = "One Subject Quizes"
        verbose_name = "One Subject Quiz"