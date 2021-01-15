from django.contrib import admin

from .models import Project, Observation

admin.site.site_header = "Cabinet Admin"
admin.site.side_title = "ajout / supression / correction d'erreurs"
admin.site.index_title = "Bienvenue dans le panneau d'administration"

class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name']}),
    ('Folder Name', {'fields' : ['folderName'], 'classes': ['collapse']}),]
    inline = [ObservationInline]

#admin.site.Register(Project)
#admin.site.Register(Observation)
admin.site.register(Project, ProjectAdmin) 