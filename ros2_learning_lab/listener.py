import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__('listener')

        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10,
        )

        self.get_logger().info('Listener started and waiting for messages.')

    def listener_callback(self, msg: String):
        self.get_logger().info(f'Heard: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = Listener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
