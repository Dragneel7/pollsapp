from django.contrib import admin
from polls.models import Question, Choice
from django.utils import *
import datetime

class ChoiceInline(admin.TabularInline):
      model = Choice
      extra = 3



class QuestionAdmin(admin.ModelAdmin):
     
     list_display = ('question_text','pub_date','was_published_recently')     
 
     def was_published_recently(self,obj):
         return obj.pub_date >=timezone.now() - datetime.timedelta(days=1)
     was_published_recently.admin_order_field = 'pub_date' 
     was_published_recently.boolean= True
     was_published_recently.short_description = 'Published recently?'
     list_filter = ['pub_date']    



     fieldsets = [
         (None,              {'fields':['question_text']}),
         ('Date information',{'fields':['pub_date'], 'classes':['collapse']}),     

     ]
     inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)

# Register your models here.
