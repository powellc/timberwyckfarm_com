"""Templatetags for the ``calendarium`` project."""
import calendar
from django.core.urlresolvers import reverse
from django import template
from django.utils.timezone import datetime, now, timedelta, utc
from datetime import datetime as ddatetime

from ..models import Event, EventCategory

register = template.Library()


@register.filter
def get_week_URL(date, day=0):
    """
    Returns the week view URL for a given date.

    :param date: A date instance.
    :param day: Day number in a month.

    """
    if day < 1:
        day = 1
    date = datetime(year=date.year, month=date.month, day=day, tzinfo=utc)
    return reverse('calendar_week', kwargs={'year': date.isocalendar()[0],
                                            'week': date.isocalendar()[1]})


def _get_upcoming_events(amount=5, category=None, month=None):
    if not isinstance(category, EventCategory):
        category = None
    if month:
        last_day = calendar.monthrange(now().year, month)[1]
        cutin = datetime(now().year, month, 1, tzinfo=utc)
        cutoff = datetime(now().year, month, last_day, 12, 0, tzinfo=utc)
    else:
        cutin = datetime(now().year, month, 1, tzinfo=utc)
        cutoff = now() + timedelta(days=356)
    events = Event.objects.get_occurrences(
        cutin, cutoff, category)
    return events[:amount]


@register.inclusion_tag('calendarium/upcoming_events.html')
def render_upcoming_events(event_amount=5, month=None, category=None):
    """Template tag to render a list of upcoming events."""
    return {
        'occurrences': _get_upcoming_events(
            amount=event_amount, month=month, category=category),
    }


@register.assignment_tag
def get_upcoming_events(amount=5, month=None, category=None):
    """Returns a list of upcoming events."""
    return _get_upcoming_events(amount=amount, category=category)
