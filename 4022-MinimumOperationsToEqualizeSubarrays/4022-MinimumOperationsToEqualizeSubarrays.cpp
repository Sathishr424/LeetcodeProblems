// Last updated: 12/25/2025, 7:09:08 PM
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <numeric>
#include <utility>

using namespace std;

// Lambda replacements using standard functions
long long cmin(long long x, long long y) { return min(x, y); }
long long cmax(long long x, long long y) { return max(x, y); }

/**
 * @brief Node structure for the Persistent Segment Tree using array indices.
 * l and r store the index of the child node in the 'nodes' vector.
 * An index of 0 will represent a null or uninitialized node.
 */
struct Node {
    int l = 0; // Index of left child in the 'nodes' vector
    int r = 0; // Index of right child in the 'nodes' vector
    long long cnt = 0;
    long long sum = 0;
};

/**
 * @brief Persistent Segment Tree (PST) implementation using array storage.
 * This approach reduces memory overhead compared to raw pointers,
 * helping to prevent Memory Limit Exceeded (MLE) errors.
 */
class PSegmentTree {
private:
    int n;
    vector<int> roots;
    // Node pool: stores all nodes created across all versions of the tree
    vector<Node> nodes; 

    // Helper to create a new node and return its index
    int newNode(int l_idx, int r_idx, long long count, long long s) {
        Node n_new;
        n_new.l = l_idx;
        n_new.r = r_idx;
        
        // If children are valid (non-zero index), aggregate their count and sum
        if (l_idx != 0 && r_idx != 0) {
            n_new.cnt = nodes[l_idx].cnt + nodes[r_idx].cnt;
            n_new.sum = nodes[l_idx].sum + nodes[r_idx].sum;
        } else {
            // Otherwise, use the explicit count and sum (for leaf updates)
            n_new.cnt = count;
            n_new.sum = s;
        }

        nodes.push_back(n_new);
        return nodes.size() - 1;
    }
    
    // Helper for leaf node creation (incrementing count/sum)
    int newNode(long long count, long long s) {
        nodes.push_back({0, 0, count, s}); // l=0, r=0 for leaves
        return nodes.size() - 1;
    }

    /**
     * @brief Recursively builds the initial empty segment tree.
     * @param l The left boundary of the current range (compressed indices).
     * @param r The right boundary of the current range (compressed indices).
     * @return The index of the root of the created subtree.
     */
    int build(int l, int r) {
        if (l == r) {
            // Leaf node is an empty Node (index 0, 0 count/sum)
            return newNode(0, 0); 
        }
        int mid = l + (r - l) / 2;
        int left_root = build(l, mid);
        int right_root = build(mid + 1, r);
        return newNode(left_root, right_root, 0, 0); // Aggregate node
    }

    /**
     * @brief Updates the tree persistently by creating a new path of nodes.
     * @param node_idx The index of the root of the previous version.
     * @param l The left boundary of the current range (compressed indices).
     * @param r The right boundary of the current range (compressed indices).
     * @param pos The compressed index (rank) to update.
     * @param value The actual value (nums[i] // k) to be added to the sum.
     * @return The index of the root of the new updated subtree.
     */
    int update(int node_idx, int l, int r, int pos, int value) {
        // Base case: leaf node
        if (l == r) {
            // Create a new node reflecting the update based on the previous node's state
            return newNode(nodes[node_idx].cnt + 1, nodes[node_idx].sum + value);
        }

        int mid = l + (r - l) / 2;
        int new_l, new_r;

        if (pos <= mid) {
            // Update left child, keep previous right child
            new_l = update(nodes[node_idx].l, l, mid, pos, value);
            new_r = nodes[node_idx].r;
        } else {
            // Update right child, keep previous left child
            new_l = nodes[node_idx].l;
            new_r = update(nodes[node_idx].r, mid + 1, r, pos, value);
        }
        
        // Create the new parent node linking the new children
        return newNode(new_l, new_r, 0, 0);
    }

    /**
     * @brief Differential query to find the compressed index (rank) of the K-th smallest element in range [L, R].
     * @param left_idx Index of Root T[L].
     * @param right_idx Index of Root T[R+1].
     * @param l The left boundary of the current range (compressed indices).
     * @param r The right boundary of the current range (compressed indices).
     * @param k The desired rank.
     * @return The compressed index of the K-th smallest element.
     */
    int _getKthSmallest(int left_idx, int right_idx, int l, int r, int k) {
        if (l == r) {
            return l;
        }

        int mid = l + (r - l) / 2;
        
        // Pointers for clarity
        const Node& left = nodes[left_idx];
        const Node& right = nodes[right_idx];
        
        // Count of elements in the left side of the range [L, R]
        // This is differential: right.l.cnt - left.l.cnt
        long long left_count = nodes[right.l].cnt - nodes[left.l].cnt;
        
        if (left_count >= k) {
            // K-th smallest is in the left subtree
            return _getKthSmallest(left.l, right.l, l, mid, k);
        }
        // K-th smallest is in the right subtree
        return _getKthSmallest(left.r, right.r, mid + 1, r, k - left_count);
    }

    /**
     * @brief Differential query to find the sum of the first K smallest elements in range [L, R].
     * @param left_idx Index of Root T[L].
     * @param right_idx Index of Root T[R+1].
     * @param l The left boundary of the current range (compressed indices).
     * @param r The right boundary of the current range (compressed indices).
     * @param k The number of smallest elements to sum up.
     * @return The sum of the first K smallest actual values (num // k).
     */
    long long _getFirstKSum(int left_idx, int right_idx, int l, int r, int k) {
        if (l == r) {
            // The sum is the contribution of the leaf in the range [L, R]
            return nodes[right_idx].sum - nodes[left_idx].sum;
        }
        
        int mid = l + (r - l) / 2;
        
        // Pointers for clarity
        const Node& left = nodes[left_idx];
        const Node& right = nodes[right_idx];
        
        // Count of elements in the left side of the range [L, R]
        long long left_count = nodes[right.l].cnt - nodes[left.l].cnt;
        
        if (left_count >= k) {
            // The first K elements are fully contained in the left side
            return _getFirstKSum(left.l, right.l, l, mid, k);
        }
        
        // The first K elements span both sides.
        // Sum the entire left side's value contribution
        long long left_sum_total = nodes[right.l].sum - nodes[left.l].sum;
        
        // Recurse for the remaining k elements in the right side
        return left_sum_total + _getFirstKSum(left.r, right.r, mid + 1, r, k - left_count);
    }

public:
    /**
     * @brief Initializes the Persistent Segment Tree.
     * @param size The size of the coordinate space (number of elements, N).
     * @param divided Vector of (num // k) values.
     * @param compressed Map from (value, original_index) to its rank (compressed index).
     */
    PSegmentTree(int size, const vector<int>& divided, 
                 const map<pair<int, int>, int>& compressed) : n(size) {
        
        // Reserve memory for the nodes (O(N log N) nodes)
        // A safe estimation is N * (log2(N) + 2) + 1 for the 1-based indexing
        nodes.reserve(n * 20 + 2); 
        nodes.push_back({}); // Index 0 is a dummy/sentinel node for easy null check

        // Root at index 0 (empty tree)
        roots.push_back(build(0, n - 1));

        for (int i = 0; i < divided.size(); ++i) {
            int num = divided[i];
            // Get the compressed index (rank) for this value at this original position
            int pos = compressed.at({num, i});
            
            // Create a new root based on the previous root
            roots.push_back(update(roots.back(), 0, n - 1, pos, num));
        }
    }
    
    // Public query methods
    int getKthSmallest(int l, int r, int k) {
        // Query on range [l, r] uses roots[r+1] and roots[l]
        return _getKthSmallest(roots[l], roots[r + 1], 0, n - 1, k);
    }

    long long getFirstKSum(int l, int r, int k) {
        // Query on range [l, r] uses roots[r+1] and roots[l]
        return _getFirstKSum(roots[l], roots[r + 1], 0, n - 1, k);
    }
};

class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> divided;
        // Prefix sum of 'divided' values (long long to prevent overflow)
        vector<long long> prefix = {0};
        
        // C++ equivalent of Python's tuple list for coordinate compression
        vector<pair<int, int>> new_nums;
        
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            int d = num / k;
            
            divided.push_back(d);
            prefix.push_back(prefix.back() + d);
            new_nums.push_back({d, i}); // (value, original_index)
        }
        
        // Coordinate Compression Logic:
        // Key: (value, original_index), Value: compressed_index (rank)
        map<pair<int, int>, int> compressed;
        // Key: compressed_index (rank), Value: actual_value (num // k)
        vector<int> uncompressed(n); 
        
        // Sort by value (num // k), then by original index for a stable ranking
        sort(new_nums.begin(), new_nums.end());
        
        int index = 0;
        for (const auto& p : new_nums) {
            int num = p.first;
            int i = p.second;
            
            compressed[{num, i}] = index;
            uncompressed[index] = num;
            index++;
        }
        
        // Determine the "same_group" based on remainder (nums[i] % k)
        vector<int> same_group(n);
        int group = 0;
        int i = 0;
        while (i < n) {
            int rem = nums[i] % k;
            int j = i;
            while (j < n && nums[j] % k == rem) {
                same_group[j] = group;
                j++;
            }
            i = j;
            group++;
        }

        // The size of the index space is 'index' (up to n)
        PSegmentTree segTree(index, divided, compressed);
        vector<long long> ret;

        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];
            
            // Constraint check: all elements in [l, r] must have the same remainder (nums[i] % k).
            if (same_group[l] != same_group[r]) {
                ret.push_back(-1);
                continue;
            }
            
            long long window = r - l + 1;
            long long half = window / 2;
            
            long long final_ops;

            if (window % 2 != 0) { // Odd window size
                // Median is the (half + 1)-th smallest element
                int med_rank = segTree.getKthSmallest(l, r, half + 1);
                long long median = uncompressed[med_rank];
                
                // Sum of the (half + 1) smallest elements
                long long leftSum = segTree.getFirstKSum(l, r, half + 1);
                
                // Total sum of 'divided' in range [l, r]
                long long totalSum = prefix[r + 1] - prefix[l];
                
                // Sum of the remaining elements (greater than median)
                long long remSum = totalSum - leftSum;
                
                // Calculate minimum operations:
                // Sum_{i <= median} (median - divided[i]) + Sum_{i > median} (divided[i] - median)
                final_ops = (median * (half + 1) - leftSum) + (remSum - median * half);
            } else { // Even window size
                // Find the half-th smallest element for the target
                int med_l_rank = segTree.getKthSmallest(l, r, half);
                long long median_target = uncompressed[med_l_rank];
                
                // Sum of the first 'half' smallest elements
                long long leftSum = segTree.getFirstKSum(l, r, half);
                
                long long totalSum = prefix[r + 1] - prefix[l];
                long long remSum = totalSum - leftSum;
                
                // Calculate minimum operations (target: median_target, count of smaller/equal: half)
                // Sum_{i < half} (median_target - divided[i]) + Sum_{i >= half} (divided[i] - median_target)
                final_ops = (median_target * half - leftSum) + (remSum - median_target * half);
            }
            
            ret.push_back(final_ops);
        }
        
        return ret;
    }
};