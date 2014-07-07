from django.contrib import admin
from polls.models import Poll, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question']
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]
    list_display = ('question','pub_date', 'was_published_recently')
    inlines = [ChoiceInline]



admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice, ChoiceInline)


