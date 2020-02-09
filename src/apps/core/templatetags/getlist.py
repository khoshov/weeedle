from django import template

register = template.Library()


@register.filter(name="getlist")
def getlist(request_dictionary, key):
    return request_dictionary.getlist(key) if request_dictionary else []
