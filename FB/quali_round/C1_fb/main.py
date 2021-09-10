def max_val(ls, c, tuns):
	val = ls[c-1]
	result = val
	if tuns:
		for x in tuns:
			a = val
			if c in x:
				x.remove(c)
				nx = x.pop(0)
				r = tuns.copy()
				r.remove(x)
				a += max_val(ls, nx, r)
			if a > result: result = a
	return result

def solution(caves, tunnels):
	# find the second layer
	left_over = []
	nd_layer = []
	st = 0
	nd = 0
	if tunnels:
		for x in tunnels:
			if 1 in x:
				x.remove(1)
				nd_layer.append(x[0])
			else:
				left_over.append(x)
		for c in nd_layer:
			check = max_val(caves, c, left_over)
			if check > st:
				nd = st
				st = check
			elif check > nd:
				nd = check
	return caves[0] + st + nd
	

if __name__ == "__main__":
	# Process the input file
	f = open("gold_mine_chapter_1_input.txt", "r")
	num_mines = int(f.readline())
	ls_cases = []
	for i in range(num_mines):
		N = int(f.readline())
		caves = f.readline().rstrip().split()
		caves = [int(x) for x in caves]
		tunnels = []
		for j in range(N-1):
			raw = f.readline().rstrip().split()
			raw = [int(x) for x in raw]
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