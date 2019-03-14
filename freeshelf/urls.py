"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('freeshelfapp/', include('freeshelfapp.urls')),
    path('', RedirectView.as_view(url='/freeshelfapp/', permanent=True)),
    # path('accounts/', include('django.contrib.auth.urls')),
        # authentication paths placed here in case we have multiple applications across the whole site
        # these URLs expect to find their associated templates in a directory '/registration/' somewhere in the templates search path
    path('accounts/', include('registration.backends.default.urls')),
        # URL patterns for the views in django-registration-redux
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # allows us to use CSS files in the static directory
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # allows us to use uploaded images

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
