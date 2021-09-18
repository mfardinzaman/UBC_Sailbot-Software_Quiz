import unittest
from anglecalc import *

class TestAngleCalc(unittest.TestCase):

    def test_refAngle(self):
        result1 = refAngle(90)
        self.assertEqual(result1, 90)  # no change

        result2 = refAngle(360)
        self.assertEqual(result2, 0)   # edge case

        result3 = refAngle(630)
        self.assertEqual(result3, 270) # >360 w/ ref angle >180

        result4 = refAngle(765)
        self.assertEqual(result4, 45)  # >360 w/ ref angle <180

    def test_boundTo180(self):
        result1 = AngleCalc.boundTo180(self, 0)
        self.assertEqual(result1, 0)    # no change, positive

        result2 = AngleCalc.boundTo180(self, 179)
        self.assertEqual(result2, 179)  # no change, edge case

        result3 = AngleCalc.boundTo180(self, 180)
        self.assertEqual(result3, -180) # exception (when angle is 180)

        result4 = AngleCalc.boundTo180(self, -180)
        self.assertEqual(result4, -180) # exception (when angle is -180)

        result5 = AngleCalc.boundTo180(self, 225)
        self.assertEqual(result5, -135) # positive to negative; reference angle >180

        result6 = AngleCalc.boundTo180(self, -90)
        self.assertEqual(result6, -90)  # no change, negative

        result7 = AngleCalc.boundTo180(self, -315)
        self.assertEqual(result7, 45)   # negative to positive; reference angle <180

        result8 = AngleCalc.boundTo180(self, 765)
        self.assertEqual(result8, 45)   # find reference angle; no change in sign

        result9 = AngleCalc.boundTo180(self, 630)
        self.assertEqual(result9, -90)  # find reference angle; change in sign

    def test_isAngleBetween(self):
        self.assertTrue(AngleCalc.isAngleBetween(self, 0, 45, 90))     # True; all angles <180

        self.assertTrue(AngleCalc.isAngleBetween(self, 90, 179, -135)) # True; edge case and negative angle

        self.assertTrue(AngleCalc.isAngleBetween(self, 135, 180, 270)) # True; exception and angle >180

        self.assertFalse(AngleCalc.isAngleBetween(self, 0, 45, 20))    # False; no angle conversion

        self.assertFalse(AngleCalc.isAngleBetween(self, 180, 270, 90)) # False; w/ angle conversion
