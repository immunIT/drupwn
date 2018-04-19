# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [0.9.2] [2018-04-16]

### Added

* Exploit mode allowing to assess for CVEs

### Changes

* Deleting the vulnerability checker plugin. Now, CVEs can be checked using the exploit mode
* Adding colors within the logger engine
* Improving the version fingerprinting engine

## [0.9.1] [2018-04-13]

### Bug fix

* Adding **/** at the end of the **/sites/default/modules** resource

## [0.9.0] [2018-04-12]

### Added

* Vulnerability checker plugin
* CVE-2018-7600 support

### Functional changes

* Fingerprinting module has been moved to the core engine and run each time Drupwn is launch without the flag **--version**
* The docker image base switched from debian to alpine for sizing concern
