"""Count_down"""


def count_down(n):
    """Count_down"""
    count = n
    while count >= 0:
        yield count
        count -= 1


for i in count_down(10):
    print(i)