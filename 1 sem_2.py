class MyName:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_course(self):
        if self.birth_year:
            current_year = 2025
            age = current_year - self.birth_year
            course = age - 15
            return course if 1 <= course <= 6 else None
        return None

    def get_name_list(self):
        return [self.first_name, self.last_name] if self.first_name and self.last_name else []

student = MyName("Vlad", "Virnyi", 2008)
print(student.get_course())
print(student.get_name_list())
