from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create one D6 die.
die = Die()

# Make some rolls, and store results in a list.
results = []
num_of_rolls = 1000
for roll_num in range(num_of_rolls):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title=f'Results of rolling one D6 {num_of_rolls} times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')