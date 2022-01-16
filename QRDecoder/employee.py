class Employee:
    def __init__(self,name,number,department):
        self.__name = name
        self.__number= number
        self.__department=department
    #-----------------------
    def set_name(self,name):
        self.__name=name
    def set_number(self,number):
        self.__number=number
    def set_department (self, department):
        self.__department=department
    #-----------------------
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    def get_department(self):
        return self.__department
    

    