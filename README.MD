[![GitHub license](https://img.shields.io/github/license/TrisNol/python-sample-package.svg)](https://github.com/TrisNol/python-sample-package/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/TrisNol/python-sample-package/total.svg)](https://github.com/users/TrisNol/packages/container/package/python-sample-package)
[![GitHub forks](https://img.shields.io/github/forks/TrisNol/python-sample-package.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/TrisNol/python-sample-package)
# Python saple release
This repo contains a skeleton for Python packages containing some basic DevOps´ components like CI/CD pipelines.

## Linting
The code of this repo will be linted with [PyLint](https://pylint.org/) automatically on each push and pull-request to ensure that the files are correctly formatted in order to improve readability.

## Tests
You can add your tests in the test/ directory. By providing the prefix test_ the files will be recognized and executed by PyTest.

## Documentation
The documentation is created with the help of [Sphinx](https://www.sphinx-doc.org/en/master/), which generates a html-based docu that is exposed via GitHub pages. In order to see the documentation, some configuration in GitHub needs to be done. Head to the repo´s settings and enable GitHub pages. Set the source to branch `gh-pages`. The documentation should now be hosted at `http[s]:<username>.github.io/<repo-name>`

In order to adapt the config, change the specifics in ```./docs/conf.py```.
To manually build the documentation execute the following command - and install sphinx if you haven´t already - ```sphinx-build ./docs ./docs/_build```.
However, the documentation will be built automatically on each push and added to the repo by a GitHub Action - so you don´t have to generate it yourself each time.