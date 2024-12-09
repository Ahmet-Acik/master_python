def DistinctList(arr):
    # __define-ocg__: Initialize a dictionary to count occurrences
    varOcg = {}
    varFiltersCg = 0

    # Count occurrences of each number in the array
    for num in arr:
        if num in varOcg:
            varOcg[num] += 1
        else:
            varOcg[num] = 1

    # Calculate the number of duplicates
    for count in varOcg.values():
        if count > 1:
            varFiltersCg += count - 1

    return varFiltersCg

# keep this function call here 
try:
    input_data = map(int, raw_input().split())
except EOFError:
    input_data = [0, -2, -2, 5, 5, 5]  # Default input for testing
print DistinctList(input_data)