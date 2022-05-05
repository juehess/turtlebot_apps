from setuptools import find_packages
from setuptools import setup

package_name = 'turtlebot_calibration'

setup(
    name=package_name,
    version='2.3.7',
    packages=['turtlebot_calibration'],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    maintainer='TODO',
    maintainer_email='TODO',
    keywords=['ROS2', 'iRobot Create', 'turtlebot'],
    description=(
        """
        ROS2 calibration package for iRobot Create
        """
    ),
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           # 'turtlebot_node = src.turtlebot_calibration.calibrate:main',
           # 'turtlebot_node = src.turtlebot_calibration.scan_to_angle:main',
        ],
    },
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
    ],
)

