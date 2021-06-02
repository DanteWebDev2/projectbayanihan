from django.contrib import admin
from .models import Guests, Members, Enter, Sponsor, Option, Monetary, Transaction, Inkind, Settlement
# Register your models here.
admin.site.register(Guests)
admin.site.register(Members)
admin.site.register(Enter)
admin.site.register(Sponsor)
admin.site.register(Option)
admin.site.register(Monetary)
admin.site.register(Transaction)
admin.site.register(Inkind)
admin.site.register(Settlement)
