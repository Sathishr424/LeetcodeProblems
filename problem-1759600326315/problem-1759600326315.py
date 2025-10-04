# Last updated: 4/10/2025, 11:22:06 pm
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        n = len(student_id)

        heap = []


        for i in range(n):
            id = student_id[i]
            score = 0
            for word in report[i].split(' '):
                if word in positive:
                    score += 3
                elif word in negative:
                    score -= 1

            heapq.heappush(heap, (score, -id))
            if len(heap) > k:
                heapq.heappop(heap)

        ret = []
        while heap:
            ret.append(-heapq.heappop(heap)[1])

        return ret[::-1]