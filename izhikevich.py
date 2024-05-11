import numpy as np
import pygame
import sys

# Constants for the Izhikevich neuron using the regular spiking parameters
C, Vr, Vt, Vpeak, k, a, b, c, d = 100.0, -60.0, -40.0, 35.0, 0.7, 0.03, -2.0, -50.0, 100.0

# Initialize Pygame
pygame.init()
width, height = 800, 600  # Set your desired resolution
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spiking Neuron Model Visualization')
clock = pygame.time.Clock()

# Colors and Styles
background_color = (255, 255, 255)
line_color = (220, 0, 0)
grid_color = (200, 200, 200)
text_color = (50, 50, 50)
font = pygame.font.SysFont('Arial', 18)

# Initialize variables for plotting
scale_y = 2  # Adjust scale for better visibility
offset_y = height // 2  # Center the graph vertically
points = []  # List to hold points for plotting

# Function to draw grid for better visibility of the plots
def draw_grid():
    for i in range(0, width, 50):  # Drawing vertical lines
        pygame.draw.line(screen, grid_color, (i, 0), (i, height))
    for i in range(0, height, 50):  # Drawing horizontal lines
        pygame.draw.line(screen, grid_color, (0, i), (width, i))

def izhikevich_update(v, u, I):
    if v >= Vpeak:  # Spike condition
        v = c  # Reset membrane potential
        u += d  # Reset recovery variable
    dv = (k * (v - Vr) * (v - Vt) - u + I) / C
    du = a * (b * (v - Vr) - u)
    v += dv  # Update membrane potential
    u += du  # Update recovery variable
    return v, u

def run_simulation():
    global points
    v = Vr  # Initial membrane potential
    u = b * v  # Initial recovery variable
    I = 53.0  # Input current to cause spiking
    time_step = 0  # Initialize time step
    line_thickness = 1  # Thickness of the line
    y_scale = 10  # Scale factor for y values
    
    # Colors
    background_color = (0, 0, 0)  # Black background
    line_color = (148, 0, 211)  # Bright purple line
    text_color = (0, 255, 0)  # Fluorescent green writing
    
    # Clear the points to start with an empty buffer
    points = [(0, offset_y) for _ in range(width)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        v, u = izhikevich_update(v, u, I)

        # Scale and wrap the y value
        scaled_v = offset_y - (v - Vr) / y_scale
        # Add new point for membrane potential at the next time step
        points[time_step % width] = (time_step % width, scaled_v)

        screen.fill(background_color)  # Fill the background with black color

        # No need for a grid on a black background unless desired
        # draw_grid()  # Draw the grid if needed

        # Draw lines connecting points with proper wrapping
        for i in range(1, len(points)):
            start_point = (points[i-1][0] % width, points[i-1][1])
            end_point = (points[i][0] % width, points[i][1])
            # If the line wraps, skip drawing this segment
            if abs(start_point[0] - end_point[0]) > 1:
                continue
            pygame.draw.line(screen, line_color, start_point, end_point, line_thickness)

        # Real-time data display with fluorescent green writing
        text_surface = font.render(f'Membrane Potential: {v:.2f} mV', True, text_color)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second
        time_step += 1

run_simulation()  # Start the simulation
