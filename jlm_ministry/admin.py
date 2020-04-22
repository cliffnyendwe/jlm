from django.contrib import admin

# Register your models here.
from .models import Pastors, Leadership, Ushering, Transport, Worshipper
from .models import Media,Deacon

admin.site.register(Pastors)
admin.site.register(Leadership)
admin.site.register(Ushering)
admin.site.register(Transport)
admin.site.register(Worshipper)
admin.site.register(Media)
admin.site.register(Deacon)
