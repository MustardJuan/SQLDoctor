from pull_from_CSV import *
import itertools
fuck = ["1","2",3,5,4,234,534,543,54,"5245"]

# for x in range(len(fuck)): 
#     if (x + 1 < len(fuck)):
#         print(fuck[x+1])


gimme = iter(fuck)
for x in gimme:
    print(next(gimme))
    