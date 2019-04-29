from pull_from_CSV import *
import itertools
test = ["1","2",3,5,4,234,534,543,54,"5245"]

gimme = iter(test)
for x in gimme:
    print(next(gimme))