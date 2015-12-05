# -*- coding: UTF-8 -*-
import inspect

# Decorators
def identify(f):
    print 'Decorator identify called.'
    return f

_functions = {}
def register(class_name):
    def _register(f):
        print 'Decorator register called.'
        global _functions
        name = class_name + '.' + f.__name__
        _functions[name] = f
        print 'Function %s is registed.' % name
        return f
    return _register


class SimpleDecorator(object):
    """
    This is my first decorator.
    """

    def __init__(self):
        super(SimpleDecorator, self).__init__()
        print 'SimpleDecorator init.'

    @identify
    def foo(self):
        print 'Foo called.'

    def test(self):
        self.foo()


class RegisterDecorator(object):
    """
    This is register Decorator.
    """
    obj = None
    def __init__(self):
        super(RegisterDecorator, self).__init__()
        print 'RegisterDecorator init.'
        self._functions = {}

    @register('RegisterDecorator')
    def foo(self):
        print 'Foo called.'

    def test(self):
        self.foo()
        pass


if __name__ == '__main__':
    print '---- Test SimpleDecorator begin. ----'
    simpleDecorator = SimpleDecorator()
    simpleDecorator.test()
    print '---- Test SimpleDecorator end. ----'

    print '---- Test RegisterDecorator begin. ----'
    registerDecorator = RegisterDecorator()
    registerDecorator.test()
    print '---- Test RegisterDecorator end. ----'
