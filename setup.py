from setuptools import setup, find_packages

setup(
    name='flask-heroku-example',
    packages=find_packages(),
    version='0.1',
    description='An example practice heroku flask application.',
    author='Sara Trickett',
    author_email='strickett4@gmail.com',
    keywords=['dev3l', 'python', 'kata',],
    install_requires=[
        'pytest',
        'flask',
        'flask-runner',
        'gunicorn',
        'coverage',
        'coveralls',
        'pylint',
        'pytest',
        'flask-wtf'

    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)