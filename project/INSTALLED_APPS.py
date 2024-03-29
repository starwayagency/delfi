INSTALLED_APPS = [
    'filebrowser',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'django.contrib.flatpages',

    # 'crispy_forms',
    'tinymce',
    'rosetta',
    'autotranslate',
    # 'import_export',
    'core.apps.CoreConfig',
    
    # 'pages.apps.PageConfig',
    # 'content.apps.ContentConfig',
    # 'order.apps.OrderConfig',
    'boilerplate.pages.apps.PageConfig',
    'boilerplate.content.apps.ContentConfig',
    'boilerplate.order.apps.OrderConfig',
]


