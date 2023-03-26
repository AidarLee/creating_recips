from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.conf.urls import handler400, handler403, handler404, handler500
from main import views
from django.contrib.auth import views as auth_views


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
)

if settings.DEBUG == False:
    urlpatterns = static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    
# handler400 = 'main.views.error_400'
# handler404 = 'main.views.error_404'
# handler403 = 'main.views.error_403'
# handler500 = 'main.views.error_500'

