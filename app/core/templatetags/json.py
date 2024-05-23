from django import template
from django.template.defaultfilters import stringfilter

import json

register = template.Library()


@register.filter()
@stringfilter
def json_pretty(value):

    return json.dumps(json.loads(value), indent=4, sort_keys=True)
