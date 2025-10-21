import rclpy
from rclpy.node import Node

class NotifierNode(Node):
    def __init__(self):
        super().__init__('notifier_node')
        self.get_logger().info('Notifier Node Started')
        # For now, no notifications implemented

def main(args=None):
    rclpy.init(args=args)
    node = NotifierNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
