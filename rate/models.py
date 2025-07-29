from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models



class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return str(self.name)

status = [
    ('Silver', 'Silver'),
    ('Gold','Gold'),
    ('Diamond','Diamond'),
    ('Elite','Elite'),
    ('Exclusive','Exclusive'),
]


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    active_deposit = models.CharField (max_length = 200, null = True, default='0')
    main_deposit = models.CharField (max_length = 200, null = True, default='0')
    added_bonus = models.CharField (max_length = 200, null = True, default='0')
    withdraw_funds = models.CharField (max_length=24, null = True, default='0.00')
    upgrade_status = models.CharField (max_length=200, null=True, choices=status, default='Silver')
    currency = models.CharField (max_length=24,  default='$')

    def __str__(self):
        return str(self.name)

class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    wallet = models.CharField (max_length = 200, null = True, default='Generating .......')

    def __str__(self):
        return str(self.name)


choices = [
    ('sweetAlert', 'click on to show'),
    ('paid','mark as paid'),
]
    
STATUS = (
    ('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'),
    )

kyc = (
    ('swal-2', 'swal-2'),
    ('swal-4', 'swal-4'),
    )

class Withdrawalert (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    alert = models.CharField (max_length=24, choices=choices, default='sweetAlert')
    status = models.CharField (max_length=200, null=True, choices=STATUS, default='You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.')
    kyc = models.CharField (max_length=24, choices=kyc, default='#swal-4')

    def __str__(self):
        return str(self.name)


choices = [
    ('sweetAlert', 'ON'),
    ('OFF','OFF'),
]
    
STATUS = (
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('KYC has not been uploaded kindly fill in your details on your kyc data table', 'KYC has not been uploaded kindly fill in your details on your kyc data table'),
    ('Dear Investor we are writing to inform you that recent transfer to our institution hasbeen subject to a Cost of Transfer C O T fee As you may be aware C O T fee are charged by intermediary banks of cover the costs of processing international transactions.', 'Dear Investor we are writing to inform you that recent transfer to our institution hasbeen subject to a Cost of Transfer C O T fee As you may be aware C O T fee are charged by intermediary banks of cover the costs of processing international transactions.'),
    ('We hope this message finds you well This is to inform you today regarding your outstanding teaching fee . As you know investing in education is one of the best decisions you can make for your future. Our teaching program is designed to provide you with the knowledge and skills necessary to succeed in your chosen field.', 'We hope this message finds you well This is to inform you today regarding your outstanding teaching fee . As you know investing in education is one of the best decisions you can make for your future. Our teaching program is designed to provide you with the knowledge and skills necessary to succeed in your chosen field.'),
    ('We regret to inform you that we are unable to confirm your recent withdrawal request at this time. Upon reviewing your request, we have discovered that your bank does not support the total amount you are attempting to withdraw from your investment account to your bank account.', 'We regret to inform you that we are unable to confirm your recent withdrawal request at this time. Upon reviewing your request, we have discovered that your bank does not support the total amount you are attempting to withdraw from your investment account to your bank account.'),
    ('Please kindly Purchase a higher signal to be able to make any withdraw due to the amount your signal is too low', 'Please kindly Purchase a higher signal to be able to make any withdraw due to the amount your signal is too low'),
    ('Payment Required for Funds Liquidation Kindly Contact Customer Care', 'Payment Required for Funds Liquidation Kindly Contact Customer Care'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    )

class Generalalert (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    alert = models.CharField (max_length=24, choices=choices, default='OFF')
    status = models.CharField (max_length=7000, null=True, choices=STATUS, default='Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info.')

    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "1991")


    def __str__(self):
        return str(self.name)


statu = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    )

class Transaction (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    time = models.DateField (auto_now=True)
    amount = models.CharField (max_length = 200, null = True)
    wallet = models.CharField (max_length = 200, null = True)
    account_name = models.CharField (max_length = 200, null = True)
    bank = models.CharField (max_length = 200, null = True)
    cashapp = models.CharField (max_length = 200, null = True)
    email = models.CharField (max_length = 200, null = True)
    gateway = models.CharField (max_length = 200, null = True)
    swift_code = models.CharField (max_length = 200, null = True)
    bank_name = models.CharField (max_length = 200, null = True)
    iban = models.CharField (max_length = 200, null = True)
    purpose = models.CharField (max_length = 200, null = True)
    bank_address = models.CharField (max_length = 200, null = True)
    account_number = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True, choices=statu, default='Pending')


    def __str__(self):
        return str(self.name)