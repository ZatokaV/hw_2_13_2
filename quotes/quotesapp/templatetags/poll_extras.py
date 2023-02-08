from collections import Counter

from django import template

from ..models import Quote

register = template.Library()

all_tags = []


@register.simple_tag
def most_popular_tags():
    tag_obj = Quote.tags
    for el in tag_obj:
        all_tags.append(el.name)
    top_tags = Counter(all_tags).most_common(10)
    print(f'{top_tags=}')
    return top_tags

