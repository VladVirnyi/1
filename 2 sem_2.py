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


class StudentInfo(MyName):
    def __init__(self, first_name=None, last_name=None, birth_year=None,
                 student_id=None, faculty=None):
        super().__init__(first_name, last_name, birth_year)

        self.student_id = student_id
        self.faculty = faculty

        self._rating_scores = [] #protected
        self.__scholarship = 0 #private

    def add_rating_score(self, score):
        if 0 <= score <= 10:
            self._rating_scores.append(score)
        else:
            raise ValueError("Оцінка має бути в межах від 0 до 10")

    def _calculate_rating(self):
        if not self._rating_scores:
            return 0

        return sum(self._rating_scores) / len(self._rating_scores)

    def calculate_scholarship(self):
        rating = self._calculate_rating()

        if rating >= 9:
            self.__scholarship = 2000
        elif rating >= 7:
            self.__scholarship = 1500
        elif rating >= 5:
            self.__scholarship = 1000
        else:
            self.__scholarship = 0

        return self.__scholarship

    def get_scholarship_details(self):
        return {
            "rating_scores": self._rating_scores,
            "average_rating": self._calculate_rating(),
            "scholarship": self.__scholarship
        }


if __name__ == "__main__":
    student = StudentInfo("Влад", "Вірний", 2008, "ST123", "Комп'ютерна інженерія")

    student.add_rating_score(9)
    student.add_rating_score(10)
    student.add_rating_score(9)

    scholarship = student.calculate_scholarship()

    details = student.get_scholarship_details()
    print(f"Оцінки: {details['rating_scores']}")
    print(f"Середній рейтинг: {details['average_rating']}")
    print(f"Сума стипендії: {details['scholarship']} грн")
