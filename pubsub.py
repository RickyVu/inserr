# WORK IN PROGRESS. IGNORE THIS FILE

import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
subscriber = roslibpy.Topic(client, '/inserr/cam/stream', 'sensor_msgs/Image')
subscriber.subscribe(image_callback)

subscriber.unsubscribe()
client.terminate()

import rospy
rospy.init_node('listener', anonymous=True)
rospy.Subscriber("chatter", String, callback)

# init_node = roslibpy.Ros
def myhook():
  pass

rospy.on_shutdown(myhook)

String = ''

class rospyInterface:
    def __init__(self, host='localhost', port=9090):
       self.client = roslibpy.Ros(host, port)

    # practically useless in roslibpy
    def init_node(self, name, anonymous):
       pass

    def Subscriber(self, topic, message_type, callback):
       self.subscriber = roslibpy.Topic(self.client, topic, message_type)
