from setuptools import setup, find_packages

setup(
    name='responses',
    version='0.01',
    license='BEENSI',
    author='beensi.com dev group',
    # author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beensi-com/responses',
    # keywords='',
    install_requires=[
        'messages @ git+https://github.com/beensi-packages/messages.git@cb3f31b7c189aed1d8fd7cb53e5266b97df81bd4',
    ],

)
