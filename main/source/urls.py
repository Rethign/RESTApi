from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RandNumCreateView, RandNumDetailsView
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
	url(r'^auth/', include('rest_framework.urls', namespace = 'rest_framework')),
#	url(r'^get-token/', obtain_auth_token),
	url(r'^randnum/$', RandNumCreateView.as_view(), name = "create"),
	url(r'^randnum/(?P<pk>[0-9]+)/$', RandNumDetailsView.as_view(), name = "details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
