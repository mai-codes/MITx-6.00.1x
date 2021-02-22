#O(nlog(n))
def mergeSortRecurs(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSortRecurs(L[:middle])
        right = mergeSortRecurs(L[middle:])
        return merge(left, right)