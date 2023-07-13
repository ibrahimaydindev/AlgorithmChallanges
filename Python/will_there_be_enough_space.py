# Solution 1
def enough(cap, on, wait):
    return max(0, wait - (cap - on))

# Solution 2 
"""
def enough(cap, on, wait):
    # Your code here
    if cap < (on + wait):
        missed = (on + wait) - cap
        return missed 
    else:
        return 0
"""