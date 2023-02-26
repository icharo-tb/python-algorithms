"""JACCARD SIMILARITY

It is mainly used to compare between two sets and calculate it's similarity ratio.

It also exists another version called Jaccard Distance, which measures the difference ratio between two sets.
"""

def jaccard_similarity(A, B):

    # This will find the common elements, that is, the intersection between the sets
    nominator = A.intersection(B)

    # We will find the union between the sets
    denominator = A.union(B)

    # Now for the ratio
    similarity_ratio = len(nominator)/len(denominator)
    
    return similarity_ratio

# TRY THE CODE
A = {1,2,5,7,92,0,1}
B = {1,1,21,7,3,2,5}

print(jaccard_similarity(A,B))