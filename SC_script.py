import numpy as np
import matplotlib.pyplot as plt

# data1 = [0., 1., 2., 3., 4., 5., 6., 7., 8.,]
# NO! This wasn't right. Try this instead:
data1 = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])

data2 = np.array([3., 6., 9., 12., 15., 18., 21., 24., 27.])

measurement_points = np.array([0., 10., 30., 32., 34., 36., 38., 40., 60.])
# NOTE: CHECK ME

assert len(data1) == len(data2), 'datasets differ in length'
assert len(data1) == len(measurement_points), 'datasets differ in length'

# Task 1.
# calculate a weighted mean of the data items
# weighted_median_of_data1 = np.median(data1)
# weight of data2 is twice data1.
weighted_mean_of_data = data1 + 2. * data2 / 3.

# Task 2.
# calculate a moving average of the data items
# we can use convolve for this
# let's try a window of 5
window_width = 3
convolution_vector = np.ones((window_width, )) / window_width
# ^^if we convolve the vector with this, we will get a moving average
convolved_data1 = np.convolve(data1, convolution_vector)
# but actually there's an edge effect transient present in the first items, so
convolved_data1 = convolved_data1[(window_width - 1):-(window_width - 1)]

# paste in the same thing as above to do the same for data2:
convolved_data2 = np.convolve(data1, convolution_vector)
convolved_data2 = convolved_data2[(window_width - 1):-(window_width - 1)]

# do these look right?
plt.plot(measurement_points[1:-1], convolved_data1)
plt.plot(measurement_points[1:-1], convolved_data2)
plt.show()

# Task 3.
# Calculate a spatially explicit mean for the averaged data we calculated above
# i.e., account for data spacing when taking a mean
# conceptualise as a histogram-like box centred on each data point
# get the measurement points in order and create the boxes:
in_order = np.argsort(measurement_points)
locations_in_order = measurement_points[in_order]
window_widths = np.empty_like(locations_in_order)
mean_positions_betw_data = (
    locations_in_order[1:] + locations_in_order[:-1]
) / 2.
window_widths[1:-1] = (
    mean_positions_betw_data[1:] - mean_positions_betw_data[:-1]
)
# deal with the edge cases: just treat symmetrically:
halfwidth_low = mean_positions_betw_data[0] - locations_in_order[0]
window_widths[0] = halfwidth_low * 2.
halfwidth_high = mean_positions_betw_data[-1] - locations_in_order[-1]
window_widths[-1] = halfwidth_high * 2.

total_width = np.sum(window_widths)

# create a list to store the data:
mymeans = []
for data in (data1, data2):
    data_in_order = data[in_order]
    # now do the mean
    area = np.sum(window_widths * data_in_order)
    mean = area / total_width
    mymeans.append(mean)

mean1 = mymeans[0]
mean2 = mymeans[1]
