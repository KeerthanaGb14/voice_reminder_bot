import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Notifier(Node):
    def __init__(self):
        super().__init__('notifier_node')
        self.subscription = self.create_subscription(
            String,
            'voice_reminders',
            self.send_notification,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Notifier Node Started')

    def send_notification(self, msg):
        # Here you can integrate actual notifications (sound, pop-up, etc.)
        self.get_logger().info(f'Notification: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Notifier()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
