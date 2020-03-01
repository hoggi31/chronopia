# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.dispatch import receiver
from django.contrib.auth.models import User

class Card(models.Model):
    name   = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=2000,blank=True,null=True)
    cost = models.IntegerField(blank=True,null=True)
    min = models.IntegerField(blank=True,null=True)
    max = models.IntegerField(blank=True,null=True)
    model_pic = models.ImageField(upload_to='armylist/cards',blank=True,null=True)
    
    
    controlemd5 = models.CharField(max_length=100,blank=True,null=True)
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):          
        
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
UNIT_CHOICES = (
    ('Independant','Independant'),
    ('Unite','Unite'),
    ('Invocation','Invocation'),
)

class Attack(models.Model):
    att=models.IntegerField(blank=True,null=True)
    dmg=models.IntegerField(blank=True,null=True)
    type= models.CharField(max_length=20)  
    Effets = models.TextField(blank=True,null=True)  
    portee = models.CharField(max_length=20 ,blank=True,null=True)  
    cadence = models.CharField(max_length=20,blank=True,null=True)
    units = models.ManyToManyField('Unit',related_name="attaques",blank=True,null=True )
    
    def __str__(self):
        return 'type {type}/ att{att} / dmg{dmg}'.format(type=self.type, att=self.att,dmg=self.dmg)
    
class Competence(models.Model):
    name   = models.TextField(unique=False)
    description = models.TextField(blank=True,null=True )
    dim = models.IntegerField(blank=True,null=True )
    units = models.ManyToManyField('Unit',related_name="competences",blank=True,null=True )
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name    
    
class spell(Card):    
    costSpell = models.IntegerField(blank=True,null=True) 
    level = models.IntegerField(blank=True,null=True ) 
    army = models.ForeignKey('Army',related_name="spellList",blank=True,null=True)
    action = models.IntegerField(blank=True,null=True ) 
    portee = models.CharField(max_length=50,blank=True,null=True)
    resistance = models.CharField(max_length=50,blank=True,null=True)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Clan(models.Model):
    name = models.CharField(max_length=100,unique=True)
    model_pic = models.ImageField(upload_to='armylist/cards',blank=True,null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Monture(Card):
    action = models.IntegerField(blank=True,null=True)
    mouvement = models.IntegerField(blank=True,null=True)
    vol = models.IntegerField(blank=True,null=True)	
    force = models.IntegerField(blank=True,null=True)
    CD = models.IntegerField(blank=True,null=True)
    CC = models.IntegerField(blank=True,null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Unit(Card):
    action = models.IntegerField(blank=True,null=True)
    mouvement = models.IntegerField(blank=True,null=True)
    vol = models.IntegerField(blank=True,null=True)
    army = models.ForeignKey('Army',related_name="unitList",blank=True,null=True)
    clan = models.ForeignKey('Clan',related_name="unitList",blank=True,null=True)
    generique = models.CharField(max_length=50,blank=True,null=True)
    magie = models.IntegerField(blank=True,null=True)
    wound = models.IntegerField(blank=True,null=True)
    commandment = models.IntegerField(blank=True,null=True)
    
    notes = models.CharField(max_length=1000,blank=True,null=True)
    defence = models.IntegerField(blank=True,null=True)
    bouclier = models.IntegerField(blank=True,null=True)
    armure = models.IntegerField(blank=True,null=True)
    force = models.IntegerField(blank=True,null=True)
    taille = models.IntegerField(blank=True,null=True)
    type = models.CharField(max_length=20,choices=UNIT_CHOICES,blank=True,null=True)
    type2 = models.CharField(max_length=20,blank=True,null=True)
    tir = models.BooleanField()
    monture = models.ManyToManyField(Monture,related_name='cavaliers',blank=True,null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
    
    
class Army(models.Model):
    name = models.CharField(max_length=100,unique=True)
    model_pic = models.ImageField(upload_to='armylist/cards',blank=True,null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Army_Party(models.Model):
    name = models.CharField(unique=True,max_length=40)
    unitList = models.ManyToManyField(Unit,through='TroupUnit',related_name='unitParties')
    spellList= models.ManyToManyField(spell,through='TroupSpell',related_name='spellParties')
    army = models.ForeignKey(Army, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, null=True, blank=True)
    totalCost = models.IntegerField()   
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
    def gettotalCost(self):
        total = 0
        totalTir = 0
        totalIndep = 0 
        counttir = 0
        countinde = 0
        countunit = 0		
            
        for troup in TroupUnit.objects.filter(armyParty=self.id):
            unit = Unit.objects.filter(id=troup.unit.id)
            instUnit =unit.first()
            total = total + instUnit.cost * troup.count
            if instUnit.tir:
                totalTir = totalTir+ instUnit.cost * troup.count
            
            if instUnit.type=='Independant':
                totalIndep = totalIndep + instUnit.cost * troup.count
        
        for troup in TroupSpell.objects.filter(armyParty=self.id): 
            spell1 = spell.objects.filter(id=troup.spell.id)
            instSpell = spell1.first()
            totalIndep = totalIndep+ instSpell.cost * troup.count
            total = total + instSpell.cost * troup.count
            
        
        for troup in TroupUnit.objects.filter(armyParty=self.id):  
            unit = Unit.objects.filter(id=troup.unit.id)
            countunit = countunit + 1	
            instUnit =unit.first()			
            if instUnit.tir:			
                counttir = counttir + 1
            if instUnit.type=='Independant':
                countinde = countinde + 1          
        self.totalCost =  total 
        self.save(update_fields=["totalCost"])  

        return total,totalTir,totalIndep,counttir,countinde,countunit

class Party(models.Model):
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    resume = models.TextField()
    army_list = models.ManyToManyField(Army_Party, related_name="Partys")
    joueurs = models.ManyToManyField(User , related_name="Partys")

    
class TroupUnit(models.Model):
    count = models.IntegerField();    
    unit = models.ForeignKey(Unit,related_name='unittroups')
    armyParty = models.ForeignKey(Army_Party, on_delete=models.CASCADE,related_name='TroupsParties')
    
   
class TroupSpell(models.Model):
    count = models.IntegerField();
    spell = models.ForeignKey(spell,related_name='spelltroups' )
    armyParty =  models.ForeignKey(Army_Party, on_delete=models.CASCADE,related_name='SpellsParties')
    