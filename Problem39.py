#Problem39

import Problem9

l = Problem9.pythagorean_list(1, 500)
print("done")
m = []
for triple in l:
    m.append(int(triple[0] + triple[1] + triple[2]))

m.sort()
print(m)


#answer is 840 (8 times)
