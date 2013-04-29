"""
Time Zone Aware Date plugin for Pelican
================================

Adds a datetime object with the selected time zone and adds a datetime object with the
UTC time zone.
"""

from pelican import signals
from datetime import datetime
from dateutil import tz

def add_tz_aware_date(generator):
    timeZone = generator.settings.get('TIMEZONE', 'UTC')
    fromZone = tz.gettz(timeZone)
    toZone = tz.gettz('UTC')
    
    for article in generator.articles:
    	if article.date.tzinfo is None:
            article.date_tz = article.date.replace(tzinfo=fromZone)
        else:
            article.date_tz = article.date
        article.date_utc = article.date_tz.astimezone(toZone)
	    	
	    	


def register():
    signals.article_generator_finalized.connect(add_tz_aware_date)
