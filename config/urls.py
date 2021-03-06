
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from django.contrib.auth import views

from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    path('account/login/', views.LoginView.as_view(), name='login'),
    path('account/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]

    #url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    #url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    #url(settings.ADMIN_URL, admin.site.urls),

    # User management
    #url(r'^users/', include('daysiweb.users.urls', namespace='users')),
    #url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
