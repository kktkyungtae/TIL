# 파일명 변경 금지
# 아래에 클래스 Point와 Circle을 선언하세요.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    pi = 3.14  # 클래스변수

    def __init__(self, center, r):
        self.center = center  # (0,0)  =-> tuple
        self.r = r  # 3

    def get_area(self):
        return round(Circle.pi * self.r * self.r, 2)

    def get_perimeter(self):
        return 2 * Circle.pi * self.r

    def get_center(self):
        a = ()
        a = (self.center.x, self.center.y)
        return a

    def print(self):
        print(f"Circle: {(self.center.x, self.center.y)}, r: {self.r}")


# 아래의 코드는 수정하지마세요.
p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.
print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.
print()