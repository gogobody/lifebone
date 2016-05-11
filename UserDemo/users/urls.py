from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',

    url(r'^login', 'login'),
    
    url(r'^register', 'register'),
    
    url(r'^loginVerify', 'loginVerify'),
)
