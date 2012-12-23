from django.contrib import admin
from models import SearchTerm

class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('ip_address','search_date')
    list_filter = ('ip_address','user','q')

admin.site.register(SearchTerm, SearchTermAdmin)