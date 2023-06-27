# Maeve K. Kennedy
# Jun 26 2023
# this took litterally 30 mins

from typing import List


def getuserinfo() -> dict[str, str]:
    userinfo = {
        "PlainText": "",
        "Key": "",
        "Path to Polybius Square": ""
    }
    for item in userinfo.keys():
        userinput: str = input("Please input the %s" % item)
        userinfo[item] = userinput.upper().replace(' ', '')
    return userinfo



def readsquare(squarepath) -> list[str]:
    square: list[str] = []
    print(f'reading: {squarepath}')
    with open(squarepath, encoding="utf-8") as file:
        for line in file:
            tmp: str = line.upper().replace("\n", "").replace(' ', '')
            # cleanup in case of sloppy users
            square.append(tmp)
        file.close()
    return square


def getnum(square: list[str], char: str) -> int:
    i: int = -1
    j: int = -1
    for line in square:
        i += 1
        j = line.find(char)
        if j != -1:
            break
    if j != -1:
        return int(str(i+1) + str(j+1))


def getallnums(square: list[str], plaintext: str) -> list[int]:
    out: list[int] = []
    for char in plaintext:
        num: int = getnum(square, char)
        out.append(num)
    return out

def customVecAdder(pt: list[int], key: list[int]) -> list[int]:
    out: list[int] = []
    while len(key) < len(pt):
        key += key
    for i in range(0, len(pt)):
        out.append(pt[i]+key[i])
    return out


if __name__ == '__main__':
    info: dict[str, str] = getuserinfo()
    polybius: list[str] = readsquare(info["Path to Polybius Square"])
    ptnums = getallnums(polybius, info["PlainText"])
    keynums = getallnums(polybius, info["Key"])
    cryptictext = customVecAdder(ptnums, keynums)

    print(cryptictext)

