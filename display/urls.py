from django.conf.urls import patterns, url, include
from display.views import ArticleViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    # url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
