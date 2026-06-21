from setuptools import setup

package_name = 'ros2_learning_lab'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/demo.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuyang',
    maintainer_email='you@example.com',
    description='ROS2 learning project with topic, service, launch, and parameters.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'talker = ros2_learning_lab.talker:main',
            'listener = ros2_learning_lab.listener:main',
            'monitor = ros2_learning_lab.monitor:main',
            'client = ros2_learning_lab.client:main',
        ],
    },
)
