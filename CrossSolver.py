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

    def get_match_count(self):
        return self.match_count


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
        col = ""


def print_matrix(matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y].get_match_count() != 0:
                    print(colored(matrix[x][y].letter, "red"), end="")
                else:
                    print(matrix[x][y].letter, end="")
            print()


def main():
    word = "cg"
    matrix = [[Letter('a'), Letter('a'), Letter('a'), Letter('a'), Letter('a')],
              [Letter('b'), Letter('b'), Letter('b'), Letter('b'), Letter('b')],
              [Letter('c'), Letter('c'), Letter('c'), Letter('g'), Letter('c')],
              [Letter('d'), Letter('d'), Letter('d'), Letter('d'), Letter('d')],
              [Letter('e'), Letter('e'), Letter('e'), Letter('e'), Letter('e')]]
    check_rows(matrix, word)
    check_cols(matrix, word)
    print_matrix(matrix)


if __name__ == "__main__":
    main()