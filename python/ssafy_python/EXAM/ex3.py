# 사각형 문제 

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)

    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2

    def is_square(self):
        # if (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y):
        #     return True
        # else:
        #     return False
        ## 걍 밑 처럼 가로 세로가 같은지 평가만 해도 가능! 위 네줄 줄이기
        return (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y)

if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3,1)
    r1 - Rectangle(p1,p2)
    print(r1.get_area())