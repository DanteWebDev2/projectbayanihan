from django.contrib import admin
from .models import Sponsor, Option, Monetary, Transaction, Inkind, Settlement, Fundraising, Recipient
# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Option)
admin.site.register(Monetary)
admin.site.register(Transaction)
admin.site.register(Inkind)
admin.site.register(Settlement)
admin.site.register(Fundraising)
admin.site.register(Recipient)
