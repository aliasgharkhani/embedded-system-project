from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'module', views.ModuleLogViewSet)

urlpatterns = [
    path('', views.my),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# urlpatterns = [
#     path('', include(router.urls)),
#     # path('', views.ModuleLogViewSet.as_view(), name='index'),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

