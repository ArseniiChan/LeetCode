class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        benches = {}
        result = 0
        for pair in students:
            sid = pair[0]
            bid = pair[1]
            if bid not in benches:
                benches[bid] = set()
            benches[bid].add(sid)

        for s in benches.values():
            result = max(result, len(s))
        return result
            










       


        