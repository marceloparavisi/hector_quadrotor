#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from hector_uav_msgs.msg import MotorPWM 

def talker():
    pub = rospy.Publisher('motor_pwm', MotorPWM, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1000) # 10hz
    while not rospy.is_shutdown():
	_motorPWM = MotorPWM();
	_motorPWM.header.stamp =rospy.Time.now();
	_motorPWM.header.frame_id="world";
	_motorPWM.pwm = [250,250,250,250];
        pub.publish(_motorPWM)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
