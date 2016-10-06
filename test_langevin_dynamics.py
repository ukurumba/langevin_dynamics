#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_langevin_dynamics
----------------------------------

Tests for `langevin_dynamics` module.
"""


import sys
import unittest
import numpy as np
from contextlib import contextmanager


from langevin_dynamics import langevin_dynamics




class TestLangevin_dynamics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass
        
    def test_potential_energy_force(self):
        with open('{}'.format('potential_energy_sample')) as potential_energy_vals:
            values = []
            for line in potential_energy_vals: 
                vals = [float(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
                values.append(vals)
            values = np.asarray(values)
            force_1 = langevin_dynamics.potential_energy_force(2.5, values)
            force_2 = langevin_dynamics.potential_energy_force(2,   values)
            self.assertEqual(force_1,-15)
            self.assertEqual(force_2,-12)

    def test_boundary_conditions(self):
        pos1 = langevin_dynamics.position(3, 2, 1, 'potential_energy_sample')
        pos2 = langevin_dynamics.position(3,-4,1,'potential_energy_sample')
        pos3 = langevin_dynamics.position(1,2,1,'potential_energy_sample')
        pos4 = langevin_dynamics.position(3,7,1, 'potential_energy_sample')
        self.assertEqual(pos1, 2)
        self.assertEqual(pos2, 2)
        self.assertEqual(pos3, 3)
        self.assertEqual(pos4, 4)


    def test_output(self):
        position_and_velocity = langevin_dynamics.langevin_simulation(1, 1, 10, 1, .1, 20, 2, 'potential_energy_sample')
        position_and_velocity_2 = langevin_dynamics.langevin_simulation(1, -10, 10, 1, .1, 20, 2, 'potential_energy_sample')
        position_and_velocity_3 = langevin_dynamics.langevin_simulation(1.9, 30, 10, 1, .1, 50, 2, 'pot_example_expanded.txt')
        self.assertIsInstance(position_and_velocity, tuple)
        self.assertIsInstance(position_and_velocity_2,tuple)
        self.assertIsInstance(position_and_velocity_3,tuple)
        self.assertIsInstance(position_and_velocity_3[0],float)
        self.assertIsInstance(position_and_velocity_3[1],float)



        
        
tests = unittest.TestLoader().loadTestsFromTestCase(TestLangevin_dynamics)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())
