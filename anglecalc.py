class AngleCalc:
    @staticmethod
    def refAngle(angle):
        '''
        Finds the reference angle [0, 369] for a given angle
        :param angle: float
        :return: float
        '''
        return (360 + angle % 360) % 360

    @staticmethod
    def boundTo180(angle):
        '''
        Bounds the provided angle in degrees between [-180, 179] degrees
        :param angle: float
        :return: float
        '''
        angle = AngleCalc.refAngle(angle)
        if angle == 180:
            angle = -180
        elif angle > 180:
            angle = angle % -180
        return angle

    @staticmethod
    def isAngleBetween(first_angle, middle_angle, second_angle):
        '''
        Determines whether middle_angle is in between two bounding angles
        :param first_angle: float
        :param middle_angle: float
        :param second_angle: float
        :return: bool
        '''
        first_angle = AngleCalc.refAngle(first_angle)
        middle_angle = AngleCalc.refAngle(middle_angle)
        second_angle = AngleCalc.refAngle(second_angle)

        return first_angle < middle_angle and middle_angle < second_angle