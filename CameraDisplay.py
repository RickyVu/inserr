import roslibpy
import cv2
import numpy as np
import base64
import time

def image_callback(msg):
    try:
        height, width = msg["height"], msg["width"]
        image_bytes = base64.b64decode(msg['data'])
        np_array = np.frombuffer(image_bytes, np.uint8).reshape((height, width, 3))
        cv2.imshow('ROS Image', np_array)
        cv2.waitKey(1)
    except Exception as e:
        print(e)

def main():
    client = roslibpy.Ros(host='localhost', port=9090)
    client.run()

    subscriber = roslibpy.Topic(client, '/inserr/cam/stream', 'sensor_msgs/Image')#'sensor_msgs/CompressedImage')#'std_msgs/ByteMultiArray')#'sensor_msgs/Image')
    subscriber.subscribe(image_callback)

    try:
        while True:
            cv2.waitKey(1)
    except KeyboardInterrupt:
        subscriber.unsubscribe()
        client.terminate()

if __name__ == '__main__':
    main()