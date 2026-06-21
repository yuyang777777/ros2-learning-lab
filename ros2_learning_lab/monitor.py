import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger


class Monitor(Node):
    def __init__(self):
        super().__init__('monitor')

        self.message_count = 0

        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.on_message,
            10,
        )

        self.service = self.create_service(
            Trigger,
            'chatter_stats',
            self.handle_stats,
        )

        self.get_logger().info('Monitor started: topic /chatter, service /chatter_stats')

    def on_message(self, msg: String):
        self.message_count += 1
        self.get_logger().info(f'Received #{self.message_count}: "{msg.data}"')

    def handle_stats(self, request, response):
        response.success = True
        response.message = f'当前已接收 {self.message_count} 条 chatter 消息'
        self.get_logger().info(f'Service called -> {response.message}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = Monitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
