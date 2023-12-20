def custom_needleman_wunsch(seq1, seq2, scoring):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    custom_scores = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            match = custom_scores[i - 1][j - 1] + scoring[seq1[i - 1]][seq2[j - 1]]
            delete = custom_scores[i - 1][j] + scoring[seq1[i - 1]]['-']
            insert = custom_scores[i][j - 1] + scoring['-'][seq2[j - 1]]
            custom_scores[i][j] = max(match, delete, insert)

    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = len_seq1, len_seq2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and custom_scores[i][j] == custom_scores[i - 1][j - 1] + scoring[seq1[i - 1]][seq2[j - 1]]:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and custom_scores[i][j] == custom_scores[i - 1][j] + scoring[seq1[i - 1]]['-']:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2

# Example usage:
x = "ATGCC"
y = "TACGCA"
scoring_matrix = {
    'A': {'A': 2, 'T': -1, 'G': -2, 'C': 0, '-': -1},
    'T': {'A': -1, 'T': 2, 'G': 0, 'C': -2, '-': -1},
    'G': {'A': -2, 'T': 0, 'G': 2, 'C': -1, '-': -1},
    'C': {'A': 0, 'T': -2, 'G': -1, 'C': 2, '-': -1},
    '-': {'A': -1, 'T': -1, 'G': -1, 'C': -1, '-': 0}
}

result = custom_needleman_wunsch(x, y, scoring_matrix)
print("Alignment X:", result[0])
print("Alignment Y:", result[1])
                        