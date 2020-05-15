from django.contrib import admin
from .models import Answer,Section,Question,Quiz

# Register your models here.
admin.site.register(Answer)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Quiz)
