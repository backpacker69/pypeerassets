from setuptools import setup

setup(name='pypeerassets',
      version='0.2.6',
      description='Python implementation of the PeerAssets protocol.',
      keywords=["blockchain", "digital asset", "protocol"],
      url='https://github.com/peerassets/pypeerassets',
      author='PeerAssets',
      author_email='peerchemist@protonmail.ch',
      license='GPL',
      packages=['pypeerassets', 'pypeerassets.provider'],
      install_requires=['requests', 'protobuf', 'peercoin_rpc'],
      zip_safe=True)
