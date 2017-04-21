'''
===================================================
Case Study 1 - Scotch Wishkies Analysis Using Bokeh
===================================================
'''

#In this case study, we have prepared step-by-step instructions for you on how 
#to prepare plots in Bokeh, a library designed for simple interactive plotting. 
#We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

#----------------------------------------------------------------------------------------------------------------

# Exercise 1
#-----------

#Here we provide a basic demonstration of an interactive grid plot using Bokeh. 
#Execute the following code and follow along with the comments. We will later 
#adapt this code to plot the correlations among distillery flavor profiles as 
#well as plot a geographical map of distilleries colored by region and flavor 
#profile.

#Make sure to study this code now, as we will edit similar code in the 
#exercises that follow.

#Once you have plotted the code, hover, click, and drag your cursor on the plot 
#to interact with it. Additionally, explore the icons in the top-right corner 
#of the plot for more interactive options!

# First, we import a tool to allow text to pop up on a plot when the cursor
# hovers over it.  Also, we import a data structure used to store arguments
# of what to plot in Bokeh.  Finally, we will use numpy for this section as well!

from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Let's plot a simple 5x5 grid of squares, alternating in color as red and blue.

plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# How do we tell Bokeh to plot each point in a grid?  Let's use a function that
# finds each combination of values from 1-5.
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)


#------------------------------------------------------------------------------

# Exercise 2
#-----------


#Let's create the names and colors we will use to plot the correlation matrix 
#of whisky flavors. Later, we will also use these colors to plot each distillery 
#geographically. Create a dictionary region_colors with regions as keys 
#and cluster_colors as values.

cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = dict(zip(regions,cluster_colors))

#Print region_colors.

print(region_colors)

#------------------------------------------------------------------------------

# Exercise 3
#-----------

#correlations is a two-dimensional np.array with both rows and columns 
#corresponding to distilleries and elements corresponding to the flavor 
#correlation of each row/column pair. Let's define a list correlation_colors, 
#with string values corresponding to colors to be used to plot each distillery 
#pair. Low correlations among distillery pairs will be white, high correlations 
#will be a distinct group color if the distilleries from the same group, and 
#gray otherwise. Edit the code to define correlation_colors for each distillery 
#pair to have input 'white' if their correlation is less than 0.7.

#whisky.Group is a pandas dataframe column consisting of distillery group 
#memberships. For distillery pairs with correlation greater than 0.7, if they 
#share the same whisky group, use the corresponding color from cluster_colors. 
#Otherwise, the correlation_colors value for that distillery pair will be 
#defined as 'lightgray'.

distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i,j] < .70:                    # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if whisky.Group[i] == whisky.Group[j]:     # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.

#------------------------------------------------------------------------------

# Exercise 4
#-----------

#We will edit the following code to make an interactive grid of the correlations 
#among distillery pairs using correlation_colors and correlations. 
#correlation_colors is a list of each distillery pair. To convert correlations 
#from a np.array to a list, we will use the flatten method. Define the color 
#of each rectangle in the grid using to correlation_colors.

#Define the alpha (transparency) values using correlations.flatten().

#Define correlations and using correlations.flatten(). When the cursor hovers 
#over a rectangle, this will output the distillery pair, show both distilleries 
#as well as their correlation coefficient.

source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "alphas": correlations.flatten(),
        "correlations": correlations.flatten(),
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(title="Whisky Correlations",
    x_axis_location="above", tools="resize,hover,save",
    x_range=list(reversed(distilleries)), y_range=distilleries)
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3

fig.rect('x', 'y', .9, .9, source=source,
     color='colors', alpha='alphas')
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}
show(fig)
#------------------------------------------------------------------------------

# Exercise 5
#-----------

#Next, we provide an example of plotting points geographically. 
#Run the following code, to be adapted in the next section. 
#Compare this code to that used in plotting the distillery correlations.

points = [(0,0), (1,2), (3,1)]
xs, ys = zip(*points)
colors = ["red", "blue", "green"]

output_file("Spatial_Example.html", title="Regional Example")
location_source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
    }
)

fig = figure(title = "Title",
    x_axis_location = "above", tools="resize, hover, save")
fig.plot_width  = 300
fig.plot_height = 380
fig.circle("x", "y", 10, 10, size=10, source=location_source,
     color='colors', line_color = None)

hover = fig.select(dict(type = HoverTool))
hover.tooltips = {
    "Location": "(@x, @y)"
}
show(fig)


#------------------------------------------------------------------------------

# Exercise 6
#-----------

#Adapt the given code from the beginning to show(fig) in order to define a 
#function location_plot(title, colors). This function takes a string title
# and a list of colors corresponding to each distillery and outputs a Bokeh 
#plot of each distillery by latitude and longitude. As the cursor hovers over 
#each point, it displays the distillery name, latitude, and longitude.

def location_plot(title, colors):
    output_file(title+".html")
    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title = title,
        x_axis_location = "above", tools="resize, hover, save")
    fig.plot_width  = 400
    fig.plot_height = 500
    fig.circle("x", "y", 10, 10, size=9, source=location_source,
         color='colors', line_color = None)
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type = HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }
    show(fig)
    
#whisky.Region is a pandas column containing the regional group membership for 
#each distillery. Make a list consisting of the value of region_colors for 
#each distillery, and store this list as region_cols.

region_cols = [region_colors[i] for i in list(whisky["Region"])]

#Use location_plot to plot each distillery, colored by its regional grouping. 

location_plot("Whisky Locations and Regions", region_cols)  

#------------------------------------------------------------------------------

# Exercise 7
#-----------

#Use list comprehensions to create the list region_cols consisting of the color
# in region_colors that corresponds to each whisky in whisky.Region.

region_cols = [region_colors[i] for i in whisky['Region']]

#Similarly, create a list classification_cols consisting of the color in 
#cluster_colors that corresponds to each cluster membership in whisky.Group.

classification_cols = [cluster_colors[j] for j in whisky['Group']]

#location_plot remains stored from the previous exercise. Use it to create two 
#interactive plots of distilleries, one colored by defined region called 
#region_cols and the other with colors defined by coclustering designation 
#called classification_cols. How well do the coclustering groupings match the 
#regional groupings?

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)


'''
We see that there is not very much overlap between the regional classifications 
and the coclustering classifications. This means that regional classifications 
are not a very good guide to Scotch whisky flavor profiles.
'''
#------------------------------------------------------------------------------