from distutils.core import setup
setup(
  name = 'csv2yaml',
  packages = ['csv2yaml'],
  version = '0.2',
  description = 'CSV To JSON, YAML & Pickle Convert Tool',
  long_description='CSV To JSON, YAML & Pickle Convert Tool',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/csv2yaml',
  download_url = 'https://github.com/sepandhaghighi/csv2yaml/tarball/v0.2',
  keywords = ['csv', 'json', 'python3','python','yaml',"pickle","moduland"],
  classifiers = [],
  install_requires=[
      'pyyaml',
      'art',
      ],
  license='MIT',
)
