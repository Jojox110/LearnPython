from bisect import *

"""
NOTES: 
"""

lst = [x for x in range(1000)]

print(bisect_left(lst, 500))
print(bisect_right(lst, 500))
