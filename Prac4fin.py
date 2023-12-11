import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_solvable(self):
        inversions_initial = self.count_inversions(self.initial_state)
        if inversions_initial % 2 == 0:
            return True
        else:
            return False  # if odd no of inveraions

    def count_inversions(self, state):
        inversions = 0
        for i in range(len(state) - 1):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversions += 1
        return inversions

    def get_neighbors(self, state):
        neighbors = []
        empty_tile_index = state.index(0)
        row, col = divmod(empty_tile_index, 3)

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]   # up , down , left and ryt

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                neighbor = list(state)
                new_index = new_row * 3 + new_col
                neighbor[empty_tile_index], neighbor[new_index] = neighbor[new_index], neighbor[empty_tile_index]
                neighbors.append(tuple(neighbor))

        return neighbors

    def heuristic(self, state):
        manhattan_distance = 0
        for i in range(9):
            if state[i] != 0:
                goal_row, goal_col = divmod(self.goal_state.index(state[i]), 3)
                current_row, current_col = divmod(i, 3)
                manhattan_distance += abs(goal_row - current_row) + abs(goal_col - current_col)
        return manhattan_distance

def solve_puzzle(puzzle):
    if not puzzle.is_solvable():
        print("Puzzle is not solvable")

    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (puzzle.heuristic(puzzle.initial_state), 0, puzzle.initial_state))
    g_score = {puzzle.initial_state: 0}
    came_from = {}

    while open_set:
        f_score, current_g_score, current_state = heapq.heappop(open_set)

        if current_state == puzzle.goal_state:
            # Reconstruct path
            path = [current_state]
            while current_state in came_from:
                current_state = came_from[current_state]
                path.insert(0, current_state)
            return path

        closed_set.add(current_state)

        for neighbor in puzzle.get_neighbors(current_state):
            if neighbor in closed_set:
                continue

            tentative_g_score = current_g_score + 1

            if neighbor not in [state for (_, _, state) in open_set] or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_state
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + puzzle.heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))


def print_solution_path(solution):
    for i, state in enumerate(solution):
        print(f"Step {i}:\n")
        for row in range(3):
            print(" ".join(map(str, state[row * 3: (row + 1) * 3])))
        print("\n")

if __name__ == "__main__":
    initial_state = (1, 2, 3 ,4 , 5, 6, 8, 7, 0)  
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)    

    puzzle = Puzzle(initial_state, goal_state)
    solution = solve_puzzle(puzzle)

    if solution:
        print("Solution found:")
        print_solution_path(solution)