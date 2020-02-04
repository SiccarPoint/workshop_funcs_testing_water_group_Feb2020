import pytest
import numpy as np
from ..SC_script_funcs_examples import weighted_mean


def test_weighted_mean_zero():
    d1 = [0., 1., 2.]
    d2 = [0., 3., 5.]
    assert np.allclose(weighted_mean(d1, d2, 0., 2.), d2)


def test_weighted_mean_arbitrary():
    d1 = [0, 0., 0., 0.]
    d2 = [0, 5., 10., 15.]
    assert np.allclose(weighted_mean(d1, d2, 1., 4.),
                       np.array([0.,  4.,  8., 12.]))


def test_weighted_mean_different_input_types():
    d = [0., 1., 2.]
    for tp in (list, tuple, np.array):
        out = weighted_mean(tp(d), d, 1., 1.)
        assert type(out) is np.ndarray


def test_weighted_mean_different_lengths():
    d1 = [0., 1., 2.]
    d2 = [0., 1., 2., 3.]
    with pytest.raises(AssertionError):
        weighted_mean(d1, d2, 1., 1.)
