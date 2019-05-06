from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name = 'blog'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('pages.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
