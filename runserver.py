# -*- coding: utf-8 -*-

from pentball import app

def load_module_recursively(module):
    import pkgutil
    for loader, name, ispkg in pkgutil.iter_modules(module.__path__):
        module_name = '%s.%s' % (module.__name__, name)
        print('loading view: %s' % module_name)
        _module = __import__(module_name, fromlist=[''])

        if ispkg:
            load_module_recursively(_module)


from pentball import views
load_module_recursively(views)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6100, threaded=True)
