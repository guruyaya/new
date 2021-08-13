"""This Moule is designed to give a python programmer an easy way to
define a default item in a function that is a list or a dict without
creating a new instance for it

"""

import copy
import inspect

def parse(func):
    '''Decorator for a function that has a new item'''
    def inner (*args, **kwargs):
        updated_args = []
        for arg in args:
            if hasattr(arg, 'MODULE_NEW'):
                updated_args.append(arg())
            else:
                updated_args.append(arg)

        signature = inspect.signature(func)
        for i, (kw, value) in enumerate(signature.parameters.items()):
            if kw not in kwargs and i >= len(args):
                kwargs[kw] = value.default

        updated_kwargs = {}
        for kw, arg in kwargs.items():
            if hasattr(arg, 'MODULE_NEW'):
                updated_kwargs[kw] = arg()
            else:
                updated_kwargs[kw] = arg
        return func(*updated_args, **updated_kwargs)
    return inner

def new(arg):
    ''' This function makes sure a new element will be a copy of
    the original, instead of the element itself'''
    def inner():
        return copy.copy(arg)
    inner.MODULE_NEW = True
    return inner
