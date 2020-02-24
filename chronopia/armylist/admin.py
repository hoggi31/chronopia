# encoding: utf-8
from django.contrib import admin
import armylist.signals

from armylist.models import Unit,Attack,spell,Competence,Army,Army_Party,TroupUnit,TroupSpell,Party,Clan
from django.contrib.auth.models import User

class AttackInline(admin.StackedInline):
    model           = Attack

class CompetenceInline(admin.StackedInline):
   model           = Competence   
    
class spellInline(admin.TabularInline):
    model = spell
    extra = 2 # how many rows to show

class unitInline(admin.TabularInline):
    model = Unit
    extra = 2 # how many rows to show

class ArmyAdmin(admin.ModelAdmin):
    inlines = (spellInline, unitInline)

class UserInline(admin.StackedInline):
    model = User

class Army_Party_inline(admin.StackedInline):
    model = Army_Party

class CompetenceAdmin(admin.ModelAdmin):
    model=Competence
    list_filter = ('name',)  
    
    
# Register your models here.
admin.site.register(Attack)
admin.site.register(Party)
admin.site.register(spell)
admin.site.register(Competence,CompetenceAdmin)
admin.site.register(Unit)
admin.site.register(Army, ArmyAdmin)
admin.site.register(Army_Party)
admin.site.register(TroupUnit)
admin.site.register(TroupSpell)
admin.site.register(Clan)

# Register your models here.
