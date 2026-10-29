import math
import sys

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Step 1: Handle recursion limit for deep tree traversals
        sys.setrecursionlimit(max(300000, n * 2))
        
        # Step 2: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 3: Setup variables for Euler Tour and Binary Lifting
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        euler_tour = [0] * (2 * n)
        timer = 0
        
        cols = int(math.log2(n)) + 1 if n > 0 else 1
        ancestor_table = [[-1] * cols for _ in range(n)]
        s_list = list(s)
        
        # Step 4: Iterative-safe DFS using an explicit call stack to avoid recursion overhead
        # Format: (node, parent, depth_val, state) where state: 0 = entering, 1 = processing children
        stack = [(0, -1, 0, 0)]
        child_indices = [0] * n
        
        while stack:
            u, p, d, state = stack[-1]
            
            if state == 0:
                depth[u] = d
                ancestor_table[u][0] = p
                tin[u] = timer
                euler_tour[timer] = 1 << (ord(s_list[u]) - 97) # 'a' is 97
                timer += 1
                stack[-1] = (u, p, d, 1) # Move to processing state
            else:
                # Process children one by one
                idx = child_indices[u]
                if idx < len(adj[u]):
                    v = adj[u][idx]
                    child_indices[u] += 1
                    if v != p:
                        stack.append((v, u, d + 1, 0))
                else:
                    # Leaving node
                    tout[u] = timer
                    euler_tour[timer] = 1 << (ord(s_list[u]) - 97)
                    timer += 1
                    stack.pop()

        # Step 5: Complete the Binary Lifting Ancestor Table
        for j in range(1, cols):
            for node in range(n):
                if ancestor_table[node][j - 1] != -1:
                    ancestor_table[node][j] = ancestor_table[ancestor_table[node][j - 1]][j - 1]
                    
        # Step 6: Binary Lifting LCA Helper Function
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(cols):
                if diff & (1 << j):
                    u = ancestor_table[u][j]
            if u == v:
                return u
            for j in range(cols - 1, -1, -1):
                if ancestor_table[u][j] != ancestor_table[v][j]:
                    u = ancestor_table[u][j]
                    v = ancestor_table[v][j]
            return ancestor_table[u][0]

        # Step 7: Fenwick Tree (XOR Binary Indexed Tree) Operations
        # Fenwick array size is 2*n + 1 (1-indexed mapping)
        N = 2 * n
        bit = [0] * (N + 1)
        
        def bit_update(idx: int, val: int):
            idx += 1 # Convert 0-index to 1-index
            while idx <= N:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx: int) -> int:
            idx += 1 # Convert 0-index to 1-index
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize the Fenwick tree values from the initial euler_tour array
        for i in range(N):
            bit_update(i, euler_tour[i])

        # Step 8: Parse and process queries sequentially
        result = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                node = int(parts[1])
                c = parts[2]
                
                # XOR-out the old mask and XOR-in the new character mask at both locations
                old_mask = 1 << (ord(s_list[node]) - 97)
                new_mask = 1 << (ord(c) - 97)
                xor_diff = old_mask ^ new_mask
                
                s_list[node] = c
                bit_update(tin[node], xor_diff)
                bit_update(tout[node], xor_diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                
                lca_node = get_lca(u, v)
                lca_mask = 1 << (ord(s_list[lca_node]) - 97)
                
                # Evaluate prefix XOR values up to tin[u] and tin[v]
                mask = bit_query(tin[u]) ^ bit_query(tin[v]) ^ lca_mask
                
                # A path is a palindrome if at most one character has an odd frequency count
                result.append((mask & (mask - 1)) == 0)
                
        return result
