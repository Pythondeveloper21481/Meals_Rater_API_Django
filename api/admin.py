from django.contrib import admin

from .models import Perfume, Rating



class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'perfume', 'user', 'stars']
    list_filter = ['perfume', 'user']
    

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']

admin.site.register(Perfume, PerfumeAdmin)
admin.site.register(Rating, RatingAdmin)