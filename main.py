# Maeve K. Kennedy
# Jun 26 2023
# this took litterally 30 mins

from typing import List


def get_user_info() -> dict[str, str]:
    userinfo: dict[str, str] = {
        "PlainText": "",
        "Key": "",
        "Path to Polybius Square": ""
    }
    for item in userinfo.keys():
        userinput: str = input("Please input the %s: " % item)
        userinfo[item] = userinput.upper().replace(' ', '')
    return userinfo


def read_square(square_path) -> list[str]:
    square: list[str] = []
    print(f'reading: {square_path}')
    with open(square_path, encoding="utf-8") as file:
        for line in file:
            tmp: str = line.upper().replace("\n", "").replace(' ', '')
            # cleanup in case of sloppy users
            square.append(tmp)
        file.close()
    return square


def get_num(square: list[str], char: str) -> int:
    i: int = -1
    j: int = -1
    for line in square:
        i += 1
        j = line.find(char)
        if j != -1:
            break
    if j != -1:
        return int(str(i + 1) + str(j + 1))


def get_all_nums(square: list[str], plaintext: str) -> list[int]:
    out: list[int] = []
    for char in plaintext:
        num: int = get_num(square, char)
        out.append(num)
    return out


def custom_vec_adder(pt: list[int], key: list[int]) -> list[int]:
    out: list[int] = []
    while len(key) < len(pt):
        key += key
    for i in range(0, len(pt)):
        out.append(pt[i] + key[i])
    return out


if __name__ == '__main__':
    info: dict[str, str] = get_user_info()
    try:
        polybius: list[str] = read_square(info["Path to Polybius Square"])
    except FileNotFoundError:
        print("File not found, Exiting...")
        exit(-1)

    print(
        custom_vec_adder(
            get_all_nums(polybius, info["PlainText"]),
            get_all_nums(polybius, info["Key"])
        )
    )

    input("Press Enter to Close...")
