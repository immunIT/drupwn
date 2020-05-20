# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.0.4] [2020-05-12]

### Added

* Added --update option to fetch the list of new modules and themes from git.drupalcode.org
* Custom modules detection

## [1.0.3] [2019-02-28]

### Added

* Support CVE-2019-6340

### Changed

* Requests wrapper to handle data and headers overwriting
* Delete legacy CVE checker

## [1.0.2] [2019-01-22]

### Changed

* README file update
* Fixing name resolution and catching stack trace when fail

## [1.0.1] [2018-11-21]

### Changed

* Fix prompt_toolkit package
* Adding new module path, used by new Drupal version
* Set 20 default threads for efficiency


## [1.0.0] [2018-08-31]

### Added

* SOCKS and HTTP proxy support

### Changed

* Misspelling

## [0.9.2] [2018-06-28]

### Hotfix

* A minimum version has been set for the prompt_toolkit library. Indeed, the last version seems to be bugged

## [0.9.2] [2018-04-16]

### Added

* Exploit mode allowing to assess for CVEs
* Adding xmlrpc.php in default files enumeration plugin
* Adding the support of the CVE-2018-7602
* Setup.py added

### Changes

* Deleting the vulnerability checker plugin. Now, CVEs can be checked using the exploit mode
* Adding colors within the logger engine
* Improving the version fingerprinting engine
* Executable bit added to drupwn.py
* /usr/bin/env added to drupwn.py

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
