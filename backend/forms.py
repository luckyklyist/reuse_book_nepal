from dataclasses import field
from django.forms import ModelForm
from .models import product, proflie_users


class upload_book(ModelForm):
    class Meta:
        model = product
        fields = ["price",
                  "product_name",
                  "img",
                  "description",
                  "slug"]


class profile_form(ModelForm):
    class Meta:
        model = proflie_users
        fields = ["phone_no",
                  "profile_pic",
                  "location",
                  "age",
                  "gender"]
