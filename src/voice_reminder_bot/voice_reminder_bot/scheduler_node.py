import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Scheduler(Node):
    def __init__(self):
        super().__init__('scheduler_node')
        self.subscription = self.create_subscription(
            String,
            'voice_reminders',
            self.schedule_reminder,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Scheduler Node Started')

    def schedule_reminder(self, msg):
        # Here you can add scheduling logic, e.g., time-based notifications
        self.get_logger().info(f'Scheduled reminder: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Scheduler()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
