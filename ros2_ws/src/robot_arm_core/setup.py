from setuptools import find_packages, setup

package_name = 'robot_arm_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='espin',
    maintainer_email='espin@todo.todo',
    description='Robot arm core ROS 2 package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status_node = robot_arm_core.status_node:main',
            'health_publisher = robot_arm_core.health_publisher:main',
            'health_monitor = robot_arm_core.health_monitor:main',
            'recovery_supervisor = robot_arm_core.recovery_supervisor:main',
            'esp32_serial_bridge = robot_arm_core.esp32_serial_bridge:main',
        ],
    },
)
