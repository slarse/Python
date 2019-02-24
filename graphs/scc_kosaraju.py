from __future__ import print_function

def dfs(g, r, scc, component, visit, stack, u):
    if visit[u]: return
    visit[u] = True
    for v in g[u]:
        dfs(g, r, scc, component, visit, stack, v)
    stack.append(u)

def dfs2(g, r, scc, component, visit, stack, u):
    if visit[u]: return
    visit[u] = True
    component.append(u)
    for v in r[u]:
        dfs2(g, r, scc, component, visit, stack, v)

def kosaraju(g, r, scc, component, visit, stack, n):
    for i in range(n):
        dfs(g, r, scc, component, visit, stack, i)
    visit = [False]*n
    for i in stack[::-1]:
        if visit[i]: continue
        component = []
        dfs2(g, r, scc, component, visit, stack, i)
        scc.append(component)
    return scc

def main():
    # n - no of nodes, m - no of edges
    n, m = list(map(int,input().split()))

    g = [[] for i in range(n)] #graph
    r = [[] for i in range(n)] #reversed graph
    # input graph data (edges)
    for i in range(m):
        u, v = list(map(int,input().split()))
        g[u].append(v)
        r[v].append(u)

    stack = []
    visit = [False]*n
    scc = []
    component = []

    print(kosaraju(g, r, scc, component, visit, stack, n))

if __name__ == "__main__":
    main()
