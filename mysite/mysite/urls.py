from django.conf.urls import patterns, include, url
#from mysite.views import hello, current_datetime, 
#from mysite.views import current_datetime, hours_ahead
from mysite import views
from django.contrib import admin
admin.autodiscover()
from contact import views as contact_views
from books import views as books_views


urlpatterns = patterns('',
#    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^search-form/$', views.search_form),
    url(r'^search/$', books_views.search),
    url(r'^contact/$', contact_views.contact),
)