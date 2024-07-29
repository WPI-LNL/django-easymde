from django.db.models import TextField
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from .widgets import EasyMDEEditor


class EasyMDEField(TextField):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('easymde_options', {})
        self.widget = EasyMDEEditor(
            easymde_options=options,
        )
        super(EasyMDEField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = self.widget
        return super(EasyMDEField, self).formfield(**defaults)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^easymde\.fields\.EasyMDEField"])
