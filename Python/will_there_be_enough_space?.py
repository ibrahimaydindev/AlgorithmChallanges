def enough(cap, on, wait):
    # Your code here
    if cap < (on + wait):
        missed = (on + wait) - cap
        return missed 
    else:
        return 0
