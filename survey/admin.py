from django.contrib import admin
from survey.models import Survey, Question, Option, Submission, Answer
# Register your models here.

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Submission)
admin.site.register(Answer)
