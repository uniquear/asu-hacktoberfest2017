def insertion(numbers):

	for i in range(1, len(numbers)):
		key = numbers[i]

		j = i-1
		while j >= 0 and key < numbers[j]:
			# TODO: if element is greater than the key,
			if numbers[j] > key:
			# move ahead of their current position
			# TODO: decrement j

		numbers[j+1] = key

	return numbers;
