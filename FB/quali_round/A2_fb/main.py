def update_above(pa_chi, chi_pa, pa, chi, dept, check_arr):
    if pa in check_arr:
        return
    check_arr.append(pa)
    if pa in chi_pa:
        for gran in chi_pa[pa]:
            # gran ofc will be in pa_chi
            dist_gran_chi = 1 + dept
            if chi in pa_chi[gran]:
                ori_dist = pa_chi[gran][chi]
                pa_chi[gran][chi] = min(dist_gran_chi, ori_dist)
            else:
                pa_chi[gran][chi] = dist_gran_chi
            update_above(pa_chi, chi_pa, gran, chi, dept + 1, check_arr)


def solution(S, K_arr):
    ht_letter_freq = {}
    ht_pa_chi = {}
    ht_chi_pa = {}
    # process and store the S first
    for s in S:
        if s in ht_letter_freq:
            ht_letter_freq[s] += 1
        else:
            ht_letter_freq[s] = 1

    # process to have the direct children and parents
    for pa_chi in K_arr:
        pa = pa_chi[0]
        chi = pa_chi[1]

        # this will store only parents not further
        if chi in ht_chi_pa:
            ht_chi_pa[chi].append(pa)
        else:
            ht_chi_pa[chi] = [pa]

        # update pa in ht_pa_chi
        if pa in ht_pa_chi:
            ht_pa_chi[pa][chi] = 1
        else:
            ht_pa_chi[pa] = {pa: 0, chi: 1}

    # print(ht_letter_freq)
    # print("pa-chi", ht_pa_chi)
    # print("chi-pa", ht_chi_pa)

    # update for further children
    for pa_chi in K_arr:
        pa = pa_chi[0]
        chi = pa_chi[1]

        # check for grandparents
        update_above(ht_pa_chi, ht_chi_pa, pa, chi, 1, [chi])

        # check for grandchildren
        if chi in ht_pa_chi:
            for nep in ht_pa_chi[chi]:
                dist_pa_nep = ht_pa_chi[chi][nep] + 1
                if nep in ht_pa_chi[pa]:
                    ori_dist = ht_pa_chi[pa][nep]
                    ht_pa_chi[pa][nep] = min(dist_pa_nep, ori_dist)
                else:
                    ht_pa_chi[pa][nep] = dist_pa_nep

    # print(ht_letter_freq)
    # print(ht_pa_chi)
    # print(ht_chi_pa)

    # get possible nodes that all letter can turn to
    possible_node = None
    for letter in ht_letter_freq:
        ls_connect_nodes = list(ht_pa_chi[letter]) if letter in ht_pa_chi else [letter]
        # print(ls_connect_nodes)
        possible_node = list(set(possible_node) & set(ls_connect_nodes)) if possible_node else ls_connect_nodes
        if not possible_node:
            return -1

    # compute the final result
    result = None
    for node in possible_node:
        check = 0
        for letter in ht_letter_freq:
            if letter in ht_pa_chi:
                check += ht_letter_freq[letter] * ht_pa_chi[letter][node]
        if result is None or check < result:
            result = check
    return result


if __name__ == "__main__":
    # Process the input file
    f = open("consistency_chapter_2_validation_input.txt", "r")
    num_birthday = int(f.readline())
    ls_cases = []
    for i in range(num_birthday):
        S = str(f.readline())[:-1]
        num_K = int(f.readline())
        K_arr = []
        for j in range(num_K):
            K_arr.append(str(f.readline())[:-1])
        K_arr.sort()
        ls_cases.append((S, K_arr))
    f.close()

    # run the solution to get the results
    to_save = []
    for i in range(num_birthday):
        result = solution(ls_cases[i][0], ls_cases[i][1])
        # print(i+1, result)
        to_save.append(f'Case #{i+1}: {result}')

    # save the result to a txt files with the correct format
    g = open(r"A2_results.txt", "w+")
    for L in to_save:
        g.write(L + "\n")
