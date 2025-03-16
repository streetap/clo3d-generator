from setuptools import setup, find_packages

setup(
    name="clo3d-generator",
    version="0.1.0",
    packages=find_packages(where="."),
    include_package_data=True,
    install_requires=[
        'click',
        'google-cloud-storage',
        'requests',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'clo3d-generator=clo3d_generator.cli:main',
        ],
    },
)
