from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', include('chat.apps.chat.urls')),

    path('admin/', admin.site.urls),

    path('auth/', include('chat.apps.myauth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('docs/', include_docs_urls(title='My Api doc'))
]

