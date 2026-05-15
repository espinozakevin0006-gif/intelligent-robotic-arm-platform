import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RecoverySupervisor(Node):

    def __init__(self):
        super().__init__('recovery_supervisor')

        self.create_subscription(
            String,
            'robot/system_status',
            self.status_callback,
            10
        )

        self.action_publisher = self.create_publisher(
            String,
            'robot/recovery_action',
            10
        )
    
    def status_callback(self,msg):
        status = msg.data

        if status.startswith('FAULT'):
            action = 'STOP_AND_ENTER_SAFE_MODE'
        elif status.startswith('WARNING'):
            action = 'SLOW_DOWN_AND_MONITOR'
        else:
            action = 'CONTINUE_OPERATION'

        action_msg = String()
        action_msg.data = action
        self.action_publisher.publish(action_msg)

        self.get_logger().info(
            f'Status received: {status} → Recovery action: {action}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = RecoverySupervisor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
