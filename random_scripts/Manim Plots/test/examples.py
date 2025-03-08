from manim import *
from manim.utils.color import ManimColor
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class LineBetweenPoints(Scene):
    def construct(self):
        # Define points A and B
        point_A = np.array([-2, -1, 0])
        point_B = np.array([2, 1, 0])

        # Create a line from point A to point B
        line = Line(start=point_A, end=point_B, color=BLUE)

        # Create dots at points A and B
        dot_A = Dot(point=point_A, color=RED)
        dot_B = Dot(point=point_B, color=GREEN)

        # Add the line and dots to the scene
        self.add(line, dot_A, dot_B)

        # Optionally, add labels to the points
        label_A = Text("A").next_to(dot_A, DOWN)
        label_B = Text("B").next_to(dot_B, UP)
        self.add(label_A, label_B)

        # Hold the final frame for a moment
        self.wait(1)

class VectorAnimation(Scene):
    def construct(self):
        # Create a number plane for reference
        plane = NumberPlane()
        self.add(plane)

        # Define the initial and target vectors
        initial_vector = Vector([1, 2], color=BLUE)
        target_vector = Vector([3, -1], color=RED)

        # Add the initial vector to the scene
        self.add(initial_vector)

        # Animate the transformation from the initial to the target vector
        self.play(Transform(initial_vector, target_vector))

        # Hold the final frame for a moment
        self.wait(1)

class LineBetweenPoints(Scene):
    def construct(self):
        # Define points A and B
        point_A = np.array([-2, -1, 0])
        point_B = np.array([2, 1, 0])

        # Create a line from point A to point B
        line = Line(start=point_A, end=point_B, color=BLUE)

        # Create dots at points A and B
        dot_A = Dot(point=point_A, color=RED)
        dot_B = Dot(point=point_B, color=GREEN)

        # Add the line and dots to the scene
        self.add(line, dot_A, dot_B)

        # Optionally, add labels to the points
        label_A = Text("A").next_to(dot_A, DOWN)
        label_B = Text("B").next_to(dot_B, UP)
        self.add(label_A, label_B)

        # Hold the final frame for a moment
        self.wait(1)

class GridExample(Scene):
    def construct(self):
        # Create a NumberPlane instance
        grid = NumberPlane(
            x_range=[-10, 10, 1],  # X-axis range with step size
            y_range=[-6, 6, 1],    # Y-axis range with step size
            axis_config={"color": BLUE},  # Axis color
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )

        # Add the grid to the scene
        self.add(grid)

        # Optionally, add labels to the axes
        x_label = grid.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = grid.get_y_axis_label("y", edge=UP, direction=UP, buff=0.2)
        self.add(x_label, y_label)

        # Hold the final frame for a moment
        self.wait(1)


class VectorGrid(Scene):
    def construct(self):
        
        #creating the gridx#
        grid = NumberPlane(
            x_range=[-10, 10, 1],  # X-axis range with step size
            y_range=[-6, 6, 1],    # Y-axis range with step size
            axis_config={"color": BLUE},  # Axis color
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )

        # Add the grid to the scene
        self.add(grid)

        # Optionally, add labels to the axes
        x_label = grid.get_x_axis_label("Re", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = grid.get_y_axis_label("Im", edge=UP, direction=UP, buff=0.2)
        self.add(x_label, y_label)


        # Define points A and B
        point_A = np.array([-2, -1, 0])
        point_B = np.array([2, 1, 0])

        # Create a line from point A to point B
        line = Line(start=point_A, end=point_B, color=BLUE)

        # Create dots at points A and B
        dot_A = Dot(point=point_A, color=RED)
        dot_B = Dot(point=point_B, color=GREEN)

        # Add the line and dots to the scene
        self.add(line, dot_A, dot_B)

        # Optionally, add labels to the points
        label_A = Text("A").next_to(dot_A, DOWN)
        label_B = Text("B").next_to(dot_B, UP)
        self.add(label_A, label_B)

        # Hold the final frame for a moment
        self.wait(1)


class ComplexFunctionHuePlot(Scene):
    def construct(self):
        # Define the complex function
        def complex_function(z):
            return np.sqrt(z**2 -1)  

        # Create a grid of points in the complex plane
        resolution = 100  # Number of points along each axis
        x_min, x_max = -10,10
        y_min, y_max = -10, 10
        x_values = np.linspace(x_min, x_max, resolution)
        y_values = np.linspace(y_min, y_max, resolution)

        # Generate the background by coloring each point
        pixels = VGroup()
        for x in x_values:
            for y in y_values:
                z = complex(x, y)
                fz = complex_function(z)
                hue = (np.angle(fz) + np.pi) / (2 * np.pi)  # Normalize to [0, 1]
                # Create color using ManimColor from HSV
                color = ManimColor.from_hsv((hue, 1, 0.5))
                pixel = Square(side_length=(x_max - x_min) / resolution)
                pixel.set_fill(color, opacity=1)
                pixel.set_stroke(width=0)
                pixel.move_to([x, y, 0])
                pixels.add(pixel)

        # Add the colored background to the scene
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


        #creating the vectors#
        z = np.array([0,2, 0])
        
        #branch points#
        A = np.array([-1,0,0])
        B = np.array([1,0,0])

        # Create a line from point z to point A
        line1 = Line(start=z, end=A, color=BLUE)

        # Create a line from point z to point A
        line2 = Line(start=z, end=B, color=BLUE)

        # Create dots at points A and B
        dot_z = Dot(point=z, color=RED)
        dot_a = Dot(point=A, color=GREEN)
        dot_b = Dot(point=B, color=GREEN)

        # Add the line and dots to the scene
        self.add(line1,dot_z, dot_a)
        self.add(line2,dot_z, dot_b)

        # Optionally, add labels to the points
        label_A = Text("A").next_to(dot_a, DOWN)
        label_B = Text("B").next_to(dot_b, UP)
        label_z = Text("z").next_to(dot_z, UP)
        self.add(label_A, label_B,label_z)



        # Hold the final frame
        self.wait(2)
