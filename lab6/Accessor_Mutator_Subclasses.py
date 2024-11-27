class HumanBeing:
    def __init__(self, gender, name):
        self.__gender = gender
        self.__name = name
    
    def set_gender(self, new_gender):
        self.__gender = new_gender

    def get_gender(self):
        return f"{self.__gender}"

    def __str__(self):
        return f"{self.__name.upper()}'s gender is {self.__gender}"

class Boy(HumanBeing):
    def __init__(self, gender, name):
        HumanBeing.__init__(self, gender, name)
 

class Girl(HumanBeing):
    def __init__(self, gender, name):
        HumanBeing.__init__(self, gender, name)




boy_instance = Boy("Male", "Bob")
girl_instance = Girl("Female", "Mary")

print(boy_instance.__str__())
print(girl_instance.__str__())












