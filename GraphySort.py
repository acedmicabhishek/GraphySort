import pygame
pygame.init()

# window starting
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graphysort")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# draw points on the graph
def draw_points(arr, sorted_arr=[]):
    window.fill(WHITE)
    for i, val in enumerate(arr):
        pygame.draw.circle(window, RED, (val * 10, height - val * 10), 5) 
    for i, val in enumerate(sorted_arr):
        pygame.draw.circle(window, GREEN, (val * 10, height - val * 10), 5)
    pygame.display.update()


def graphysort(arr):
    sorted_arr = []
    n = len(arr)

    # pairs in python
    points = [(val, val) for val in arr]

    # call the windows
    draw_points(arr)

    # Main Sort here
    for y in range(1, max(arr) + 1):
        for point in points:
            if point[1] == y and point not in sorted_arr:
                sorted_arr.append(point[1])
                draw_points(arr, sorted_arr)
                break

    return sorted_arr

def main(): 
    array = [345, 32, 65, 1, 73, 2, 12, 8, 83]
    
    running = True
    sorted = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not sorted:
            sorted_array = graphysort(array)
            sorted = True
            
        draw_points(array, sorted_array)

    print("Final sorted array:", sorted_array)
    pygame.quit()

if __name__ == "__main__":
    main()
