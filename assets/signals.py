from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver  
from user.models import User
from assets.models import Wallet, Expense


@receiver(post_save, sender=User) 
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(name=instance)

@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()


@receiver(pre_save, sender=Expense) 
def create_expense(sender, instance, **kwargs):
    if instance.pk is not None:
        wallet = Wallet.objects.get(name=instance.spender.id)
        wallet.balance = wallet.balance - instance.amount
        wallet.save()
