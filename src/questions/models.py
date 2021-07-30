from django.contrib.admin import options
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class QuesMcq(models.Model):
    SUB_CHOICES = (
        ('physics' ,'Physics'),
        ('maths' ,'Maths'),
        ('chem', 'Chemistry')
    )
    
    question = models.CharField(max_length=500, null=True)
    question_image = models.ImageField(upload_to='media/images', null=True, blank=True)
    
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    option_4 = models.CharField(max_length=500)
    
    ANS_CHOICES = (
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'), 
        ('option_3', 'Option 3'), 
        ('option_4', 'Option 4'),
    )
    
    answer   = models.CharField(max_length=50, choices=ANS_CHOICES)
    
    subject  = models.CharField(max_length=50 ,choices=SUB_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    publish  = models.BooleanField(default=True)
    difficulty_level = models.IntegerField(default=1, validators = [MaxValueValidator(5)] , help_text='Take Range from 1 to 5 only')
    
    class Meta:
        verbose_name = 'MCQ type Question'
    
    
class QuesIntType(models.Model):
    SUB_CHOICES = (
        ('physics' ,'Physics'),
        ('maths' ,'Maths'),
        ('chem', 'Chemistry')
    )
    
    question = models.CharField(max_length=500, null=True)
    question_image = models.ImageField(upload_to='media/images', null=True, blank=True)
    correct_answer = models.DecimalField(decimal_places=3, max_digits=10)
    
    subject  = models.CharField(max_length=50 ,choices=SUB_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    publish  = models.BooleanField(default=True)
    difficulty_level = models.IntegerField(default=1, validators = [MaxValueValidator(5)] , help_text='Take Range from 1 to 5 only')
    
    class Meta:
        verbose_name = 'Numeric Type Question'