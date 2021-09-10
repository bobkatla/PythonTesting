def solution(cells):
    n = len(cells)
    min_X = None
    possible_sets = None
    # check for row cases
    for i in range(n):
        check_min_X = 0
        can_win = True
        for j in range(n):
            c = cells[i][j]
            if c == 'O' or (min_X is not None and check_min_X > min_X):
                can_win = False
                break
            elif c == '.':
                check_min_X += 1
                check_col_win = True
                for a in range(n):
                    if a != i and cells[a][j] != 'X':
                        check_col_win = False
                        break
                if check_col_win:
                    can_win = False
                    break

        if can_win:
            if min_X is None or check_min_X < min_X:
                min_X = check_min_X
                possible_sets = 1
            elif check_min_X == min_X:
                possible_sets += 1
    # check for col cases
    for i in range(n):
        check_min_X = 0
        can_win = True
        for j in range(n):
            c = cells[j][i]
            if c == 'O' or (min_X is not None and check_min_X > min_X):
                can_win = False
                break
            elif c == '.':
                check_min_X += 1
        if can_win:
            if min_X is None or check_min_X < min_X:
                min_X = check_min_X
                possible_sets = 1
            elif check_min_X == min_X:
                possible_sets += 1
    return min_X, possible_sets


if __name__ == "__main__":
    # Process the input file
    f = open("xs_and_os_validation_input.txt", "r")
    num_cases = int(f.readline())
    ls_cases = []
    for i in range(num_cases):
        N = int(f.readline())
        arr = []
        for j in range(N):
            arr.append(str(f.readline())[:-1])
        ls_cases.append(arr)
    f.close()

    # run the solution to get the results
    to_save = []
    for i in range(num_cases):
        check = solution(ls_cases[i])
        result = "Impossible"
        if check[0] is not None:
            result = f"{check[0]} {check[1]}"
        to_save.append(f'Case #{i+1}: {result}')

    print(to_save)

    # save the result to a txt files with the correct format
    g = open(r"B_results.txt", "w+")
    for L in to_save:
        g.write(L + "\n")
