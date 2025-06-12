// Last updated: 12/6/2025, 5:46:42 am
class Solution {
  public boolean isBipartite(int[][] graph) {
    UnionFind uf = new UnionFind(graph.length);
    for(int i = 0; i < graph.length; i++) {
      
      for(int j = 0; j < graph[i].length; j++) {
        // If the node is in the same component as its neighbors, then they are in the same set and the graph is not bipartite.
        // Bipartite means each node can only be connected to a node in another set/component
        if(uf.isConnected(i, graph[i][j])) return false;
        
        // We union all the neighbors together
        uf.union(graph[i][0], graph[i][j]);
      }
    }

    return true;
  }

  public class UnionFind {
    private int[] parent;
    private int[] rank;

    public UnionFind(int n) {
      parent = new int[n];
      rank = new int[n];

      for (int i = 0; i < n; i++) {
        parent[i] = i;
      }
    }

    public int find(int x) {
      if(parent[x] == x) return x;

      int root = find(parent[x]);
      parent[x] = root; // path compression
      return root;
    }

    public void union(int x, int y) {
      int rootx = find(x);
      int rooty = find(y);

      if (rootx == rooty) return;

      if (rank[rootx] > rank[rooty]) {
        parent[rooty] = rootx;
        rank[rootx]++;
      } else {
        parent[rootx] = rooty;
        rank[rooty]++;
      }
    }

    public boolean isConnected(int p, int q) {
      return find(p) == find(q);
    }
  }
}