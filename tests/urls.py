from django.conf.urls import include, url
from djohno.views import server_error


urlpatterns = (
    url(r'^djohno/', include('djohno.urls')),
    url(r'^500/', server_error, name='server_error_handler'),
)
