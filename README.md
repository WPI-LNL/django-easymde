# A markdown editor (with preview) for Django
Use a simple markdown editor https://github.com/Ionaru/easy-markdown-editor in django forms. This project is inspired by https://github.com/sparksuite/simplemde-markdown-editor and https://github.com/douglasmiranda/django-wysiwyg-redactor/.

***Note that [SimpleMDE](https://github.com/sparksuite/simplemde-markdown-editor) is no longer in development, and has been forked to create [EasyMDE](https://github.com/Ionaru/easy-markdown-editor), which is in active development as of mid-2024.***

# Getting started
* install django-easymde
```
pip install django-easymde
```

* add 'easymde' to INSTALLED_APPS.

```python
INSTALLED_APPS = (
    # ...
    'easymde',
    # ...
)
```

# Using field in models
```python
from django.db import models
from easymde.fields import EasyMDEField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = SimpleMDEField(verbose_name=u'mardown content')
```

Note: The widget `SimpleMDEWidget` can also be used in forms on existing fields.

# EasyMDE options
EasyMDE options can be set in `settings.py`:

```python
EASYMDE_OPTIONS = {
    'placeholder': 'Type here...',
    'status': False,
    'autosave': {
        'enabled': True
    }
}
```

***For the autosave option, this plugin will generate uniqueId with python's uuid.uuid4 automatically.***

Right now, this plugin supports [EasyMDE Configurations](https://github.com/Ionaru/easy-markdown-editor#configuration), but only the static ones(no support for javascript configurations such as ```previewRender```)

# Get SimpleMDE instance from DOM

After SimpleMDE is initialized, a SimpleMDE instance can be retrieved from the DOM element:

```javascript
$('.simplemde-box')[0].EasyMDE
```
