from django.contrib import admin
from .models import Location, Myrating, MyList

# Register your models here.
admin.site.register(Location)
admin.site.register(Myrating)
admin.site.register(MyList)