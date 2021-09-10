def solution(arr):
    results = []
    for case in arr:
        # prep the loop
        max_vo, max_con, num_vo, num_con = 0, 0, 0, 0
        ls_vo = ['A', 'E', 'I', 'O', 'U']
        dict_vo = {}
        dict_con = {}
        for letter in case:
            if letter in ls_vo:
                num_vo += 1
                if letter in dict_vo:
                    dict_vo[letter] += 1
                else:
                    dict_vo[letter] = 1
                if dict_vo[letter] > max_vo:
                    max_vo = dict_vo[letter]
            else:
                num_con += 1
                if letter in dict_con:
                    dict_con[letter] += 1
                else:
                    dict_con[letter] = 1
                if dict_con[letter] > max_con:
                    max_con = dict_con[letter]
        # there are 2 cases, 1: turn to vo, 2: turn to con
        case_1 = (num_vo - max_vo)*2 + num_con
        case_2 = (num_con - max_con)*2 + num_vo
        # calculate the result
        re = 0
        if num_vo == 0:
            re = case_2 if case_2 < num_con else num_con
        elif num_con == 0:
            re = case_1 if case_1 < num_vo else num_vo
        else:
            re = case_1 if case_1 < case_2 else case_2
        results.append(re)
    return results

if __name__ == "__main__":
    f = open("consistency_chapter_1_input.txt", "r")
    num_birthday = int(f.readline())
    ls_cases = []
    for case in f:
        ls_cases.append(str(case)[:-1])
    f.close()
    results = solution(ls_cases)
    to_save = []
    for i in range(num_birthday):
        to_save.append(f'Case #{i+1}: {results[i]}')
    g = open(r"A1_results.txt", "w+")
    for L in to_save:
        g.write(L + "\n")