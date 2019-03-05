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


def check_diag(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    max_slices = rows + cols - 1
    for total in range(max_slices):
        string= ""
        z1 = 0 if total < cols else total - cols + 1
        z2 = 0 if total < rows else total - rows + 1
        for j in range(total - z2, z1 - 1, -1):
            string+= matrix[j][total - j]
            if word in string:
                print("Word Found!")
                x = j
                y = total - j
                for z in range(len(word)):
                    matrix[x][y].add_match_counter()
                    x + +
                    y - -
    for total in range(max_slices):
        string+= ""
        z1 = 0 if total < cols else total - cols + 1
        z2 = 0 if total < rows else total - rows + 1
        for j in range(total - z2, z1 - 1, -1):
            string+= matrix[rows - j - 1][total - j]
            if word in string:
                print("Word Found!")
                x = rows - j - 1
                y = total - j
                for z in range(len(word)):
                    matrix[x][y].add_match_counter()
                    x - -
                    y - -
        print
        s


def main():
    words = ["edg", "cgc", "bcd"]
    matrix = [[Letter('a'), Letter('a'), Letter('a'), Letter('a'), Letter('a')],
              [Letter('b'), Letter('b'), Letter('b'), Letter('b'), Letter('b')],
              [Letter('c'), Letter('c'), Letter('c'), Letter('g'), Letter('c')],
              [Letter('d'), Letter('d'), Letter('d'), Letter('d'), Letter('d')],
              [Letter('e'), Letter('e'), Letter('e'), Letter('e'), Letter('e')]]
    # for word in words:
    #     check_rows(matrix, word)
    #     check_cols(matrix, word)
    check_diag(matrix, words)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
