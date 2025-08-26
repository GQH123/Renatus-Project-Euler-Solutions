with open('input.txt', 'r') as f:
    edges = [[int(x) if x != '-' else -1 for x in line.split(',') if x] for line in f.read().split('\n') if line]


N = len(edges)
print(f'N: {N}')
for _edges in edges:
    assert len(_edges) == N

ufs_parent = [i for i in range(len(edges))]


def ufs(x):
    if ufs_parent[x] == x:
        return x
    ufs_parent[x] = ufs(ufs_parent[x])
    return ufs_parent[x]


all_edges = []
total_cost = 0

for i in range(len(edges)):
    for j in range(i + 1, len(edges)):
        if edges[i][j] != -1:
            all_edges.append((i, j, edges[i][j]))
            total_cost += edges[i][j]

all_edges.sort(key=lambda x: x[2])
answer = 0
added_edges_count = 0

for edge in all_edges:
    if ufs(edge[0]) == ufs(edge[1]):
        continue
    ufs_parent[ufs(edge[0])] = ufs(edge[1])
    answer += edge[2]
    added_edges_count += 1

print(answer)
print(added_edges_count)
print(total_cost - answer)
