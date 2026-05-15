import rclpy
from rclpy.node import Node


class StatusNode(Node):
    def __init__(self):
        super().__init__('status_node')
        self.timer = self.create_timer(1.0, self.print_status)
        self.get_logger().info('Robot arm status node started.')

    def print_status(self):
        self.get_logger().info('robot_arm_core is alive')


def main(args=None):
    rclpy.init(args=args)
    node = StatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
