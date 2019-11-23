from django.contrib import admin

from .models import Selection, Choice, Participation

admin.site.register(Selection)
admin.site.register(Choice)
admin.site.register(Participation)
