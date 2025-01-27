from django.contrib import admin
from django.contrib.auth.models import User

from.models import CustomerType


class CustomerTypeAdmin(admin.ModelAdmin):
    model = CustomerType
    list_display =('__str__','customer_type_name')
    search_fields = ('customer_type_name',)
    
    # Add filters on the admin page for better navigation
    list_filter = ('customer_type_name',)

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('customer_type_name',)  # Customize the fields shown in the edit form
        }),
    )
admin.site.register(CustomerType,CustomerTypeAdmin)