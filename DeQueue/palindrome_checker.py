from dequeue import Dequeue

def pal_checker(word):
	chardequeue = Dequeue()

	for char in word:
		chardequeue.add_rear(char)

	still_equal = True

	while chardequeue.size() > 1 and still_equal:
		first = chardequeue.remove_front()
		last = chardequeue.remove_rear()
		if first != last:
			still_equal = False

	return still_equal