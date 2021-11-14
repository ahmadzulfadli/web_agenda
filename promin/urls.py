from django.contrib import admin
from django.urls import path
from apps.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('input/', input, name="input"),
    path('input_Agenda/', input_Agenda, name="input_Agenda"),
    path('ubah/data/<str:id>/', ubah_data, name="ubah_data"),
    path('hapus/<str:id>/', hapus, name="hapus"),
    path('kalender/', kalender, name="kalender"),
    path('tables/', tables, name="tables"),
    path('lihat/<str:id>/', lihat, name="lihat"),

    path('user', user, name="user"),
    path('export/xls/', export_xls, name="export_xls"),

    path('registrasi/', registrasi, name="registrasi"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)