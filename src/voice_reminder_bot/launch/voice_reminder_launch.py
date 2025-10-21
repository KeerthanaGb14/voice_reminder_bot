from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='voice_reminder_bot',
            executable='speech_listener_node',
            name='speech_listener_node'
        ),
        Node(
            package='voice_reminder_bot',
            executable='reminder_parser_node',
            name='reminder_parser_node'
        ),
        Node(
            package='voice_reminder_bot',
            executable='scheduler_node',
            name='scheduler_node'
        ),
        Node(
            package='voice_reminder_bot',
            executable='notifier_node',
            name='notifier_node'
        ),
    ])
