# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [0.9.0] [2018-04-12]

### Added

* Vulnerability checker plugin
* CVE-2018-7600 support

### Functional changes

* Fingerprinting module has been moved to the core engine and run each time Drupwn is launch without the flag **--version**
* The docker image base switched from debian to alpine for sizing concern
