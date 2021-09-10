def solution(caves, tunnels):
	print(caves, tunnels)
	return 0

if __name__ == "__main__":
    # Process the input file
    f = open("gold_mine_chapter_1_sample_input.txt", "r")
    num_mines = int(f.readline())
    ls_cases = []
    for i in range(num_cases):
        N = int(f.readline())
        caves = map(int, f.readline().rstrip().split())
		tunnels = []
        for j in range(N-1):
			raw = map(int, f.readline().rstrip().split)
			tunnels.append(raw)
        ls_cases.append((caves, tunnels))
    f.close()

    # run the solution to get the results
    to_save = []
    for i in range(num_mines):
		result = solution(ls_cases[i][0], ls_cases[i][1])
        to_save.append(f'Case #{i+1}: {result}')

    print(to_save)

    # save the result to a txt files with the correct format
    g = open(r"C_results.txt", "w+")
    for L in to_save:
        g.write(L + "\n")
