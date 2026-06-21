# ros2_learning_lab

一个用于 ROS2 入门练习的学习仓库，覆盖 Topic、Service、Launch 和 Parameter。

## 功能
- `talker`: 发布 chatter 消息
- `listener`: 订阅 chatter 消息
- `monitor`: 统计接收到的消息数量，并提供 `/chatter_stats` 服务
- `client`: 调用 `/chatter_stats` 服务获取统计信息

## 技术点
- rclpy
- std_msgs
- std_srvs
- Launch
- Parameters

## 运行环境
建议使用已安装 ROS2 的 Linux 环境，例如 Ubuntu + ROS2 Humble / Jazzy。

## 编译
```bash
colcon build --packages-select ros2_learning_lab
source install/setup.bash
