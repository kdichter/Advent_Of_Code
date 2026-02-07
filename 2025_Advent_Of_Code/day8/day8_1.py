import math

file = open("day8_data.txt", "r")

points = []
for line in file:
    points.append([int(x) for x in line.strip().split(',')])

distances = {}

for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if j > i:
            distances[(i, j)] = math.dist(p1, p2)

sorted_points = sorted(distances.items(), key=lambda x: x[1])

clusters = []
point_to_cluster = {}  # maps point -> cluster index
max_connections = 1000
curr_connections = 0

for (p1, p2), dist in sorted_points:
    c1 = point_to_cluster.get(p1, -1)
    c2 = point_to_cluster.get(p2, -1)

    # Case 1: both are in clusters but not the same cluster
    if c1 != -1 and c2 != -1:
        if c1 != c2:
            clusters[c1].extend(clusters[c2])
            for p in clusters[c2]:
                point_to_cluster[p] = c1
            clusters[c2] = []

    # Case 2: p1 in cluster -> add p2 if not in any cluster
    elif c1 != -1:
        clusters[c1].append(p2)
        point_to_cluster[p2] = c1

    # Case 3: p2 in cluster -> add p1 if not in any cluster
    elif c2 != -1:
        clusters[c2].append(p1)
        point_to_cluster[p1] = c2

    # Case 4: neither in a cluster -> create new cluster
    else:
        clusters.append([p1, p2])
        cluster_idx = len(clusters) - 1
        point_to_cluster[p1] = cluster_idx
        point_to_cluster[p2] = cluster_idx

    curr_connections += 1
    if curr_connections >= max_connections:
        break

# Remove any empty clusters created during merges
clusters = [cl for cl in clusters if cl]

# Sort clusters by size descending
clusters.sort(key=len, reverse=True)

# Multiply the sizes of the three largest clusters
total = len(clusters[0]) * len(clusters[1]) * len(clusters[2])
print(total)
