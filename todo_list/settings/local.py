from settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root_join('..', 'var', 'db.sqlite3')  # noqa
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'tasks': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
