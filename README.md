# Data-Visualization
A python program to generate data sets and create visualizations of that data using Matplotlib.

# Note
When you give plot() a sequence of numbers, it assumes the first data point corresponds to an x-coordinate value of 0, but our first point corresponds to an x-value of 1. We can override the default behavior by giving plot() the input and output values used to calculate the squares.
For colormaps, You can see all the colormaps available in pyplot at https://matplotlib.org/; go to Examples, scroll down to Color, and click Colormap reference.

# Plotting and Styling Individual Points with scatter()
Sometimes, it’s useful to plot and style individual points based on certain characteristics. For example, you might plot small values in one color and larger values in a different color. You could also plot a large data set with one set of styling options and then emphasize individual points by replotting them with different options. To plot a single point, use the scatter() method. Pass the single (x, y) values of the point of interest to scatter() to plot those values.

# Defining Custom Colors
You can also define custom colors using the RGB color model. To define a color, pass the c argument a tuple with three decimal values (one each for red, green, and blue in that order), using values between 0 and 1. For example, the following line creates a plot with light-green dots:
"ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)"
Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.
