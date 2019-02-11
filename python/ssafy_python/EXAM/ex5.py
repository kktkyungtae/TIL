def cipher(word, n):
    result = '' #빈스트링

    n = n % 26 #26이 최대, 26 초과하면 첨으로

    for c in word:
        w = ord(c) + n #아스키 코드 번호 매기기

        # z(122)를 넘어갔을 경우,
        if w > 122:
            w = w - 26

        result += chr(w) # 숫자 w를 character로 만들어주는 chr

    return result


if __name__ == "__main__":
    print(cipher('apple', 1)) # 몇개를 이동하겠다
    print(cipher('zoo',2))