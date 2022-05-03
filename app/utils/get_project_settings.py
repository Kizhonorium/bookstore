import settings


def get_project_settings(module=settings):
    __settings: dict = dict()
    for key in dir(module):
        if key.isupper():
            __settings[key] = getattr(module, key)
    return __settings
