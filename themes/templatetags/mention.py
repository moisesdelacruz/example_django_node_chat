from django import template
import re

username_re = re.compile(r'@([A-Za-z0-9_]+)')


register = template.Library()

@register.filter('mention')
def mention(value):
    return username_re.sub(lambda m: '<a href="/%s">%s</a>' % (m.group(0), m.group(0)), value)
