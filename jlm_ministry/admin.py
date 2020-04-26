from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string


from .models import *

class PastorsAdmin(admin.ModelAdmin):
    class Meta:
        model = Pastors
        exclude = ['__all__']

class LeadershipAdmin(admin.ModelAdmin):
    class Meta:
        model = Leadership
        exclude = ['__all__']

class UsheringAdmin(admin.ModelAdmin):
    class Meta:
        model = Ushering
        exclude = ['__all__']

class TransportAdmin(admin.ModelAdmin):
    class Meta:
        model = Transport
        exclude = ['__all__']

class MediaAdmin(admin.ModelAdmin):
    class Meta:
        model = Media
        exclude = ['__all__']

class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
        exclude = ['__all__']

class WorshipperAdmin(admin.ModelAdmin):
    class Meta:
        model = Worshipper
        exclude = ['__all__']

class ExtremeAdmin(admin.ModelAdmin):
    class Meta:
        model = Extreme
        exclude = ['__all__']

class TrusteeAdmin(admin.ModelAdmin):
    class Meta:
        model = Trustee
        exclude = ['__all__']

class DeaconAdmin(admin.ModelAdmin):
    class Meta:
        model = Deacon
        exclude = ['__all__']

class TestimonyAdmin(admin.ModelAdmin):
    class Meta:
        model = Testimony
        exclude = ['__all__']

admin.site.register(Pastors, PastorsAdmin)
admin.site.register(Leadership, LeadershipAdmin)
admin.site.register(Ushering, UsheringAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Worshipper, WorshipperAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Deacon, DeaconAdmin)
admin.site.register(Trustee, TrusteeAdmin)
admin.site.register(Extreme, ExtremeAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Testimony, TestimonyAdmin)
