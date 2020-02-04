import numpy as np
import pytest
from .weighted_mean import weighted_mean  # no dot if no __init__.py

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


def test_weighted_mean_lists():
    """Test response for supplied lists
    """
    data1 = [1., 2., 3.]
    data2 = [2., 3., 4.]
    w1 = 4.
    w2 = 2.
    with pytest.raises(TypeError):
        out = weighted_mean(data1, data2, w1, w2)


def test_weighted_mean_zeros():
    """Test response for supplied lists
    """
    data1 = np.array([1., 2., 3.])
    data2 = np.array([2., 3., 4.])
    w1 = 0.
    w2 = 0.
    out = weighted_mean(data1, data2, w1, w2)
