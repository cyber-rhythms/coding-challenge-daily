# Submission.

def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    else:
        # Allocate first $n$ customers to $n$ tills.
        tills = customers[0:n]

        # Now run through remaining and allocate accordingly.
        for customer in customers[n:]:
            shortest_time = min(tills)
            min_index = next(i for i in range(len(tills)) if tills[i] == shortest_time)
            tills[min_index] += customer

        # Take a maximum of the till durations. 
        queue_time = max(tills)
        return queue_time
    
# Code review.
# For now note the following use of min with `key=iterable.__get__item`.
# Can also use `heapq` - but finish your DSA study first then we can get there.

def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        min_index = min(range(len(tills)), key=tills.__getitem__)
        tills[min_index] += customer
    return max(tills)