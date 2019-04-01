data = []
count = 0
y = 0
z = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('read finished, there are ', len(data), 'data')

for x in data:
	y += len(x)
	z = y/len(data)
print('the average length of the data is ', z)

new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[3])
