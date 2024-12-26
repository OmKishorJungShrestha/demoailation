#lab 16:minmax

import math

def minmax(depth, nodeindex, isMax, scores, h):
    if depth == h:
        return scores[nodeindex]
    
    if isMax:
        return max(
            minmax(depth + 1, nodeindex * 2, False, scores, h),
            minmax(depth + 1, nodeindex * 2 + 1, False, scores, h)
        )
    else:
        return min(
            minmax(depth + 1, nodeindex * 2, True, scores, h),
            minmax(depth + 1, nodeindex * 2 + 1, True, scores, h)
        )

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 2, 3]
    h = int(math.log2(len(scores)))  # Using log2 for binary trees
    result = minmax(0, 0, True, scores, h)
    print(f"The optimal value is: {result}")

