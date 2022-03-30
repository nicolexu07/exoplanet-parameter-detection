import unittest
import tools
import nose.tools as nt
import numpy as np

class test_tools(unittest.TestCase):
    def test_solve_for_u(self):
        e = np.random.uniform(0, 1)
        T = np.random.uniform(3282.3503, 3.46896e13)
        tau = n.random.uniform(3282.3503, 3.46896e13)

        #when t=tau we expect u=0
        #numerical solver gives approximately 0
        temp = solve_for_u(tau, tau, T, e)
        self.assertAlmostEqual(0, temp)

        e = 0
        t = np.random.uniform(0, T)
        temp = solve_for_u(t, tau, T, e)
        #when e=0 the function is linear
        self.assertAlmostEqual(2*np.pi*(t-tau)/T, temp)
