from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    talker_node = Node(
        package='ros2_learning_lab',
        executable='talker',
        name='talker',
        output='screen',
        parameters=[
            {'name': 'yuyang'},
            {'interval_sec': 1.0},
        ],
    )

    listener_node = Node(
        package='ros2_learning_lab',
        executable='listener',
        name='listener',
        output='screen',
    )

    monitor_node = Node(
        package='ros2_learning_lab',
        executable='monitor',
        name='monitor',
        output='screen',
    )

    return LaunchDescription([
        talker_node,
        listener_node,
        monitor_node,
    ])
