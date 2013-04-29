"""
Re-strftime plugin for Pelican
================================

Rewrites Article.locale_date using the standard strftime call. Bypasses Pelican's
implementation, which doesn't allow platform-specific modifiers.
"""

from pelican import signals
from datetime import datetime

def rewrite_locale_date(generator):
    timeFormat = generator.settings.get('DEFAULT_DATE_FORMAT', '%A, %B %e, %Y')
    
    for article in generator.articles:
        article.locale_date = article.date.strftime(timeFormat)
	    	
	    	


def register():
    signals.article_generator_finalized.connect(rewrite_locale_date)
