from unittest import TestCase
import logging
logging.basicConfig(level=logging.DEBUG)
from numpy.testing import assert_almost_equal

from fracPy.ExperimentalData.ExperimentalData import ExperimentalData
from fracPy.Optimizable.Optimizable import Optimizable

class TestOptimizable(TestCase):
    def setUp(self):
        # first, create a ExperimentalData dataset
        data = ExperimentalData('test:nodata')
        data.wavelength = 1234
        optimizable = Optimizable(data)
        self.data = data
        self.optimizable = optimizable

    def test_copyAttributesFromExperiment(self):
        self.check_scalar_property()
        self.check_array_property()

    def check_scalar_property(self):

        # check that the wavelength is properly copied
        self.assertEqual(self.optimizable.wavelength, self.data.wavelength)
        # now if we change it, it should no longer be the same
        self.optimizable.wavelength = 4321
        self.assertNotEqual(self.optimizable.wavelength, self.data.wavelength)

    def check_array_property(self):
        """
        Arrays are passed by reference by default. Check that they are properly copied as well
        :return:
        """
        assert_almost_equal(self.optimizable.positions, self.data.positions)
        self.optimizable.positions += 1
        assert_almost_equal(self.optimizable.positions - 1, self.data.positions)

