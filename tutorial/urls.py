from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from quickstart.views import AccountListView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'accounts', views.AccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^acc_list/(?P<q>.+)/$', AccountListView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

