import math

# 1️⃣ Read points from file
with open("day8_data.txt", "r") as file:
    points = [list(map(int, line.strip().split(','))) for line in file]

n_points = len(points)

# 2️⃣ Compute all pairwise distances
distances = {}
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if j > i:
            distances[(i, j)] = math.dist(p1, p2)

# 3️⃣ Sort pairs by ascending distance
sorted_pairs = sorted(distances.items(), key=lambda x: x[1])

# 4️⃣ Initialize clusters
clusters = []  # list of clusters (lists of point indices)
point_to_cluster = {}  # point index -> cluster index

# 5️⃣ Optional: limit number of connections
max_connections = 1000  # for AoC example, 10 shortest connections
connections_made = 0

# 6️⃣ Process distance pairs
for (p1, p2), dist in sorted_pairs:
    c1 = point_to_cluster.get(p1)
    c2 = point_to_cluster.get(p2)

    if c1 is not None and c2 is not None:
        # Both points are in clusters
        if c1 != c2:
            # Merge clusters: c2 into c1
            clusters[c1].extend(clusters[c2])
            for p in clusters[c2]:
                point_to_cluster[p] = c1
            clusters[c2] = []  # mark old cluster as empty
        # if c1 == c2, already same cluster → do nothing
    elif c1 is not None:
        # Only p1 is in a cluster → add p2
        clusters[c1].append(p2)
        point_to_cluster[p2] = c1
    elif c2 is not None:
        # Only p2 is in a cluster → add p1
        clusters[c2].append(p1)
        point_to_cluster[p1] = c2
    else:
        # Neither point in a cluster → create new cluster
        clusters.append([p1, p2])
        idx = len(clusters) - 1
        point_to_cluster[p1] = idx
        point_to_cluster[p2] = idx

    connections_made += 1
    if max_connections is not None and connections_made >= max_connections:
        break

# 7️⃣ Remove empty clusters created during merges
clusters = [cl for cl in clusters if cl]

# 8️⃣ Add any unassigned points as single-point clusters
for i in range(n_points):
    if i not in point_to_cluster:
        clusters.append([i])

# 9️⃣ Sort clusters by size descending
clusters.sort(key=len, reverse=True)

# 10️⃣ Multiply sizes of the three largest clusters
top_three_sizes = [len(clusters[i]) for i in range(min(3, len(clusters)))]
total = 1
for size in top_three_sizes:
    total *= size

# 11️⃣ Output results
print("Clusters:", clusters)
print("Sizes of top three clusters:", top_three_sizes)
print("Product of top three cluster sizes:", total)
