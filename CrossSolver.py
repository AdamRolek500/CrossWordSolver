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


def check_diag(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    max_slices = rows + cols - 1
    for total in range(max_slices):
        string = ""
        z1 = 0 if total < cols else total - cols + 1
        z2 = 0 if total < rows else total - rows + 1
        for j in range(total - z2, z1 - 1, -1):
            string += matrix[j][total - j].letter
            if word in string or word[::-1] in string:
                print("Word Found!")
                x = j
                y = total - j
                for z in range(len(word)):
                    matrix[x][y].add_match_count()
                    x += 1
                    y -= 1
                return
    for total in range(max_slices):
        string = ""
        z1 = 0 if total < cols else total - cols + 1
        z2 = 0 if total < rows else total - rows + 1
        for j in range(total - z2, z1 - 1, -1):
            string += matrix[rows - j - 1][total - j].letter
            if word in string or word[::-1] in string:
                print("Word Found!")
                x = rows - j - 1
                y = total - j
                for z in range(len(word)):
                    matrix[x][y].add_match_count()
                    x -= 1
                    y -= 1
                return


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
    words = ["black", "blue", "brown", "green", "orange", "pink", "red", "white", "yellow"]
    matrix = [[Letter('b'), Letter('x'), Letter('h'), Letter('p'), Letter('b'), Letter('l'), Letter('a'), Letter('c'), Letter('k')],
              [Letter('b'), Letter('g'), Letter('o'), Letter('i'), Letter('e'), Letter('f'), Letter('w'), Letter('f'), Letter('i')],
              [Letter('n'), Letter('y'), Letter('q'), Letter('n'), Letter('p'), Letter('d'), Letter('h'), Letter('a'), Letter('q')],
              [Letter('q'), Letter('g'), Letter('t'), Letter('k'), Letter('g'), Letter('r'), Letter('e'), Letter('e'), Letter('n')],
              [Letter('w'), Letter('h'), Letter('i'), Letter('t'), Letter('e'), Letter('b'), Letter('l'), Letter('u'), Letter('e')],
              [Letter('o'), Letter('r'), Letter('a'), Letter('n'), Letter('g'), Letter('e'), Letter('g'), Letter('u'), Letter('x')],
              [Letter('u'), Letter('b'), Letter('l'), Letter('y'), Letter('e'), Letter('l'), Letter('l'), Letter('o'), Letter('w')],
              [Letter('k'), Letter('x'), Letter('m'), Letter('g'), Letter('z'), Letter('p'), Letter('d'), Letter('r'), Letter('r')],
              [Letter('b'), Letter('r'), Letter('o'), Letter('w'), Letter('n'), Letter('t'), Letter('r'), Letter('e'), Letter('d')]]
    for word in words:
        check_rows(matrix, word)
        check_cols(matrix, word)
        check_diag(matrix, word)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
