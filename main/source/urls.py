from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework import routers
#from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', ChoiceView, base_name='choice')
router.register(r'plan', PlanView, base_name='plan')
urlpatterns = router.urls
