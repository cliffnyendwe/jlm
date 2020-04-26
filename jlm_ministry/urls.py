from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('ushering', views.ushering,name='ushering'),
    path('transport', views.transport,name='transport'),
    path('media', views.media,name='media'),
    path('living_voice', views.living_voice,name='living_voice'),
    path('boa_base', views.boa_base, name='boa_base'),
    path('deacon', views.deacon,name='deacon'),
    path('extreme_grace', views.extreme_grace,name='extreme_grace'),
    path('pastors', views.pastors,name='pastors'),
    path('board_of_trustee', views.board_of_trustee,name='board_of_trustee'),
    path('event', views.event,name='event'),
    path('contact', views.contact,name='contact'),
    path('success',views.success,name='success'),
    path('testimonies', views.testimonies,name='testimonies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
