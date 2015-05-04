from queue import Queue 

def hot_potatoe(namelist, num):
	simqueue = Queue()
	
	# metemos los nombres al queue
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()
