from django.contrib import admin
from .models import User, Phone, Basket


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Basket, BasketAdmin)