import rospy
from std_msgs.msg import String

rospy.init_node('node1')
message = 'Iniciando...'

def receive_message(message_param):
    global message
    message = message_param.data

def timerCallBack(event):
    print(message)
    msg = String()
    msg.data = '2017011881'
    pub.publish(msg)

pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, receive_message)

rospy.spin()
