from setuptools import setup

setup(name='testpipeline',
      description='simple gaia python pipeline example',
      packages=['pipeline'],
      author='pipelineauthor',
      author_email='pipelineauthor@mail.com',
      install_requires=[
            'gaiasdk>=0.0.16',
            'bandit==1.7.4',
            'safety==2.2.0',
            'pyraider==1.0.20',
            'GitPython==3.1.27'
      ])
