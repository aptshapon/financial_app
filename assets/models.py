from django.db.models import (
    OneToOneField, DateTimeField, Model, TextChoices, CASCADE, 
    CharField, DecimalField, ForeignKey, TextField,
    FileField, ImageField, PositiveIntegerField, EmailField
)
from user.models import User


class Wallet(Model):
    class Currency_Symbol(TextChoices):
        BDT = 'BDT', 'BDT'
        USD = 'USD', 'USD'

    class Money_Source(TextChoices):
        bKash = 'bKash', 'bKash'
        Nagad = 'Nagad', 'Nagad'
        Rocket = 'Rocket', 'Rocket'
        Bank = 'Bank', 'Bank Account'

    name = OneToOneField(User, on_delete=CASCADE, null=True)
    opening_date = DateTimeField(auto_now_add=True)
    currency = CharField(max_length=3, 
                        choices=Currency_Symbol.choices,
                        default=Currency_Symbol.BDT)
    source = CharField(max_length=6, 
                        choices=Money_Source.choices,
                        default=Money_Source.Bank)
    balance = DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Hello {self.name}, your balance is: {self.balance}"


class Expense(Model):

    class ExpeseType(TextChoices):
        Transportation = 'Transportation', 'Transport Bill'
        Rent = 'Rent', 'Rent'
        Breakfast  = 'Breakfast', 'Breakfast'
        Lunch = 'Lunch', 'Lunch'
        Dinner = 'Dinner', 'Dinner'
        Entertainment = 'Entertainment', 'Entertainment'
    type = CharField(max_length=14, 
                        choices=ExpeseType.choices,
                        default=ExpeseType.Transportation,
                        blank=True)
    
    class Utilities(TextChoices):
        Electric = 'Electric', 'Electric Bill'
        Water = 'Water', 'Water Bill'
        Gas = 'Gas', 'Gas Bill'
        Oil = 'Oil', 'Oil Purchase'
        Internet = 'Internet', 'Internet Bill'
        CellPhone = 'CellPhone', 'CellPhone Bill'
    utilities = CharField(max_length=10, 
                        choices=Utilities.choices,
                        default=Utilities.CellPhone,
                        blank=True)    
    spender = OneToOneField(User, on_delete=CASCADE, null=True)
    amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    voucher_no = PositiveIntegerField(blank=True, null=True)
    description = TextField(blank=True, help_text=('Reason of the expense'))
    file = FileField(blank=True)
    image = ImageField(blank=True)
    expense_date = DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Hello {self.spender}, your expense is: {self.amount}"


class Income(Model):
    amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    detail = TextField(blank=True)
    date = DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.detail


class LendMoney(Model):
    name = CharField(max_length=64)
    email = EmailField(blank=True, null=True)
    phone = PositiveIntegerField(blank=True, null=True)
    address = CharField(max_length=256)
    city = CharField(max_length=64)
    amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    money_return_in_months = PositiveIntegerField()
    description = TextField(blank=True, null=True)
    lend_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Liability(Model):
    name = CharField(max_length=64)
    email = EmailField()
    phone = PositiveIntegerField()
    address = CharField(max_length=256)
    loan_amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    description = TextField()
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
