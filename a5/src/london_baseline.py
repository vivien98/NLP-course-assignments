# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
a = open('birth_dev.tsv','r',errors="ignore").read()
a=list(a.encode('utf-8').decode('ascii', errors='ignore').split('\n'))
count=0.0
for q in a[:-1]:
	(b1,b2) = q.split('\t')
	if b2=='London':
		count+=1.0

print(100.0*count/len(a))
