
def simple_similarity(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().split()
        words2 = f2.read().split()

    match_count = 0
    for word in words1:
        if word in words2:
            match_count += 1

    total = len(words1)
    similarity = (match_count / total) * 100 if total > 0 else 0
    return round(similarity, 2)

if __name__ == "__main__":
    sim = simple_similarity('sample_file1.txt', 'sample_file2.txt')
    print(f"Similarity: {sim}%")
