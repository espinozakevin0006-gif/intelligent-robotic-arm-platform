import rclpy
from rclpy.node import Node
from robot_arm_interfaces.msg import Health
from std_msgs.msg import String


class HealthMonitor(Node):

    def __init__(self):
        super().__init__('health_monitor')

        self.create_subscription(
            Health,
            'robot/health',
            self.health_callback,
            10
        )

        self.status_publisher = self.create_publisher(
            String,
            'robot/system_status',
            10
        )

    def health_callback(self, msg):

        current = round(msg.current, 2)
        temperature = round(msg.temperature, 2)
        vibration = round(msg.vibration, 2)

        if temperature > 65.0:
            status = 'FAULT: overheating'
        elif current > 2.5:
            status = 'WARNING: high current'
        elif vibration > 1.5:
            status = 'WARNING: vibration'
        else:
            status = 'NORMAL'

        status_msg = String()
        status_msg.data = status

        self.status_publisher.publish(status_msg)

        self.get_logger().info(
            f'Current={current}A, Temp={temperature}C, '
            f'Vib={vibration}g → {status}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = HealthMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()