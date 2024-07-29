import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-easymde',
    version='1.0.1',
    description='django-easymde is a WYSIWYG markdown editor for Django',
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Benjamin Antupit",
    author_email='b@antupit.com',
    url='https://github.com/WPI-LNL/django-easymde',
    license='MIT',
    packages=['easymde'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,admin,wysiwyg,markdown,editor,easymde',
)
