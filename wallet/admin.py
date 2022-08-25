from .models import Customer
from .models import Wallet
from .models import Transaction
from .models import Reward
from .models import Receipt
from .models import Loan
from .models import Notifications
from .models import Card
from .models import Account
from .models import ThirdPartyAccount
from .models import Currency
from django.contrib import admin
class CustormerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","age","email")
    search_fields=("first_name","last_name")
class WalletAdmin(admin.ModelAdmin):
    list_display =("user_name","phone_number","user_email","account_number","account_name")
    search_fields=("user_name","phone_number")
    
class TransactionAdmin(admin.ModelAdmin):
    list_display =("transaction", Wallet,"transaction_amount")
    search_fields=("transaction",Wallet)
    
class RewardAdmin(admin.ModelAdmin):
    list_display =("points","date_of_reward","transaction_amount")
    search_fields=("transaction_amount","date_of_reward")
    
class ReceiptAdmin(admin.ModelAdmin):
    list_display =("receipt_type","receipt_date","total_amount")
    search_fields=("receipt_type","receipt_date")
    
class LoanAdmin(admin.ModelAdmin):
    list_display =("loan_id","loan_type","amount","loan_term")
    search_fields=("loan_id","loan_type")
    
class NotificationsAdmin(admin.ModelAdmin):
    list_display =("title","status","recepients")
    search_fields=("title","status","recepients")
    
class CardAdmin(admin.ModelAdmin):
    list_display =("card_number","card_name","expiry_date")
    search_fields=("card_number","card_name")

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_number","account_type","name")
    search_fields=("account_number","account_type","name")
    
class ThirdPartyAccountAdmin(admin.ModelAdmin):
    list_display =(Account,"name","transaction_cost","currency","location")
    search_fields=(Account,"name","transaction_cost","currency","location")
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display =('symbol',"amount")
    search_fields= ("symbol","amount")     
    
                              
admin.site.register(Customer,CustormerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(ThirdPartyAccount,ThirdPartyAccountAdmin)
admin.site.register(Currency,CurrencyAdmin)








