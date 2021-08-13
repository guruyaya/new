# The python "New" Module
This little module is designed to solve one of the most annoying issues python has. Imagine you want to create a function that on of the parameters defaults to an empty list:


    >>> def no_new_func(a=[]):
	...    a.append('new')
	...    return a

    >>> no_new_func()
	['new']
	>>> no_new_func()
	['new', 'new']
	>>>

The new module is designed to solve this issue using as explicitly as possible

    >>> @NEW.parse
    ... def new_func(a=NEW.new([])):
    ...     a.append('new appended')
    ...     return a
    ...
    >>> new_func()
    ['new appended']
    >>> new_func()
    ['new appended']