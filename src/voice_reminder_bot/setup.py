from setuptools import find_packages, setup

package_name = 'voice_reminder_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/voice_reminder_launch.py']),  # <--- add this line
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='keerthana',
    maintainer_email='keerthana@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'speech_listener_node = voice_reminder_bot.speech_listener_node:main',
            'reminder_parser_node = voice_reminder_bot.reminder_parser_node:main',
            'scheduler_node = voice_reminder_bot.scheduler_node:main',
            'notifier_node = voice_reminder_bot.notifier_node:main',
        ],
    },
)

