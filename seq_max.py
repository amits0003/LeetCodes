# # Given prerequisites
# a0 = 0
# N, M = 10, 5
# restrictions = [(2, 0), (4, 6), (7, 0), (9, 0), (3, 2)]
#
# # Initialize the sequence with a0
# sequence = [a0]
#
# # Generate the sequence based on restrictions
# for i in range(1, N):
#     possible_values = [j for j in range(1, i + 2) if all(sequence[i - j] <= limit for _, limit in restrictions[:j])]
#     sequence.append(max(possible_values))
#
# # Find the maximum number in the sequence
# max_number = max(sequence)
#
# # Print the sequence and the maximum number
# print("Generated Sequence:", sequence)
# print("Maximum Number:", max_number)
def find_maximum(N, M_values):
    sequence = [0]
    for i in range(1, N):
        max_val = min(M_values[i - 1], sequence[i - 1] + 1)
        sequence.append(max_val)

    return max(sequence), sequence

# Example usage:
N = 10
M_values = [1, 3 ,4 , 5]
result, seq = find_maximum(N, M_values)
print("Maximum value in the sequence:", result)
print("sequnece : ", seq)
