from django.contrib import admin

from .models import Bird, Cage, Breeding

admin.site.register(Bird)
admin.site.register(Cage)
admin.site.register(Breeding)
