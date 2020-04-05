#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""远程指令接收节点：keyboard_recv 发布话题: move_cmd
"""

import socket
import rospy
from std_msgs.msg import String


HOST = ''
PORT = 1201
ADDR = (HOST, PORT)


def talker():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print('waiting...')
    client, addr = s.accept()
    print('recevied connection from:{0}:{1}'.format(addr[0], addr[1]))
    temp_cmd = None

    pub = rospy.Publisher('move_cmd', String, queue_size=10)
    rospy.init_node('keyboard_recv', anonymous=True)
    rate = rospy.Rate(30)  # 10hz
    while not rospy.is_shutdown():
        data = client.recv(1024)
        command = data.decode('utf-8')
        if temp_cmd != command:
            temp_cmd = command
            # print(temp_cmd)
        
            rospy.loginfo(temp_cmd)
            pub.publish(temp_cmd)
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
