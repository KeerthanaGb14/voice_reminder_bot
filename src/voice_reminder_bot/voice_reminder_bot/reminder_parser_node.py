import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReminderParser(Node):
    def __init__(self):
        super().__init__('reminder_parser_node')
        self.subscription = self.create_subscription(
            String,
            'voice_reminders',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Reminder Parser Node Started')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received reminder: "{msg.data}"')
        # Here you can add parsing logic if needed

def main(args=None):
    rclpy.init(args=args)
    node = ReminderParser()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
