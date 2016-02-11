file = open('submission.txt')

lines = [line.rstrip('\n') for line in file]
lines = lines[1:]

print len(lines)

S = set()

for line in lines:
    tokens = line.split()
    date1 = tokens[0]
    date2 = tokens[1]
    ass_assignment = ' '.join(tokens[2:-1])
    S.add(ass_assignment)

print S
