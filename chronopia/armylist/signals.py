from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from armylist.models import Unit
import hashlib


@receiver(post_save, sender=Unit)
def calculate_MD5(sender,**kwargs):  
    if  kwargs['update_fields'] != None:
        if not "controlemd5" in kwargs['update_fields']:         
            kwargs['instance'].controlemd5 = hashlib.md5(open(kwargs['instance'].model_pic.path,'rb').read()).hexdigest()
            kwargs['instance'].save(update_fields=["controlemd5",])
# Create your tests here.
