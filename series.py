def get_num(num):
	if num == 1:
		return "2"
	elif num == 2:
		return "12"
	if num%2 == 0:
		middle = "2"
	else:
		middle = "1"
	return get_num(num - 1)[1:][::-1] + middle + get_num(num - 1)[:-1][::-1]

