from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter(name='addplaceholder')
def addplaceholder(field, text):
    return field.as_widget(attrs={'placeholder': text})


@register.filter(name='addattrs')
def addattrs(field, attrs):
    """
    Add multiple attributes to a field
    Usage: {{ form.field|addattrs:"class:form-control,placeholder:Enter text" }}
    """
    attrs_dict = {}
    attrs_list = attrs.split(',')

    for attr in attrs_list:
        key, value = attr.split(':')
        attrs_dict[key.strip()] = value.strip()

    return field.as_widget(attrs=attrs_dict)