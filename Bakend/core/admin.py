from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

admin.site.site_header = 'CovidArmour'


# Register your models here.
class ContactUSAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')
    list_display_links = ('name', 'email', 'phone', 'subject')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    list_max_show_all = 100


admin.site.register(models.ContactUs, ContactUSAdmin)


class EnquiryAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'pincode', 'subject', 'membership')
    list_display_links = ('name', 'email', 'phone', 'subject')
    list_filter = ('membership', 'pincode', 'name')
    search_fields = ('name', 'email', 'phone', 'subject', 'message', 'pincode', 'state', "city")
    list_max_show_all = 100


admin.site.register(models.Enquiry, EnquiryAdmin)


class FranchiseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('name_of_firm', 'name_of_contact_person', 'email', 'phone', 'pincode')
    list_display_links = ('name_of_firm', 'name_of_contact_person', 'email', 'phone')
    list_filter = ('membership', 'pincode')
    search_fields = ('name', 'email', 'phone', 'subject', 'message', 'pincode', 'state', "city")
    list_max_show_all = 100


admin.site.register(models.Franchise, FranchiseAdmin)
