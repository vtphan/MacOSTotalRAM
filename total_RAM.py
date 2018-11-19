'''
This computes the total amount of RAM of all programs being run on a MacOS system.
This is not the same as "memory usage", displayed by Activity Monitor.
Due to memory compression, memory usage is always less than the system memory.
Memory usage is, therefore, not the total of RAM of all programs being run.
'''
import subprocess

command = ['top', '-o', 'mem', '-stats', 'mem,command', '-i', '5']
t = 1

print('Gathering mem info...')
with open('mem.txt', 'w') as output:
	try:
		subprocess.run(command, timeout=t, stdout=output)
	except subprocess.TimeoutExpired:
		pass
	except:
		print('Error executing command.')

print('Analyzing mem info...')
with open('mem.txt') as input:
	for line in input:
		if line.startswith('MEM'):
			break
	total, count = 0, 0
	oneK = 1024
	oneM = oneK * 1024
	oneG = oneM * 1024
	for line in input:
		mem, command = line.strip().split(' ', 1)
		mem = mem.strip('\n\t +-')
		if mem.endswith('G'):
			m = int(mem[:-1]) * oneG
		elif mem.endswith('M'):
			m = int(mem[:-1]) * oneM
		elif mem.endswith('K'):
			m = int(mem[:-1]) * oneK
		elif mem.endswith('B'):
			m = int(mem[:-1])
		else:
			m = int(mem)
		total += m
		command = command.strip() + ' ' * 20
		count += 1
		print('{}\t{}\t{}\t{}G'.format(command[:20], m, mem, round(total/oneG,2)))
	print('There are', count, 'programs running.')
	print('Total memory usage: {}G'.format(round(total/oneG,2)))

