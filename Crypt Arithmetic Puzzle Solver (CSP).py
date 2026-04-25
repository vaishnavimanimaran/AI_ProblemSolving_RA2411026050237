import itertools

def solve_cryptarithm(puzzle):
    left, right = puzzle.split('=')
    terms = [t.strip() for t in left.split('+')]
    result = right.strip()

    letters = list(set(''.join(terms + [result])))

    if len(letters) > 10:
        print("Too many letters!")
        return

    first_letters = set(word[0] for word in terms + [result])

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[l] == 0 for l in first_letters):
            continue

        def word_to_num(word):
            return int(''.join(str(mapping[c]) for c in word))

        if sum(word_to_num(t) for t in terms) == word_to_num(result):
            print("Solution:")
            for k, v in mapping.items():
                print(k, "=", v)
            return

    print("No solution found")


puzzle = input("Enter puzzle: ")
solve_cryptarithm(puzzle)
