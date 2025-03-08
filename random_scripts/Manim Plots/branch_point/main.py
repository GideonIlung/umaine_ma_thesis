from manim import *
from manim.utils.color import ManimColor
import numpy as np

class ComplexFunctionHuePlot(Scene):
    def construct(self):
        # Define the complex function with a parameter theta
        def complex_function(z, theta):
            # Adjust the branch cut by rotating the angle
            return np.sqrt(z**2 - 1) * np.exp(-1j * theta)

        # Create a ValueTracker for the angle theta
        theta_tracker = ValueTracker(0)

        # Create a grid of points in the complex plane
        resolution = 100  # Number of points along each axis
        x_min, x_max = -5, 5
        y_min, y_max = -5, 5
        x_values = np.linspace(x_min, x_max, resolution)
        y_values = np.linspace(y_min, y_max, resolution)

        # Generate the background by coloring each point
        pixels = VGroup()
        pixel_size = (x_max - x_min) / resolution
        for x in x_values:
            for y in y_values:
                pixel = Square(side_length=pixel_size)
                pixel.set_stroke(width=0)
                pixel.move_to([x, y, 0])
                pixels.add(pixel)

        # Updater function for the pixels
        def update_pixels(group):
            theta = theta_tracker.get_value()
            for pixel in group:
                x, y, _ = pixel.get_center()
                z = complex(x, y)
                fz = complex_function(z, theta)
                hue = (np.angle(fz) + np.pi) / (2 * np.pi)  # Normalize to [0, 1]
                color = ManimColor.from_hsv((hue, 1, 0.5))
                pixel.set_fill(color, opacity=1)

        pixels.add_updater(update_pixels)
        self.add(pixels)

        # Optionally, add a grid and labels
        grid = NumberPlane(
            x_range=[x_min, x_max, 1],
            y_range=[y_min, y_max, 1],
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )
        self.add(grid)

        x_label = grid.get_x_axis_label("Re", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = grid.get_y_axis_label("Im", edge=UP, direction=UP, buff=0.2)
        self.add(x_label, y_label)

        # Branch points
        A = np.array([-1, 0, 0])
        B = np.array([1, 0, 0])

        # Create dots at branch points
        dot_a = Dot(point=A, color=GREEN)
        dot_b = Dot(point=B, color=GREEN)
        self.add(dot_a, dot_b)

        # Add labels to the branch points
        label_A = Text("A").next_to(dot_a, DOWN)
        label_B = Text("B").next_to(dot_b, UP)
        self.add(label_A, label_B)

        # Create a dot that moves along a path around the branch point B
        r = 2  # Radius of the circle around the branch point
        def get_z():
            theta = theta_tracker.get_value()
            z = B[:2] + r * np.array([np.cos(theta), np.sin(theta)])
            return np.array([z[0], z[1], 0])

        moving_dot = Dot(color=YELLOW)
        moving_dot.add_updater(lambda d: d.move_to(get_z()))
        self.add(moving_dot)

        # Animate the ValueTracker to rotate theta from 0 to 2*pi
        self.play(theta_tracker.animate.set_value(2 * np.pi), run_time=8, rate_func=linear)

        # Remove updaters to prevent further updates
        pixels.clear_updaters()
        moving_dot.clear_updaters()

        # Hold the final frame
        self.wait(2)
