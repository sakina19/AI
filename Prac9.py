def is_consistent(assignment, region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring_solver(regions, colors, neighbors):
    assignment = {}
    
    def backtrack(region_index):
        if region_index == len(regions):
            return True
        
        region = regions[region_index]
        for color in colors:
            if is_consistent(assignment, region, color):
                assignment[region] = color
                if backtrack(region_index + 1):
                    return True
                assignment.pop(region)
        
        return False
    
    if backtrack(0):
        print("Solution:")
        for region, color in assignment.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

regions = ["WA", "NT", "Q", "SA", "NSW"]
colors = ["Red", "Green", "Blue"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "Q": ["NT", "SA", "NSW"],
    "SA": ["WA", "NT", "Q", "NSW"],
    "NSW": ["Q", "SA"]
}

map_coloring_solver(regions, colors, neighbors)