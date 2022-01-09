scanners = []

with open('input19.txt') as input:
    i = 0
    lines = input.readlines()
    title = 0
    while i <= 33:
        scanner = []
        for j in range(1+title, len(lines)):
            if lines[j] != '\n':
                scanner.append([int(coord) for coord in lines[j].split(',')])
            else:
                title = j + 1
                scanners.append(scanner)
                i += 1
                break

# part one

def orientate(scanner, orientation):
    
    new_scanner = []

    for point in scanner:
        x = point[0]
        y = point[1]
        z = point[2]

        orientations = {
            0: [x, z, -y], 1: [-z, x, -y], 2: [-x, -z, -y],
            3: [z, -x, -y], 4: [z, -y, x], 5: [y, z, x],
            6: [-z, y, x], 7: [-y, -z, x], 8: [-y, x, z], 
            9: [-x, -y, z], 10: [y, -x, z], 11: [x, y, z], 
            12: [-z, -x, y], 13: [x, -z, y], 14: [z, x, y], 
            15: [-x, z, y], 16: [-x, y, -z], 17: [-y, -x, -z], 
            18: [x, -y, -z], 19: [y, x, -z], 20: [y, -z, -x], 
            21: [z, y, -x], 22: [-y, z, -x], 23: [-z, -y, -x]
            }

        new_scanner.append([orientations[orientation][0], orientations[orientation][1], orientations[orientation][2]])


    return new_scanner

inverse_rotation = {0: 13, 1: 20, 2: 2, 3: 7, 4: 4, 5: 14, 6: 21, 7: 3, 8: 10, 9: 9, 10: 8, 11: 11, 12: 22, 13: 0, 14: 5, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 1, 21: 6, 22: 12, 23: 23}


# compare scanners

def compare_scanner(scanner1, scanner2):
    distance = []
    
    for point1 in scanner1:
        for point2 in scanner2:
            space = [c1-c2 for c1, c2 in zip(point1, point2)]
            # distance.append([[point1, point2], space])
            distance.append(space)

    return distance

beacons = []
for el in scanners[0]:
    beacons.append(el)


cracked = [0]
vector = [[0, 0, 0] for i in range(34)]


lst = [[1, 3], [1, 3], [1, 2], [1, 3]]
lst2 = [1, 2, 2, 2, 2, 2]


while len(cracked) < 34:
    print(len(cracked))
    print(vector)
    print(scanners[0])

    for scanner1 in scanners:
        index1 = scanners.index(scanner1)

        if index1 not in cracked:
            continue

        scanner_copies = []

        for i in range(0, 24):
            scanner_copies.append(orientate(scanner1, i))

        for scanner2 in scanners:
            index2 = scanners.index(scanner2)

            if index2 in cracked or index1 == index2:
                continue
            
            print(index1, index2)

            found = False
            for scanner_copy in scanner_copies:
                if found == True:
                    break
                else:
                    distances = []
                    distances = compare_scanner(scanner_copy, scanner2)

                    for distance in distances:
                        if distances.count(distance) > 11:
                            orientation = scanner_copies.index(scanner_copy)
                            
                            #  rotate to get back
                            vector_s1_s2 = orientate([distance], inverse_rotation[orientation])[0]


                            vector[index2] = [i + j for i, j in zip(vector[index1], vector_s1_s2)]

                            scanners[index2] = orientate(scanner2, inverse_rotation[orientation])
                                                
                            for point in scanners[index2]:
                                beacons.append([point[0] + vector[index2][0], point[1] + vector[index2][1], point[2] + vector[index2][2]])
                            found = True

                            cracked.append(index2)

                            print('match!:', index1, index2)

                            break


unique_beacons = []

for beacon in beacons:
    if beacon not in unique_beacons:
        unique_beacons.append(beacon)

print('unique beacons:', len(unique_beacons))


# part two

def manhattan(point1, point2):
    distance = 0
    for c1, c2 in zip(point1, point2):
        distance += abs(c2 - c1)
    
    return distance

man_distances = 0

for scan1 in vector:
    for scan2 in vector:
        if manhattan(scan1, scan2) > man_distances:
            man_distances = manhattan(scan1, scan2)

print('max manhattan distance between two scanners:', man_distances)
