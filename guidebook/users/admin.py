from django.contrib import admin
from users.models import Main, Firstname, Surname, Patronymic, Street


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'surname', 'patronymic')


@admin.register(Firstname)
class MainAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Surname)
class MainAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Patronymic)
class MainAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Street)
class MainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
