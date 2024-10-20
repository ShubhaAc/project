from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_mentee', 'is_mentor')  # Fields to display in the list view
    search_fields = ('username', 'email')  # Searchable fields
    list_filter = ('is_mentee', 'is_mentor')  # Add filters for these fields

# Register the CustomUser model with the custom admin class
#admin.site.register(CustomUser, CustomUserAdmin)





