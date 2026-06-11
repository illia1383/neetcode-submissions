class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter  = Counter(tasks)


        cnt = [-cnt for cnt in counter.values()]

        heapq.heapify(cnt)

        time = 0
        q = deque() #[cnt, time]
        while cnt or q:
            time += 1

            if not cnt:
                time = q[0][1]
            else:
                cnts = 1 + heapq.heappop(cnt)

                if cnts:
                    q.append([cnts, time + n])
            if q and q[0][1] == time:
                heapq.heappush(cnt, q.popleft()[0])
        return time 

