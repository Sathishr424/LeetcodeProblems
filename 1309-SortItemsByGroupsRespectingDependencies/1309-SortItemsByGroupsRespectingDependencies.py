# Last updated: 12/6/2025, 5:42:57 am
class Solution:
    def set_up(self, n, m, groups, predecessors) : 
        self.n = n 
        self.m = m 
        self.groups = groups 
        self.P = predecessors

    def process_groups(self) :
        for gi in range(len(self.groups)) :
            if self.groups[gi] == -1 : 
                self.groups[gi] = self.m 
                self.m += 1 

    def build_graphs(self) : 
        self.graph_of_items = [[] for _ in range(self.n)]
        self.indegree_of_items = [0]*self.n
        self.graph_of_groups = [[] for _ in range(self.m)]
        self.indegree_of_groups = [0] * self.m
        for dst in range(self.n) : 
            for src in self.P[dst] : 
                self.graph_of_items[src].append(dst)
                self.indegree_of_items[dst] += 1
                if self.groups[dst] != self.groups[src] : 
                    self.graph_of_groups[self.groups[src]].append(self.groups[dst])
                    self.indegree_of_groups[self.groups[dst]] += 1 

    def get_topological_ordering(self, graph, indegrees) :
        target = len(graph) 
        topo_order = []
        stack = [node for node in range(target) if indegrees[node] == 0] 
        while stack : 
            src = stack.pop()
            topo_order.append(src)
            for dst in graph[src] : 
                indegrees[dst] -= 1 
                if indegrees[dst] == 0 : 
                    stack.append(dst)
 
        return topo_order if len(topo_order) == target else []

    def set_topological_orderings(self) : 
        self.item_ordering = self.get_topological_ordering(self.graph_of_items, self.indegree_of_items)
        if len(self.item_ordering) == 0 : 
            return False 
        self.group_ordering = self.get_topological_ordering(self.graph_of_groups, self.indegree_of_groups)
        if len(self.group_ordering) == 0 : 
            return False 
        return True 

    def set_inter_group_ordering(self) : 
        self.inter_group_orderings = collections.defaultdict(list)
        for dst in self.item_ordering : 
            self.inter_group_orderings[self.groups[dst]].append(dst)

    def combine_ordered_groups(self) : 
        self.ordered_groups = []
        for group in self.group_ordering : 
            self.ordered_groups += self.inter_group_orderings[group]

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        self.set_up(n, m, group, beforeItems)
        self.process_groups()
        self.build_graphs()
        if self.set_topological_orderings() == False : 
            return []
        self.set_inter_group_ordering()
        self.combine_ordered_groups()
        return self.ordered_groups