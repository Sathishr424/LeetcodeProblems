// Last updated: 12/25/2025, 7:07:56 PM
class Solution {
public:
    int dfs(vector<vector<int>>& graph, vector<int>& good, vector<int>& costs, int x, int par) {
        int total_cost = good[x];
        for (int y: graph[x]) {
            if (y == par) continue;
            int cost = dfs(graph, good, costs, y, x);
            total_cost += max(0, cost);
        }
        costs[x] = total_cost;
        return total_cost;
    }

    void dfs2(vector<vector<int>>& graph, vector<int>& costs, vector<int>& ret, int x, int par, int cost_so_far) {
        int cost = costs[x];
            
        if (cost <= 0) {
            cost_so_far += cost;
        }
        ret[x] = max(cost, cost_so_far);

        for (int y: graph[x]) {
            if (y == par) continue;
            dfs2(graph, costs, ret, y, x, max(cost_so_far, cost));
        }
    }

    vector<int> maxSubgraphScore(int n, vector<vector<int>>& edges, vector<int>& good) {
        vector<int> ret(n, 0);
        vector<int> costs(n, 0);
        vector<vector<int>> graph(n);
        for (int i=0; i<n; i++) {
            good[i] = good[i] == 0 ? -1 : 1;
        }

        for (auto& edge: edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        dfs(graph, good, costs, 0, -1);
        dfs2(graph, costs, ret, 0, -1, costs[0]);

        return ret;
    }
};