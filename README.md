# Drupwn [v0.8]

## Description

Drupwn claims to provide an efficient way to gather drupal information.

[![asciicast](https://asciinema.org/a/42383.png)](https://asciinema.org/a/J6dQmUJVskyHV07iARITfoLan)

## Functionalities

* User enumeration
* Node enumeration
* Default files enumeration
* Module enumeration
* Theme enumeration
* Fingerprinting module
* Cookies support
* User-Agent support
* Basic authentication support
* Request delay
* Enumeration range
* Logging

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 drupwn.py --help
```

## Docker alternative

### Build

To build the container, just use this command:

```bash
docker build -t drupwn .
```

Docker will download the Debian image and then execute the installation steps.

> Be patient, the process can be quite long the first time.

### Run

Once the build process is over, get and enjoy your new Drupal scanner

```bash
docker run --rm -it drupwn --help
```

## Logging

The output generated is stored in the following file **/tmp/drupwn.txt**.
When using docker, you must prior create your logging file then link it when running your container using the following option

```bash
-v YOUR_PATH_FOLDER/YOUR_lOGGING_FILE:/tmp/drupwn.txt
```

## Enhancement

To add a new module, follow the template used in the *User.py* file.
Then, add a reference in the Parser as well as in the Dispatcher in order to ensure its support by the reflective factory.
