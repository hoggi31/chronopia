"""chronopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from armylist import viewsets as army_views

router = routers.DefaultRouter(schema_title='API')

router.register(r'Army', army_views.ArmyViewSet, r'Army')
router.register(r'Unit', army_views.UnitViewSet, r'Units')


router.register(r'ArmyParty', army_views.ArmyPartyViewSet, r'ArmyParty')
router.register(r'Party', army_views.PartyViewSet, r'Party')
router.register(r'ArmyPartyDisplay', army_views.ArmyPartyViewSet2, r'ArmyPartyDisplay')

router.register(r'troupes',army_views.TroupeViewSet, r'troupes') 
router.register(r'spells',army_views.TroupSpellViewSet, r'spells') 
router.register(r'users',army_views.userViewSet, r'users') 
router.register(r'spellsf',army_views.SpellViewSet, r'spellsf') 
router.register(r'Comp',army_views.CompViewSet, r'Comp') 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^api/v1/', include(router.urls)),
]

if settings.DEBUG:
  urlpatterns += [url(r'^armylist/', include('armylist.urls', namespace='armylist'))]
  urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))