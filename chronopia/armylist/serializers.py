# encoding: utf-8
'''
Created on 21 juil. 2016

@author: k005129
'''
from rest_framework import serializers

from armylist.models import Unit,Attack,spell,Competence,Army,Army_Party,TroupUnit,TroupSpell,Party,Clan
from django.contrib.auth.models import User

#DocumentType(Authored):
#    lettre =models.CharField(max_length=4, primary_key=True)  
#    name=models.CharField(max_length=50) 
class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class attaquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = "__all__"

class spellSerializer(serializers.ModelSerializer):
    class Meta:
        model = spell
        fields = ("id", "name", "army","cost","description","model_pic","level","action","portee","resistance")

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"

class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):
    competences = CompetenceSerializer( many=True, read_only=True)
    attaques = attaquesSerializer(many=True, read_only=True)    
    clan = ClanSerializer(many=False, read_only=True) 
    class Meta:
        model = Unit
        fields = ("id", 
                  "competences",
                    "attaques",
                    "bouclier",
                    "cost",
                    "min",
                    "max",
                    "vol",
                    "model_pic",
                    "controlemd5",
                    "name",
                    "action",
                    "mouvement",
                    "wound",
                    "magie",
                    "commandment",
                    "notes",
                    "defence",
                    "armure",
                    "force",
                    "taille",
                    "type",
                    "type2",
                    "army",
                    "clan",
                    "tir") 
        read_only_fields = ('competences','attaques','clan') 



class ArmySerializer(serializers.ModelSerializer):
    #unitList=UnitSerializer(many=True)
    #spellList=spellSerializer(many=True)
    class Meta:
       model = Army
       fields = ('id','name','unitList','spellList')  
         

       
class TroupesSerializer(serializers.ModelSerializer):
    #unit = UnitSerializer(read_only=True)
    #armyParty = ArmySerializer(read_only=True)
    class Meta:
        model = TroupUnit
        fields = ('id','unit','armyParty','count')
        
        
class TroupesSerializer2(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    armyParty = ArmySerializer(read_only=True)
    class Meta:
        model = TroupUnit
        fields = ('id','unit','armyParty','count')

class TroupSpellscompSerializer(serializers.ModelSerializer):
    spell = spellSerializer(read_only=True)
    
    class Meta:
        model = TroupSpell
        fields = ('id','spell','count')        

       
class TroupesSimpleSerializer(serializers.ModelSerializer):
    #unit = UnitSerializer(read_only=True)
    #armyParty = ArmySerializer(read_only=True)
    class Meta:
        model = TroupUnit
        fields = ('id','unit','armyParty','count')
        read_only_fields = ('id',) 

class TroupSpellsSerializer(serializers.ModelSerializer):
    #spell = spellSerializer(read_only=True)
    
    class Meta:
        model = TroupSpell
        fields = ('id','spell','armyParty','count')    
          
class ArmyPartySerializer(serializers.ModelSerializer):
    unitList = TroupesSerializer(source='TroupsParties', many=True, read_only=True )
    spellList = TroupSpellscompSerializer(source='SpellsParties', many=True, read_only=True)
    #army = ArmySerializer()
    class Meta:
       model = Army_Party
       fields = ('id','unitList','spellList','name','army','author','totalCost')   
       read_only_fields = ('id','author') 
       
       
          
class ArmyPartySerializer2(serializers.ModelSerializer):
    unitList = TroupesSerializer2(source='TroupsParties', many=True, read_only=True )
    spellList = TroupSpellscompSerializer(source='SpellsParties', many=True, read_only=True)
    #army = ArmySerializer()
    class Meta:
       model = Army_Party
       fields = ('id','unitList','spellList','name','army','author','totalCost')   
       read_only_fields = ('id','author') 
       
class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

