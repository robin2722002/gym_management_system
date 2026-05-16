# from django.contrib import admin
# from .models import User

# admin.site.register(User)


# from django.contrib import admin
# from .models import User

# class UserAdmin(admin.ModelAdmin):

#     def save_model(self, request, obj, form, change):
#         if not change:  # new user create
#             obj.set_password(obj.password)
#         super().save_model(request, obj, form, change)

# admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {
            'fields': ('name','phone','weight','joining_date','profile_photo','role')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {
            'fields': ('name','phone','weight','joining_date','profile_photo','role')
        }),
    )


admin.site.register(User, CustomUserAdmin)