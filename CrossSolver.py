"""

"""


class Letter:
    letter = ''
    match_count = 0

    def __init__(self, letter):
        self.letter = letter

    def add_match_count(self):
        self.match_count += 1

    def get_match_count(self):
        return self.match_count


def check_rows(matrix, word):
    row = ""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            row += matrix[x][y]
            if word in row:
                print("Word Found!")
                print(row)
                return
        row = ""


def check_cols(matrix, word):
    col = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            col += matrix[x][y]
            if word in col:
                print("Word Found!")
                print(col)
                return
        col = ""


def main():
    word = "abg"
    matrix = [['a', 'a', 'a', 'a', 'a'],
              ['b', 'b', 'b', 'b', 'b'],
              ['c', 'c', 'g', 'c', 'c'],
              ['d', 'd', 'd', 'd', 'd'],
              ['e', 'e', 'e', 'e', 'e']]
    check_rows(matrix, word)
    check_cols(matrix, word)


if __name__ == "__main__":
    main()
