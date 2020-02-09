from django import template

register = template.Library()


@register.filter(name="getparam")
def getlist(request_dictionary, key):
    return request_dictionary.get(key, "")
