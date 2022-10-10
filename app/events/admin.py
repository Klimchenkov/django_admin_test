from urllib.parse import uses_relative
from django.contrib import admin

from events.models import *


class EventUserProblemTypeinline(admin.StackedInline):
    model = EventUserProblemType


@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    inlines = [EventUserProblemTypeinline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [EventUserProblemTypeinline]


@admin.register(ProblemType)
class ProblemTypeAdmin(admin.ModelAdmin):
    inlines = [EventUserProblemTypeinline]


@admin.register(EventUserProblemType)
class EventUserProblemTypeAdmin(admin.ModelAdmin):
    pass
