from django.contrib import admin
from .models import Petition, Signature, Complaint

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'created_at', 'updated_at')  # Show relevant fields
    search_fields = ('title', 'description')  # Search functionality
    list_filter = ('created_by',)  # Filter by creator

class SignatureAdmin(admin.ModelAdmin):
    list_display = ('user', 'petition', 'signed_at')  # Show signatures
    search_fields = ('user__username', 'petition__title')  # Search functionality

# Register your models



class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # Columns to display in the list view
    search_fields = ('title',)  # Fields that can be searched in the admin

admin.site.register(Petition, PetitionAdmin)
admin.site.register(Signature, SignatureAdmin)
admin.site.register(Complaint, ComplaintAdmin)   
