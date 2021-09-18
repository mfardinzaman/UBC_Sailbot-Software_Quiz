def refAngle(angle):
    '''
    Bounds the provided angle in degrees between
    :param angle:
    :return:
    '''
    return (360 + angle % 360) % 360

class AngleCalc:

    def boundTo180(self, angle):
        '''
        Bounds the provided angle in degrees between [-180, 179] degrees
        :param angle: float
        :return: float
        '''
        angle = refAngle(angle)
        if angle == 180:
            angle = -180
        elif angle > 180:
            angle = angle % -180
        return angle

    def isAngleBetween(self, first_angle, middle_angle, second_angle):
        '''
        Determines whether middle_angle is in between two bounding angles
        :param first_angle: float
        :param middle_angle: float
        :param second_angle: float
        :return: bool
        '''
        first_angle = refAngle(first_angle)
        middle_angle = refAngle(middle_angle)
        second_angle = refAngle(second_angle)

        return first_angle < middle_angle and middle_angle < second_angle