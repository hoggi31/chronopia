# encoding: utf-8
'''
Created on 23 sept. 2016

@author: ks002450
'''
from rest_framework import viewsets, filters, response
from django.contrib.auth.models import User
from armylist.models import Unit,Attack,spell,Competence,Army,Army_Party,TroupUnit,TroupSpell,Party
from armylist.serializers import UnitSerializer,CompetenceSerializer,ArmySerializer,ArmyPartySerializer,ArmyPartySerializer2,TroupesSerializer,usersSerializer,TroupSpellsSerializer,spellSerializer,TroupesSimpleSerializer,PartySerializer
from rest_framework import filters
from rest_framework.decorators import detail_route, list_route

import django_filters
from rest_framework.response import Response

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = usersSerializer 
    
    @list_route()
    def myself(self,request):
        current_user = request.user
        data = self.get_serializer(current_user).data        
        return Response(data)
    
class ProductFilter(django_filters.FilterSet):    
    #name = django_filters.CharFilter(lookup_expr='contains')
    #name = ListFilter(name='name')
    name = django_filters.CharFilter(name="name",lookup_expr="regex")
    
    class Meta:
        model = Unit

class SpellFilter(django_filters.FilterSet):    
    #name = django_filters.CharFilter(lookup_expr='contains')
    #name = ListFilter(name='name')
    name = django_filters.CharFilter(name="name",lookup_expr="regex")
    
    class Meta:
        model = spell        
        
class SpellViewSet(viewsets.ModelViewSet):
    queryset = spell.objects.all()
    serializer_class = spellSerializer
    
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = SpellFilter
    search_fields = ('name')
    
    
        
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = ProductFilter
    search_fields = ('name','magie', 'type','type2','generique')
    
    @detail_route(methods=['post'])
    def populate_xls(self, request, pk=None):
        importFile = request.data["file"];

class ArmyViewSet(viewsets.ModelViewSet):
   queryset = Army.objects.all()
   serializer_class = ArmySerializer 

class PartyFilter(django_filters.FilterSet):    
    #name = django_filters.CharFilter(lookup_expr='contains')
    #name = ListFilter(name='name')
    author = django_filters.CharFilter(name="author",)
    
    class Meta:
        model = Army_Party
        fields = {
                  'author',
                 } 

class ArmyPartyViewSet(viewsets.ModelViewSet):
   filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
   filter_class = PartyFilter
   search_fields = ('author')
    
   ordering_fields = '__all__' 
    
   queryset = Army_Party.objects.all()
   serializer_class = ArmyPartySerializer 

   def perform_create(self, serializer):
       serializer.save(author=self.request.user)
 

       
class ArmyPartyViewSet2(viewsets.ModelViewSet):
   filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
   filter_class = PartyFilter
   search_fields = ('author')
    
   ordering_fields = '__all__' 

    
   queryset = Army_Party.objects.all()
   serializer_class = ArmyPartySerializer2 

   def perform_create(self, serializer):
       serializer.save(author=self.request.user)
       
   @detail_route()
   def totalCost(self,request,pk):        
        armyParty = self.get_object()
        total, unittir, unitIndep, counttir, countinde,countunit = armyParty.gettotalCost()
        #serializer = self.get_serializer(armyParty)
        return Response({'total':total, 'totaltir':unittir, 'unitIndep':unitIndep,'counttir':counttir,'countinde':countinde,'countunit':countunit})
       
class TroupeViewSet(viewsets.ModelViewSet):
   queryset = TroupUnit.objects.all()
   serializer_class = TroupesSimpleSerializer 
   
class TroupSpellViewSet(viewsets.ModelViewSet):
   queryset = TroupSpell.objects.all()
   serializer_class = TroupSpellsSerializer   
    
class CompViewSet(viewsets.ModelViewSet):
   queryset = Competence.objects.all()
   serializer_class = CompetenceSerializer  
   
class PartyViewSet(viewsets.ModelViewSet):
   queryset = Party.objects.all()
   serializer_class = PartySerializer  
