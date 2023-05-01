from django.contrib import admin

# Register your models here.
from .models import UserDetails,Headphones,Keyboards,mouse,laptops,phones,watches,speakers,tvs

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Headphones)
admin.site.register(Keyboards)
admin.site.register(mouse)
admin.site.register(laptops)
admin.site.register(phones)
admin.site.register(watches)
admin.site.register(speakers)
admin.site.register(tvs)
