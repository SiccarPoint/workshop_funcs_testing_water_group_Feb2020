import numpy as np
import matplotlib.pyplot as plt

# we will move this to the bottom
# # data1 = [0., 1., 2., 3., 4., 5., 6., 7., 8.,]
# data1 = [1., 2., 3., 4., 5., 6., 7., 8., 9.]
#
# data2 = [3., 6., 9., 12., 15., 18., 21., 24., 27.]
#
# measurement_points = [0., 10., 30., 32., 34., 36., 38., 40., 60.]
#
# assert len(data1) == len(data2), 'datasets differ in length'
# assert len(data1) == len(measurement_points), 'datasets differ in length'

# Task 1.
# calculate a weighted mean of the data items
def weighted_mean(dataset1, dataset2, weight1, weight2):
    """Calculate a weighted mean of the input datasets.

    Parameters
    ----------
    dataset1 : length n array or array-like
        The first dataset
    dataset2 : length n array or array-like
        The second dataset
    weight1 : float
        The weight to apply to dataset1
    weight2 : float
        The weight to apply to dataset2

    Returns
    -------
    weighted_mean_of_data : length n array
        The weighted mean of the datasets
    """  # three speech marks/apostrophes starts a multi-line text block
    d1 = np.array(dataset1)
    d2 = np.array(dataset2)
    assert d1.size == d2.size, 'datasets differ in length'
    weighted_mean_of_data = weight1 * d1 + weight2 * d2 / (weight1 + weight2)
    return weighted_mean_of_data

# Task 2.
# calculate a moving average of the data items
def moving_average(dataset, window_width=3):
    """
    Calculate a moving average with window width window_width across the data.

    Parameters
    ----------
    dataset : length n array or array-like
        The data on which to perform the moving average
    window_width : int
        The window width over which to average

    Returns
    -------
    convolved_data : length n - (window_width - 1) array
        The moving average data, with the transients at the start and end of
        the array removed.
    """
    assert type(window_width) is int, "type of window_width must be int!"
    # we can use convolve for this
    d = np.array(dataset)
    convolution_vector = np.ones((window_width, )) / window_width
    # ^^if we convolve the vector with this, we will get a moving average
    convolved_data = np.convolve(d, convolution_vector)
    # but actually there's an edge effect transient present in the first items:
    convolved_data = convolved_data[(window_width - 1):-(window_width - 1)]
    return convolved_data


# We'll put this at the bottom after our funcs
# # do these look right?
# plt.plot(measurement_points[2:], convolved_data1)
# plt.plot(measurement_points[2:], convolved_data2)
# plt.show()

# Task 3.
# Calculate a spatially explicit mean for the averaged data we calculated above
def spatial_mean(dataset, measurement_points):
    """
    Calculate a spatially explicit mean for dataset, that accounts for data
    spacing. The spacing at the ends of the array is treated symmetrically
    around the final datapoint.

    Parameters
    ----------
    dataset : length n array or array-like
        The data on which to perform the spatial averaging
    measurement_points : length n array or array-like
        The 1D positions of the points

    Returns
    -------
    spatial_mean : length n array
        The spatial mean of the data
    """
    assert len(dataset) == len(measurement_points), (
        'dataset and measurement_points are different lengths!'
    )
    # conceptualise as a histogram-like box centred on each data point
    # get the measurement points in order and create the boxes:
    d = np.array(dataset)
    pts = np.array(measurement_points)
    in_order = np.argsort(pts)
    locations_in_order = pts[in_order]
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
    halfwidth_high =  locations_in_order[-1] - mean_positions_betw_data[-1]
    window_widths[-1] = halfwidth_high * 2.
    total_width = np.sum(window_widths)
    data_in_order = d[in_order]
    # now do the mean
    area = np.sum(window_widths * data_in_order)
    spatial_mean = area / total_width
    return spatial_mean


print("this statement will never get printed")
# ...because it isn't in the code block below


if __name__ == '__main__':
    # Anything you write after this weird thing gets run if the file is run
    # as if it was just a script:
    data1 = [1., 2., 3., 4., 5., 6., 7., 8., 9.]
    data2 = [3., 6., 9., 12., 15., 18., 21., 24., 27.]
    measurement_points = [0., 10., 30., 32., 34., 36., 38., 40., 60.]

    wgtd_mean = weighted_mean(data1, data2, 1., 2.)

    convolved_data1 = moving_average(data1)
    convolved_data2 = moving_average(data2)

    plt.plot(measurement_points[1:-1], convolved_data1)
    plt.plot(measurement_points[1:-1], convolved_data2)

    mean1 = spatial_mean(data1, measurement_points)
    mean2 = spatial_mean(data2, measurement_points)

    plt.show()
