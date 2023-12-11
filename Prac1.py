
from collections import deque

jug1_capacity = int(input("Enter the capacity of Jug 1 : "))
jug2_capacity = int(input("Enter the capacity of Jug 2 : "))
target_volume = int(input("Enter target capacity : "))

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_volume):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_volume = target_volume
        self.visited = set()

    def is_valid_state(self, state):
        jug1, jug2 = state
        return 0 <= jug1 <= self.jug1_capacity and 0 <= jug2 <= self.jug2_capacity

    def solve(self):
        start_state = (0, 0)
        queue = deque()
        queue.append((start_state, []))

        while queue:
            current_state, path = queue.popleft()
            self.visited.add(current_state)

            jug1, jug2 = current_state

            if jug1 == self.target_volume or jug2 == self.target_volume:
                return path

            # Fill jug1
            if jug1 < self.jug1_capacity:
                new_state = (self.jug1_capacity, jug2)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Fill Jug 1", new_state)]))

            # Fill jug2
            if jug2 < self.jug2_capacity:
                new_state = (jug1, self.jug2_capacity)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Fill Jug 2", new_state)]))

            # Pour from jug1 to jug2
            if jug1 > 0:
                pour_amount = min(jug1, self.jug2_capacity - jug2)
                new_state = (jug1 - pour_amount, jug2 + pour_amount)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Pour Jug 1 to Jug 2", new_state)]))

            # Pour from jug2 to jug1
            if jug2 > 0:
                pour_amount = min(jug2, self.jug1_capacity - jug1)
                new_state = (jug1 + pour_amount, jug2 - pour_amount)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Pour Jug 2 to Jug 1", new_state)]))

            # Empty jug1
            if jug1 > 0:
                new_state = (0, jug2)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Empty Jug 1", new_state)]))

            # Empty jug2
            if jug2 > 0:
                new_state = (jug1, 0)
                if new_state not in self.visited:
                    queue.append((new_state, path + [(current_state, "Empty Jug 2", new_state)]))

        return None

problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_volume)
solution = problem.solve()


if solution:
    print("Solution found:")
    for step, (prev_state, action, new_state) in enumerate(solution):
        print(f"Step {step + 1}: {action}")
        print(f"  Previous State: {prev_state}")
        print(f"  New Statwe: {new_state}")
else:
    print("It is not possible to find  solution .")