from distutils.core import setup
from pkg_resources import parse_requirements

setup(
    name='french-political-speeches-to-json',
    packages=['french-political-speeches-to-json'],
    version='0.1',
    license='MIT',
    description='french-political-speeches-to-jsont',
    author='Antoine',  # Type in your name
    author_email='',  # Type in your E-Mail
    url='https://github.com/gyab/french-political-speeches-to-json',
    install_requires=[str(requirement) for requirement in
                      parse_requirements(open("requirements.txt"))],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': ['french-political-speeches-to-json=crawling.crawling.spiders.speeches'],
    }
)
