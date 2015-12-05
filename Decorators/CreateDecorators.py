# -*- coding: UTF-8 -*-
import functools
import inspect

# Decorators
def identify(f):
    print 'Decorator identify called.'
    return f


_functions = {}
def register1(class_name):
    def _register(f):
        """
        This is register1 doc.
        """
        print 'Decorator register1 called.'
        global _functions
        name = class_name + '.' + f.__name__
        _functions[name] = f
        print 'Function %s is registed.' % name
        def warpper(*args, **kwargs):
            """
            This is warpper doc.
            """
            f(*args, **kwargs)
        return warpper
    return _register


def register2(class_name):
    def _register(f):
        """
        This is register2 doc.
        """
        print 'Decorator register2 called.'
        global _functions
        name = class_name + '.' + f.__name__
        _functions[name] = f
        print 'Function %s is registed.' % name
        @functools.wraps(f)
        def warpper(*args, **kwargs):
            """
            This is warpper doc.
            """
            f(*args, **kwargs)
        return warpper
    return _register


def check_name(name):
    def _check_name(f):
        print 'Decorator check name called.'
        @functools.wraps(f)
        def warpper(*args, **kwargs):
            """
            This the warpper doc.
            """
            func_args = inspect.getcallargs(f, *args, **kwargs)
            args_name = inspect.getargspec(f)[0]
            args_first_name = 'unkown'
            if len(args_name) > 1:
                args_first_name = args_name[1]
            if func_args.get(args_first_name) != name :
                raise Exception('This user is not %s.' % name)
            return f(*args, **kwargs)
        return warpper
    return _check_name


class SimpleDecorator(object):
    """
    This is my first decorator test class.
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
    The decorator registed the function in golbal dict.
    """

    def __init__(self):
        super(RegisterDecorator, self).__init__()
        print 'RegisterDecorator init.'

    @register1('RegisterDecorator')
    def foo1(self):
        """
        This is the foo1 doc.
        """
        print 'Foo1 called.'

    @register2('RegisterDecorator')
    def foo2(self):
        """
        This is the foo2 doc.
        """
        print 'Foo2 called'

    def test(self):
        self.foo1()
        self.foo2()
        pass


class CheckNameDecorator(object):
    """
    This is check name Decorator.
    The Decorator is defined by functools.
    """

    def __init__(self):
        super(CheckNameDecorator, self).__init__()
        print 'CheckNameDecorator init.'


    @check_name('admin')
    def get_something(self, username, something):
        """
        This is the get_something doc.
        """
        print '% s getted %s' % (username, something)

    def test(self):
        try:
            self.get_something('admin', 'apple')
        except Exception, e:
            print 'Exception catched: ', e
        try:
            self.get_something('chenwei', 'apple')
        except Exception, e:
            print 'Exception catched: ', e


if __name__ == '__main__':
    print '---- Test SimpleDecorator begin. ----'
    simpleDecorator = SimpleDecorator()
    simpleDecorator.test()
    print '---- Test SimpleDecorator end. ----'
    print '\n'
    print '---- Test RegisterDecorator begin. ----'
    registerDecorator = RegisterDecorator()
    registerDecorator.test()
    print 'The doc of foo1 is: ', registerDecorator.foo1.__doc__
    print 'The name of foo1 is: ', registerDecorator.foo1.__name__
    print 'The doc of foo2 is: ', registerDecorator.foo2.__doc__
    print 'The name of foo2 is: ', registerDecorator.foo2.__name__
    print '---- Test RegisterDecorator end. ----'
    print '\n'
    print '---- Test CheckNameDecorator begin. ----'
    checkNameDecorator = CheckNameDecorator()
    checkNameDecorator.test()
    print 'The doc of get_something is: ', checkNameDecorator.get_something.__doc__
    print 'The name of get_something is: ', checkNameDecorator.get_something.__name__
    print '---- Test CheckNameDecorator end. ----'






