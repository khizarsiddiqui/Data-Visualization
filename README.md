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

# Random Walk
The main part of the fill_walk() method tells Python how to simulate four random decisions: will the walk go right or left? How far will it go in that direction? Will it go up or down? How far will it go in that direction?

# Styling The Walk
We’ll customize our plots to emphasize the important characteristics of each walk and deemphasize distracting elements. To do so, we identify the characteristics we want to emphasize, such as where the walk began, where it ended, and the path taken. Next, we identify the characteristics to deemphasize, such as tick marks and labels. The result should be a simple visual representation that clearly communicates the path taken in each random walk. To color the points according to their position in the walk, we pass the c argument a list containing the position of each point. Because the points are plotted in order, the list just contains the numbers from 0 to 4999.

# Altering the Size to Fill the Screen
Matplotlib assumes that your screen resolution is 100 pixels per inch;if this code doesn’t give you an accurate plot size, adjust the numbers as necessary. Or, if you know your system’s resolution, pass plt.subplots() the resolution using the dpi parameter to set a plot size that makes effective use of the space available on your screen, as "fig, ax = plt.subplots(figsize=(10, 6), dpi=128)"

# Rolling Dice
The __init__() method takes one optional argument. With the Die class, when an instance of our die is created, the number of sides will always be six if no argument is included. If an argument is included, that value will set the number of sides on the die. (Dice are named for their number of sides: a six-sided die is a D6, an eight-sided die is a D8, and so on.) The roll() method uses the randint() function to return a random number
between 1 and the number of sides. This function can return the starting value (1), the ending value (num_sides), or any integer between the two.
