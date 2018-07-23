from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (SpreadSheet1, SpreadSheet2, SpreadSheet3, SpreadSheet4, SpreadSheet5, SpreadSheet6, SpreadSheet7,
                     SpreadSheet8, SpreadSheet9, SpreadSheet10, SpreadSheet11, SpreadSheet12, SpreadSheet13,
                     SpreadSheet14, SpreadSheet15, SpreadSheet16,
                     SpreadSheet17, SpreadSheet18, SpreadSheet19, SpreadSheet20,
                     )
from import_export import resources


class SpreadSheetResource(resources.ModelResource):
    class Meta:
        model = SpreadSheet1
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand', 'date')


# Register your models here.
@admin.register(SpreadSheet1)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheetResource


class SpreadSheet2Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet2
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet2)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet2Resource


class SpreadSheet3Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet3
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet3)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet3Resource


class SpreadSheet4Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet4
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet4)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet4Resource


class SpreadSheet5Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet5
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet5)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet5Resource


class SpreadSheet6Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet6
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet6)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet6Resource


class SpreadSheet7Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet7
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet7)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet7Resource


class SpreadSheet8Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet8
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet8)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet8Resource


class SpreadSheet9Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet9
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet9)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet9Resource


class SpreadSheet10Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet10
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet10)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet10Resource


class SpreadSheet11Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet11
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet11)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet11Resource


class SpreadSheet12Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet12
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet12)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet12Resource


class SpreadSheet13Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet13
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet13)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet13Resource


class SpreadSheet14Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet14
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet14)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet14Resource


class SpreadSheet15Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet15
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet15)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet15Resource


class SpreadSheet16Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet16
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet16)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet16Resource


class SpreadSheet17Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet17
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet17)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet17Resource


class SpreadSheet18Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet18
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet18)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet18Resource


class SpreadSheet19Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet19
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet19)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet19Resource


class SpreadSheet20Resource(resources.ModelResource):
    class Meta:
        model = SpreadSheet20
        skip_unchanged = True
        report_unchanged = True
        exclude = ('id',)
        import_id_fields = ('consumed', 'spread', 'percentage_of_available_funds', 'rand_loan_amount', 'rand_term',
                            'rand_rate', 'btc_usd_price', 'eth_usd_price', 'btc_eth_price', 'demand')


# Register your models here.
@admin.register(SpreadSheet20)
class SpreadSheet1Admin(ImportExportModelAdmin):
    resource_class = SpreadSheet20Resource

# @admin.register(SpreadSheet1)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass


# @admin.register(SpreadSheet2)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet3)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet4)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet5)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet6)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet7)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet8)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet9)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet10)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet11)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet12)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet13)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet14)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet15)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet16)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet17)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet18)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet19)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
#
#
# @admin.register(SpreadSheet20)
# class SpreadsheetAdmin(ImportExportModelAdmin):
#    pass
