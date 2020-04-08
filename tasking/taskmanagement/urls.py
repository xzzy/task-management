from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth import logout

#from ledger.accounts.views import logout 
#from ledger.urls import urlpatterns as ledger_patterns
from taskmanagement import views
from taskmanagement import api

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login', kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout, name='logout'),
#    url(r'^', include('applications.urls')),
#    url(r'^', include('approvals.urls')),
#    url(r'^', include('public.urls')),
    url(r'^new-task', views.NewTask.as_view(),  name='new_task'),
    url(r'^view-task/(?P<pk>[0-9]+)/$', views.ViewTask.as_view(),  name='view_task'),
    url(r'^api/search-pg/', api.search_pg, name='search_pg'),
#    url(r'^ledger/', include('ledger.accounts.urls', namespace='accounts')),
#    url(r'^ledger/', include('social_django.urls', namespace='social')),
    #url(r'^', include('approvals.urls'))
]

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

