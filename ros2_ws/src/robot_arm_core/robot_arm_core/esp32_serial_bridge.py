import serial

import rclpy
from rclpy.node import Node
from robot_arm_interfaces.msg import Health
from std_msgs.msg import String


class ESP32SerialBridge(Node):

    def __init__(self):
        super().__init__('esp32_serial_bridge')

        self.health_publisher = self.create_publisher(
            Health,
            'robot/health',
            10
        )

        self.create_subscription(
            String,
            'robot/arm_command',
            self.command_callback,
            10
        )

        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0)

        self.timer = self.create_timer(0.1, self.read_serial)

        self.get_logger().info('ESP32 serial bridge started on /dev/ttyUSB0')

    def command_callback(self, msg):
        command = msg.data.strip()

        if not command.startswith('ANGLE:'):
            self.get_logger().warn(f'Ignored invalid command: {command}')
            return

        serial_command = command + '\n'
        self.serial_port.write(serial_command.encode('utf-8'))

        self.get_logger().info(f'Sent command to ESP32: {command}')

    def read_serial(self):
        if self.serial_port.in_waiting == 0:
            return

        line = self.serial_port.readline().decode('utf-8', errors='ignore').strip()

        if not line:
            return

        if line.startswith('ACK:'):
            self.get_logger().info(f'ESP32 acknowledged command: {line}')
            return

        if not line.startswith('HEALTH:'):
            self.get_logger().warn(f'Ignored non-health line: {line}')
            return

        try:
            payload = line.replace('HEALTH:', '')
            sensor_part, angle_part = payload.split(',ANGLE:')

            current_str, temperature_str, vibration_str = sensor_part.split(',')

            msg = Health()
            msg.current = float(current_str)
            msg.temperature = float(temperature_str)
            msg.vibration = float(vibration_str)

            commanded_angle = int(angle_part)

            self.health_publisher.publish(msg)

            self.get_logger().info(
                f'ESP32 → current={msg.current}, '
                f'temp={msg.temperature}, '
                f'vib={msg.vibration}, '
                f'angle={commanded_angle}'
            )

        except ValueError:
            self.get_logger().warn(f'Bad telemetry packet: {line}')


def main(args=None):
    rclpy.init(args=args)
    node = ESP32SerialBridge()
    rclpy.spin(node)
    node.serial_port.close()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()