import rospy
from std_msgs.msg import String

rospy.init_node('node2')

matricula='0'

def receive_msg(received):
    global matricula
    matricula = received.data

sub = rospy.Subscriber('/topic1', String, receive_msg)

def timerCallBack(event):
    total = 0
    for number in matricula:
        total +=int(number)
    msg = String()
    msg.data = str(total)
    pub.publish(msg)

pub = rospy.Publisher('/topic2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
