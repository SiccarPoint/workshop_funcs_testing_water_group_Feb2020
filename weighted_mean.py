import numpy as np

def weighted_mean(dataset1, dataset2,
                  weight1=1., weight2=5.):
    """Calculate a weighted mean of data items.
    """
    weighted_mean = ((weight1 * dataset1
                      + weight2 * dataset2)
                     / (weight1 + weight2))
    return weighted_mean


def test_weighted_mean():
    """Test answer for simple weighted mean.
    """
    data1 = np.array([1., 2., 3.])
    data2 = np.array([2., 3., 4.])
    w1 = 4.
    w2 = 2.
    ans = np.array([4./3., 7./3., 10./3.])
    out = weighted_mean(data1, data2, w1, w2)

    assert np.allclose(out, ans)
