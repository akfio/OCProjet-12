from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    search_fields = ('username', 'type')
    list_filter = ('type', )
    list_display = ('username', 'type')

    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )


admin.site.register(CustomUser, UserAdminConfig)
