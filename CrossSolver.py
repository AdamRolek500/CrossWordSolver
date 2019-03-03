"""

"""

from termcolor import colored


class Letter:
    letter = ''
    match_count = 0

    def __init__(self, letter):
        self.letter = letter

    def add_match_count(self):
        self.match_count += 1


def check_rows(matrix, word):
    row = ""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            row += matrix[x][y].letter
            if word in row:
                print("Word Found!")
                start_index = row.find(word)
                for index in range(len(word)):
                    matrix[x][start_index + index].add_match_count()
                return
            if word[::-1] in row:
                print("Word Found!")
                start_index = row.find(word)
                for index in range(len(word)):
                    matrix[x][start_index - index].add_match_count()
                return
        row = ""


def check_cols(matrix, word):
    col = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            col += matrix[x][y].letter
            if word in col:
                print("Word Found!")
                start_index = col.find(word)
                for index in range(len(word)):
                    matrix[start_index + index][y].add_match_count()
                return
            if word[::-1] in col:
                print("Word Found!")
                start_index = col.find(word)
                for index in range(len(word)):
                    matrix[start_index - index][y].add_match_count()
                return
        col = ""


def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y].match_count == 0:
                print(matrix[x][y].letter, end="")
            else:
                if matrix[x][y].match_count == 1:
                    print(colored(matrix[x][y].letter, "red"), end="")
                elif matrix[x][y].match_count == 2:
                    print(colored(matrix[x][y].letter, "blue"), end="")
                else:
                    print(colored(matrix[x][y].letter, "yellow"), end="")
        print()


def main():
    words = ["edg", "cgc", "bcd"]
    matrix = [[Letter('a'), Letter('a'), Letter('a'), Letter('a'), Letter('a')],
              [Letter('b'), Letter('b'), Letter('b'), Letter('b'), Letter('b')],
              [Letter('c'), Letter('c'), Letter('c'), Letter('g'), Letter('c')],
              [Letter('d'), Letter('d'), Letter('d'), Letter('d'), Letter('d')],
              [Letter('e'), Letter('e'), Letter('e'), Letter('e'), Letter('e')]]
    for word in words:
        check_rows(matrix, word)
        check_cols(matrix, word)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
