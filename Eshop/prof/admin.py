from django.contrib import admin
from .models import Profile


admin.site.site_header = 'E-shop Dashboard'
admin.site.site_title = 'Easy Shop'
admin.site.index_title = 'Admin Dashboard'

admin.site.register(Profile)
