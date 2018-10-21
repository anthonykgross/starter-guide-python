
class MyClass(object):

    def __init__(self):
        # Public Attribute
        self.attribute = 'my_value'

        """
        Now, I can access to it via : 
        
        cls = MyClass()
        cls.attribute
        """

        # Private Attribute
        self.__another_attribute = 'my_second_value'

        """
        Now, I CAN'T access to it via : 

        cls = MyClass()
        cls.__another_attribute # ERROR
        """

    def set(self, *args, **kargs):
        print(args)
        print(kargs)

    def define(self, param, *args):
        print(param)
        print(args)
