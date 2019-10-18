import time
import math


class Person:
    """Class Person with name and year of birth"""

    def __init__(self, full_name: str, b_year: int):
        """
        :param full_name: Name Surname - str
        :param b_year: birthday year
        Creates attributes year of birth and name.
        Year of birth should be from 1900 to 2019.
        Full name - two words with a space separator
        """
        assert 1900 < b_year < 2019, "Verified your birthday please..."
        assert len(full_name.split(' ')) == 2, "Houston we've got a problem"
        self.full_name = full_name
        self.b_year = b_year

    def __str__(self):
        return f"Class Person: {self.full_name}, Year of birth: {self.b_year} "

    def age_in(self, year=int(time.strftime('%Y'))) -> int:
        """
        :param year: get any year int
        :return: age
        The function tells how old a person now.
        """
        return year - self.b_year

    def get_name(self) -> str:
        """
        :return: str name
        returns only name
        """
        return self.full_name.split(" ")[0]

    def get_last_name(self) -> str:
        """
        :return:
        returns only last name
        """
        return self.full_name.split(" ")[1]


class Employee(Person):
    """Class Employee with experience, position and salary"""

    def __init__(self, experience: int, position: str, salary: int, full_name: str, b_year: int):
        """A person who has work experience, position and salary.
        Work experience and salary must be bigger than 0"""
        super().__init__(full_name, b_year)
        assert experience > 0 and salary > 0, "Houston we've got a problem..."
        self.experience = experience
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Class Employee: {self.full_name}, position: {self.position}, salary {self.salary}"

    def get_full_position(self) -> str:
        """
        returns position depending on work experience
        """
        if self.experience < 3:
            return f'Junior {self.position}'
        elif self.experience > 6:
            return f'Senior {self.position}'
        else:
            return f'Middle {self.position}'

    def add_salary(self, money: int):
        """
        :param money: money add int
        Adds Salary Money ;)
        """
        self.salary = self.salary + money
        return


class ITEmployee(Employee):
    """class - a person with IT skills."""

    def __init__(self, experience: int, position: str, salary: int, full_name: str, b_year: int, skill=None):
        super().__init__(experience, position, salary, full_name, b_year)
        self.skill = skill
        if self.skill is None:
            self.skill = []

    def __str__(self):
        return f'class ITEmployee, Person: {self.full_name}, with skills: {", ".join(self.skill)}'

    def add_skill(self, skill):
        """Add one skill"""
        self.skill.append(skill)

    def add_skills(self, *args):
        """add many skills"""
        self.skill = self.skill + list(args)


class Room:
    """ The class room - have two sides and an area"""

    def __init__(self, side_a: int, side_b: int):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Room with side A = {self.side_a} and side B = {self.side_b}"

    def get_area(self) -> int:
        """
        :return: room area
        """
        return self.side_a * self.side_b

    def get_perimeter(self) -> int:
        """:return room sides perimeter"""
        return (self.side_a + self.side_b) * 2


class Point:
    """Point cartesian coordinates"""

    def __init__(self, x: int, y: int):
        """get x and y int args"""
        self.x = x
        self.y = y

    def __str__(self):
        return f"I'm point with x = {self.x}, y = {self.y} "

    def point_start_distance(self) -> float:
        """
        Get the distance from the origin to the point
        """
        return math.hypot(self.x, self.y)

    @staticmethod
    def two_points_distance(point1: object, point2: object) -> float:
        """
        :param point1: object1 with x and y attr
        :param point2: object2 with x and y attr
        :return: distance from object1 and object2
        """
        x1, y1 = getattr(point1, 'x'), getattr(point1, 'y')
        x2, y2 = getattr(point2, 'x'), getattr(point2, 'y')
        return math.hypot(x2 - x1, y2 - y1)

    def convert_point_cor(self):
        """convert to sel coord"""
        return math.atan(self.y/self.x)


if __name__ == '__main__':
    b = Person('Sergey Ivanov', 1999)
    print(f'в 2030 году будет {b.age_in(2030)}')
    print(f'имя {b.get_name()}')
    print(f'фамилия {b.get_last_name()}')
    print(b)

    print('-' * 100)

    a = Employee(8, "progr", 1000, getattr(b, "full_name"), b.b_year)
    print(a.get_full_position())
    a.add_salary(10)
    print(a.salary)
    print(a)

    print('-' * 100)

    d = ITEmployee(3, "tester", 600, 'Andrey Gust', 1985, skill=['info', 'drive'])
    d.add_skills('write', 'read')
    print(d)

    print('-' * 100)

    c = Room(2, 4)
    print(c.get_area())
    print(c.get_perimeter())
    print(c)

    print('-' * 100)

    p1 = Point(4, 3)
    p2 = Point(2, 2)
    print(f"Расстояние между точками p1 и p2 {Point.two_points_distance(p1, p2)}")
    print(f"Точка p1 на расстоянии {p1.point_start_distance()} от начала координат")
    print(f"Точка p2 на расстоянии {p2.point_start_distance()} от начала координат")
    print(p1, p2, sep='\n')
    print(p1.convert_point_cor())

    print('-' * 100)


