from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user_test.urls')),
    url(r'^accounts/', include('user_test.urls'))


]
