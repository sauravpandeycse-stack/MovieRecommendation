from django import template

register=template.Library()
import datetime


@register.simple_tag()
def get_date(name='get_date'):
	now=datetime.datetime.now()
	return now