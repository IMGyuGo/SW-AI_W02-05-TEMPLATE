import heapq
patients2 = [
("환자A", 5),
("환자B", 1),
("환자C", 3),
("환자D", 2)
]
heap = []

heapq.heappush(heap, patients2)
print(heap)