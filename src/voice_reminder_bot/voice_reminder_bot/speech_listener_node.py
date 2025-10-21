import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SpeechListener(Node):
    def __init__(self):
        super().__init__('speech_listener_node')
        self.publisher_ = self.create_publisher(String, 'voice_reminders', 10)
        self.get_logger().info('Speech Listener Node Started')
        self.timer = self.create_timer(5.0, self.publish_dummy_reminder)

    def publish_dummy_reminder(self):
        msg = String()
        msg.data = 'Reminder: Drink water'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SpeechListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
