import random

#print(dir(random))
pick=random.choice(range(10))
pick=random.choice([1,2,3,4,5])
print(pick)

#help
#help(random.sample)

pic=random.sample(range(10),3)

import mymath

print(mymath.PI)
print(mymath.sum(3,4))