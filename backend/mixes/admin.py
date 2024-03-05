from django.contrib import admin

from .models import (
    Company,
    Favorite,
    Flavor,
    Lines,
    Mixes,
    MixesTobacco,
    Strength,
    Tobacco
    )


class MixesTobaccoInline(admin.StackedInline):
    model = MixesTobacco
    min_num = 2


@admin.register(Lines)
class LinesAdmin(admin.ModelAdmin):
    list_display = ('company', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_lines')
    list_filter = ('name',)
    search_fields = ('name',)

    def get_lines(self, obj):
        return '\n'.join([p.name + ',' for p in obj.lines.all()])
    get_lines.short_description = 'Линейки'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'tobacco')


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Mixes)
class MixesAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'pub_date')
    list_filter = ('pub_date', 'tobaccos')
    inlines = [MixesTobaccoInline]


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Tobacco)
class TobaccoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'company',
        'tobacco_line',
        'name',
        'description',
        'strength',
        'get_flavor'
    )
    list_editable = ('name', 'company', 'tobacco_line')
    list_filter = (
        'company',
        'tobacco_line',
        'name',
        'flavor',
        'strength'
    )
    search_fields = ('name',)

    def get_flavor(self, obj):
        return '\n'.join([p.name + ',' for p in obj.flavor.all()])
    get_flavor.short_description = 'Ароматы'
