class Word:
    def __init__(self):
        self.wordbook = {}
    
    def add(self, ed, ko):
        self.wordbook.update({ed: ko})

    def delete(self, en):
        if en in self.wordbook:
            self.wordbook.pop(en)
            return True 
        else:
            return False

    def print(self): # 메서드는 무조건 셀프
        for en, ko in self.wordbook.items(): # 아이템즈 키랑 벨류 둘다 뽑아
            print('{}: {}'.format(en,ko))

if __name__ = "__main__":
    mybook = word()
    mybook.add()
    mybook.print()
    print(mybook.delete()) # 리턴을 통해 프린트에 넣는 것