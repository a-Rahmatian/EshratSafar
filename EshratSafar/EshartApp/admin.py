from django.contrib import admin
from EshartApp.models import travel  , passenger ,ticket,company,supporter,city,admin1,terminal
# Register your models here.
admin.site.register(ticket)
admin.site.register(company)
admin.site.register(travel)
admin.site.register(passenger)
admin.site.register(supporter)
admin.site.register(city)
admin.site.register(admin1)
admin.site.register(terminal)

