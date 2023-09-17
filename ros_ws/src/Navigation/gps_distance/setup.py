from setuptools import find_packages, setup

package_name = 'gps_distance'

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
    maintainer='Filip',
    maintainer_email='filipp@my.yorku.ca',
    description='Solution to 23/24 software onboarding',
    license='Copyright York University Robotics Society',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'completeSoftwareOnboarding = gps_distance.CompleteSoftwareOnboarding:main'
        ],
    },
)
