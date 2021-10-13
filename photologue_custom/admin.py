from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Gallery

#from .models import GalleryExtended

class GalleryAdminForm(forms.ModelForm):
    """Replace the default description field, with one that uses a custom widget."""

    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Gallery
        exclude = ['']
#############
#class GalleryExtendedInline(admin.StackedInline):
#    model = GalleryExtended
#   can_delete = False
#############
class GalleryAdmin(GalleryAdminDefault):
    form = GalleryAdminForm
#    inlines = [GalleryExtendedInline, ]



admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)








