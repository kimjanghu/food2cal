from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import permissions

from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

# schema_url_patterns = [ path('', include('posts.urls')), ] 
schema_view = get_schema_view( 
    openapi.Info( 
        title="Django API", 
        default_version='v1', 
        terms_of_service="https://www.google.com/policies/terms/", 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('users/signup/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),

    path('posts/', include('posts.urls')),
    path('diets/', include('diets.urls')),
    path('predict/', include('ai.urls')),
    # swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)