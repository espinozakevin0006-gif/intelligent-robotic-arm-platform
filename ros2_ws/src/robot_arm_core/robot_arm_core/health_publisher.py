import rclpy
from rclpy.node import Node
from robot_arm_interfaces.msg import Health


class HealthPublisher(Node):

    def __init__(self):
        super().__init__('health_publisher')
        self.publisher = self.create_publisher(Health, 'robot/health', 10)
        self.timer = self.create_timer(1.0, self.publish_health)
        self.counter = 0

    def publish_health(self):
        msg = Health()

        self.counter += 1

        if self.counter % 20 == 0:
            msg.current = 1.1
            msg.temperature = 72.0
            msg.vibration = 0.5
        elif self.counter % 12 == 0:
            msg.current = 3.4
            msg.temperature = 40.0
            msg.vibration = 0.4
        elif self.counter % 9 == 0:
            msg.current = 1.3
            msg.temperature = 36.0
            msg.vibration = 1.8
        else:
            msg.current = 1.2
            msg.temperature = 35.0
            msg.vibration = 0.3

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published → current={msg.current}, '
            f'temp={msg.temperature}, vib={msg.vibration}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = HealthPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()