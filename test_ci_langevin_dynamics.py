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
from click.testing import CliRunner

from langevin_dynamics import langevin_dynamics
from langevin_dynamics import cli



class TestLangevin_dynamics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'langevin_dynamics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
        
    def test_potential_energy_force(self):
        with open('{}'.format('potential_energy_sample')) as potential_energy_vals:
            values = []
            for line in potential_energy_vals: 
                vals = [float(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
                values.append(vals)
            values = np.asarray(values)
            force = langevin_dynamics.potential_energy_force(2.5, values)
            self.assertEqual(force,-15)

    def test_boundary_conditions(self):
        pos1 = langevin_dynamics.position(3, 2, 1, 'potential_energy_sample')
        pos2 = langevin_dynamics.position(3,-4,1,'potential_energy_sample')
        self.assertEqual(pos1, 2)
        self.assertEqual(pos2, 2)


    def test_output(self):
        position_and_velocity = langevin_dynamics.langevin_simulation(1, 1, 10, 1, .1, 20, 'potential_energy_sample', 2)
        position_and_velocity_2 = langevin_dynamics.langevin_simulation(1, -10, 10, 1, .1, 20, 'potential_energy_sample', 2)
        self.assertIsInstance(position_and_velocity, tuple)
        self.assertIsInstance(position_and_velocity_2,tuple)


        
        
tests = unittest.TestLoader().loadTestsFromTestCase(TestLangevin_dynamics)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())
