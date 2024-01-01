faces = [1, 2, 3, 4, 5, 6]
total = len(faces) ** 2
print("Total Combinations:", total)
combinations = [(i, j) for i in faces for j in faces]
print("\nCombinations Distribution:")
for i in range(0, total, len(faces)):
    print(combinations[i:i + len(faces)])

print("\nProbability of Sums:")
for i in range(2, 13):
    count = sum(1 for face in combinations if sum(face) == i)
    probability = count / total
    print(f"P(Sum = {i}): {count}/{total} = {probability:.2f}")
    
