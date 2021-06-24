from django.contrib import admin
from .models import Sponsor, Inkind, Fundraising, Recipient
# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Inkind)
admin.site.register(Fundraising)
admin.site.register(Recipient)
