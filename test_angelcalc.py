import unittest
from anglecalc import AngleCalc


class TestAngleCalc(unittest.TestCase):

    def test_refAngle(self):
        result0 = AngleCalc.refAngle(0)
        self.assertEqual(result0, 0)  # no change

        result1 = AngleCalc.refAngle(90)
        self.assertEqual(result1, 90)  # no change

        result2 = AngleCalc.refAngle(360)
        self.assertEqual(result2, 0)   # edge case

        result3 = AngleCalc.refAngle(630)
        self.assertEqual(result3, 270) # >360 w/ ref angle >180

        result4 = AngleCalc.refAngle(765)
        self.assertEqual(result4, 45)  # >360 w/ ref angle <180

    def test_boundTo180(self):
        result1 = AngleCalc.boundTo180(0)
        self.assertEqual(result1, 0)    # no change, positive

        result2 = AngleCalc.boundTo180(179)
        self.assertEqual(result2, 179)  # no change, edge case

        result3 = AngleCalc.boundTo180(180)
        self.assertEqual(result3, -180) # exception (when angle is 180)

        result4 = AngleCalc.boundTo180(-180)
        self.assertEqual(result4, -180) # exception (when angle is -180)

        result5 = AngleCalc.boundTo180(225)
        self.assertEqual(result5, -135) # positive to negative; reference angle >180

        result6 = AngleCalc.boundTo180(-90)
        self.assertEqual(result6, -90)  # no change, negative

        result7 = AngleCalc.boundTo180(-315)
        self.assertEqual(result7, 45)   # negative to positive; reference angle <180

        result8 = AngleCalc.boundTo180(765)
        self.assertEqual(result8, 45)   # find reference angle; no change in sign

        result9 = AngleCalc.boundTo180(630)
        self.assertEqual(result9, -90)  # find reference angle; change in sign

    def test_isAngleBetween(self):
        self.assertTrue(AngleCalc.isAngleBetween(0, 45, 90))     # True; all angles <180

        self.assertTrue(AngleCalc.isAngleBetween(90, 179, -135)) # True; edge case and negative angle

        self.assertTrue(AngleCalc.isAngleBetween(135, 180, 270)) # True; exception and angle >180

        self.assertFalse(AngleCalc.isAngleBetween(0, 45, 20))    # False; no angle conversion

        self.assertFalse(AngleCalc.isAngleBetween(180, 270, 90)) # False; w/ angle conversion

if __name__ == '__main__':
    unittest.main()
