from setuptools import setup, find_packages

setup(
    name='image_compressor',
    version='1.0.0',
    description='A command-line tool to compress JPEG images.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'compress-images=image_compressor.compressor:main',
        ],
    },
)
