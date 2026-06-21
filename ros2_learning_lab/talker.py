import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        self.declare_parameter('name', 'yuyang')
        self.declare_parameter('interval_sec', 1.0)

        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.counter = 0

        interval = float(self.get_parameter('interval_sec').value)
        self.timer = self.create_timer(interval, self.timer_callback)

        self.get_logger().info(f'Talker started with interval={interval}s')

    def timer_callback(self):
        name = self.get_parameter('name').value

        msg = String()
        msg.data = f'[{self.counter}] 你好，{name}，这是 ROS2 talker。'

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publish: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = Talker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
