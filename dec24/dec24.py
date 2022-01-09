input = open('input24.txt').readlines()
MONAD = [line.split() for line in input]

for line in MONAD:
    try:
        line[-1] = int(line[-1])
    except ValueError:
        continue
# print(MONAD)

# each block of 18 lines does: z_next = (0 if (z%26 + b) == w else 1) * ((z//a)*25 + w + c) + z//a
# we start from the end and find all possibles previous z (pz) until first block

from collections import defaultdict

A = [MONAD[4+i*18][-1] for i in range(14)]
B = [MONAD[5+i*18][-1] for i in range(14)]
C = [MONAD[15+i*18][-1] for i in range(14)]

const = list(zip(A, B, C))

levels = {}
def build_deps(i, zl):
    A,B,C = const[i]

    sols = defaultdict(list)
    for w in range(9, 0, -1):
        for z in zl:
            for a in range(A):
                pz = z * A + a
                if pz % 26 + B == w:
                    if pz // A == z:
                        sols[pz].append((w, z))

                pz = round((z - w - C) / 26 * A + a)
                if pz % 26 + B != w:
                    if pz//A * 26 + w + C == z:
                        sols[pz].append((w, z))

    if sols:
        levels[i] = sols

    if i > 0:
        build_deps(i-1, list(sols.keys()))

def solve(i, z, sol, largest):
    if i == 14:
        return ''.join(str(j) for j in sol)

    for w, nz in sorted(levels[i][z], reverse=largest):
        ans = solve(i+1, nz, (*sol, w), largest)
        if ans:
            return ans

build_deps(13, [0])

print('part one solution', solve(0, 0, (), largest=True))
print('part two solution', solve(0, 0, (), largest=False))