from django.contrib import admin
from backend.models import product,proflie_users,Rental,ask_question,reply_ask
# Register your models here.
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

admin.site.register(Rental, RentalAdmin)
admin.site.register(product)
admin.site.register(proflie_users)
admin.site.register(ask_question)
admin.site.register(reply_ask)
