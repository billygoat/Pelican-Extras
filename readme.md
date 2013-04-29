# Pelican Extras

Templates, plugins, etc. for the [Pelican Static Site Generator](http://getpelican.com).

## Templates

### atom.html

Template for a linked-list Atom feed. See [this blog post](http://newsgoat.com/2013/04/22/creating-a-linked-list-atom-feed-in-pelican/) for details on how to use it.

## Plugins

### TZAwareDate

Adds a timezone-aware datetime object (Article.date_tz) based on either the timezone that's already specified for the post or the default timezone for the site. Also, adds a UTC datetime object (Article.date_utc). This plugin is required by the atom.html template.

### Re-strftime

Rewrites Article.locale_date using the built in strftime and the default date format. Used to bypass Pelican's builtin strftime utility, which doesn't allow platform dependent modifiers.