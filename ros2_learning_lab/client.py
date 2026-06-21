import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class StatsClient(Node):
    def __init__(self):
        super().__init__('stats_client')
        self.client = self.create_client(Trigger, 'chatter_stats')

    def call_service(self):
        if not self.client.wait_for_service(timeout_sec=3.0):
            self.get_logger().error('Service /chatter_stats not available.')
            return None

        request = Trigger.Request()
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = StatsClient()

    try:
        response = node.call_service()
        if response is not None:
            node.get_logger().info(f'Service response: success={response.success}, message="{response.message}"')
    finally:
        node.destroy_node()
        rclpy.shutdown()
