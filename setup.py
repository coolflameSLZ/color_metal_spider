from setuptools import setup, find_packages

requirements = [
    'jupyter',
    'numpy',
    'matplotlib',
    'requests',
    'pandas',
    'scrapy',
    'protego',
    'selenium'
]

setup(
    name='color_metal_dataspider',
    version='0.0.1',
    python_requires='>=3.5',
    author='',
    author_email='',
    url='',
    description='有色金属爬虫',
    license='MIT-0',
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements,
)
