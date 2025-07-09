# hybrid  same as multiple inheritance


class BaseClass:
    pass

class Derive1(BaseClass):
    pass

class Derive2(BaseClass):
    pass

class child(Derive1, Derive1):
    pass




# hierarchical same as multilevel inheritance
class BaseClass:
    pass

class Derive1(BaseClass):
    pass

class Derive2(BaseClass):
    pass

class child1(Derive1):
    pass

class child2(Derive1):
    pass

class child1(Derive2):
    pass

class child2(Derive2):
    pass