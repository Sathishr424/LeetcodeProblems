# Last updated: 12/25/2025, 7:12:05 PM
class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        active_count = s.count('1')
        
        segments = []
        start = 0
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                segments.append((start, i - start + 1))
                start = i + 1
        segment_count = len(segments)
        
        max_power = 20
        INF = 10**9
        NEG_INF = -INF
        rmq = [[NEG_INF] * segment_count for _ in range(max_power)]
        
        for i in range(segment_count):
            if s[segments[i][0]] == '0' and i + 2 < segment_count:
                rmq[0][i] = segments[i][1] + segments[i + 2][1]
        
        for power in range(1, max_power):
            range_len = 1 << power
            for i in range(segment_count - range_len + 1):
                rmq[power][i] = max(rmq[power - 1][i],
                                    rmq[power - 1][i + (range_len >> 1)])
        
        def get_max_in_range(l, r):
            if l > r:
                return NEG_INF
            p = (r - l + 1).bit_length() - 1
            return max(rmq[p][l], rmq[p][r - (1 << p) + 1])
        
        result = []
        for left, right in queries:
            left_index = bisect_right(segments, (left, INF)) - 1
            right_index = bisect_right(segments, (right, INF)) - 1
            
            if right_index - left_index + 1 <= 2:
                result.append(active_count)
                continue
            
            def get_segment_size(i):
                if i == left_index:
                    return segments[left_index][1] - (left - segments[left_index][0])
                if i == right_index:
                    return right - segments[right_index][0] + 1
                return segments[i][1]
            
            def calculate_new_sections(i):
                if i < 0 or i + 2 >= segment_count or s[segments[i][0]] == '1':
                    return NEG_INF
                return get_segment_size(i) + get_segment_size(i + 2)
            
            best_increase = max(get_max_in_range(left_index + 1, right_index - 3), 0)
            best_increase = max(best_increase, calculate_new_sections(left_index))
            best_increase = max(best_increase, calculate_new_sections(right_index - 2))
            
            result.append(active_count + best_increase)
        
        return result