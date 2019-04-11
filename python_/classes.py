######## slot instead __dict__ ################################

class slot:
    __slots__ = ['a', 'b']
    c = 10


from functools import wraps
############# decorator class ############################################

def wrap_decor_class(cls):

    @wraps(cls)
    def decor_class(arg):
        print(cls.func(arg))

    cls.func = lambda p:  p**2
    return decor_class

@wrap_decor_class
class somthing_do:
    """'DOcument'"""
    pass


############# decorator initial ############################



class decor:
    def __init__(self, arg):
        print(arg)

    def __call__(self, *args, **kwargs):
        print(args)
        return self

@decor('Somthing')
class check:
    pass

###################   my super() ########################3
from functools import partial

class Proxy:
    def __init__(self, cls, obj):
        self._cls = cls
        self._obj = obj

    def __getattr__(self, item):
        func = getattr(self._cls, item)
        return partial(func, self._obj)


# Косяк, не смотрю на присутствие функции в классе
def _super(cls, obj):
    mro = obj.__class__.mro()
    next = mro[mro.index(cls) + 1]
    return Proxy(next, obj)



################## descriptor ##################
print('-' * 100)

class non_data_descriptor:
    def __init__(self, f):
        pass

    def __get__(self, instance, owner):
        print('Non_data')


class data_descriptor:
    def __init__(self, f):
        print(f, 'data_descr')

    def __get__(self, instance, value):
        print('GET')
        return 'OKe'

    def __set__(self, instance, value):
        print('SET')
        print(instance, value)

    def __del__(self):
        pass

class test_descriptor:

    def __init__(self):
        self.a = 12
        self.get = 'I not will be rewrite'
        print(self.__dict__)
        self.get2 = 'I will be rewrite'
        print(self.__dict__)

    @data_descriptor # have __get__ and __set__ return class.__dict__[*].__get__(in, cl)
    def get(self):
        pass

    @non_data_descriptor # only have __get__ return instance.__dict__[*]
    def get2(self):
        pass

print('--' * 100)
instance = test_descriptor()
print(instance.get)
print(instance.get2)
print(test_descriptor.__dict__)
print('d--' * 100)


class property_:
    def __init__(self, send=None, add=None, delete=None):
        self.d = delete
        self.a = add
        self.s = send

    def send(self, method):
        self.s = method
        return self

    def add(self, method):
        print(self, method)
        self.a = method
        return self

    def delete(self, method):
        self.d = method
        return self

    def __del__(self):
        pass

    def __get__(self, instance, class_):
        print(self.a)
        return self.a(instance, class_)


    def __set__(self, instance, value):
        print(instance, value, '___')
        self.s(instance, value)


class test:

    @property_   #test.__dict__['get']# property_ object # has __get__
    def get(self, ):
        return 'Somthing'

    @get.add
    def get(self, value):
        print('ADD WORK', value)

    @get.send
    def get(self, value):
        print('SEND WORK', value)

i = test()
i.get = 10
i.get
print('!')
print(test.__dict__, '!')
print(type(test).__dict__)
##################### Meta// class##################################



"""
error              OK
M     M          M 
\     /         /  \ 
 K   K         M    K
  \ /         /    /
   K         K--  K        
"""

########### error #############################
# class Meta1(type):
#     pass
#
# class Meta2(type):
#     pass
#
#
# class test1(metaclass=Meta1):
#     pass
#
# class test2(metaclass=Meta2):
#     pass
#
#
# class Check(test1, test2):
#     pass

###  OK ###################
class Meta1(type):
    pass

class Meta2(Meta1):
    pass


class test1(metaclass=Meta1):
    pass

class test2(metaclass=Meta2):
    pass


class Check(test2, test1):
    pass


#####################################


class MetaType(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {}

    def __new__(mcls, name, bases, attrs, **kwargs):
        print(kwargs['foo'])
        print('args from namespace class',attrs)
        print(mcls)
        cls = super().__new__(mcls, name, bases, attrs)
        print(cls.__dict__)
        return cls

    def __call__(cls, *args, **kwargs):
        instance = cls.__new__(cls, *args, **kwargs)
        if isinstance(instance, cls):
            instance.__init__(*args, **kwargs)
        return instance

class ClassType(metaclass=MetaType, foo=1):
    a = 10
    b = 20
    c = 30

    def namespace(self):
        pass
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, *args, **kwargs):
        pass

d = ClassType()
##################################################################

class FieldDescript:
    def __set_name__(self, owner, name): #set name дескриптору
        print(name)
        self.name = name
        self.value = ''

    def __set__(self, instance, value):
        self.value = value
        print('__set__')
        return self

    def __get__(self, instance, owner):
        return self.value

class test:
    desript_field = FieldDescript()

    def __setattr__(self, key, value):
        print(key, value, 'Setattr')
        super().__setattr__(key, value)

ins = test()
ins.desript_field = 'I NAME DESCRIPT'
print(ins.desript_field, '--')
print()
########################################################################

class Init_sub:  # call перед созданием класса наследника
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.attribut = 32
        for i in cls.__dict__:
            print(i)
            if i == 'attribut':
                print(i)
            #assert i.lower() in 'abc'
            pass



class Test_init(Init_sub):
    a = 1
    b = 2
    c = 3





