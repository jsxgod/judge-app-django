from django.contrib import admin


from .models import *

admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Competition)
admin.site.register(Crew)
admin.site.register(Score)