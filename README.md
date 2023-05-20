# Local Maxima Analysis of Firing Rates

This code analyzes the firing rates of a neuron and identifies the local maxima in the rate data. It plots the firing rate over time and marks the local maxima points on the graph.

## Dependencies
- Python 3.x
- numpy
- matplotlib

## Dataset
The code loads the firing rate data from a text file named `rates.txt`. The firing rates represent the activity level of a neuron over time.

## Local Maxima Detection
The code iterates through the firing rate data and compares each rate to its previous and next rates. If a rate is higher than both its neighbors, it is considered a local maximum. The code stores a `1` in the `local_max` array at the corresponding timestamp if a local maximum is found; otherwise, it stores a `0`.

## Plotting
The code generates a plot of the firing rate over time using the `rates` data. It also creates a subplot on the same graph to display the extracted local maxima points. The local maxima points are represented as blue dots on the graph.

## Execution Time
The code uses the `%%time` magic command to measure the execution time of the entire cell. The elapsed time will be displayed when running the code.

## Usage
To use this code, ensure that the required dependencies are installed. Provide the firing rate data in the `rates.txt` file or update the code to load your own data. Run the code, and it will display the firing rate graph with local maxima marked. The execution time of the cell will be printed as well.

Feel free to modify the code to adapt it to different datasets or customize the plot appearance according to your needs.
