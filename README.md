# Drupwn [v0.9.0]

## Description

Drupwn claims to provide an efficient way to gather drupal information.

[![asciicast](https://asciinema.org/a/42383.png)](https://asciinema.org/a/J6dQmUJVskyHV07iARITfoLan)

Further explaination on our [blog post article](https://www.immunit.ch/en/blog/2018/04/10/yet-another-drupal-scanner-drupwn-2/)

## Supported tested version

* Drupal 7
* Drupal 8

## Functionalities

* User enumeration
* Node enumeration
* Default files enumeration
* Module enumeration
* Theme enumeration
* Vulnerability checker
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

Docker will download the Alpine image and then execute the installation steps.

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

## Disclaimer of Warranty

WPScan is provided under this License on an "as is" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the WPScan is free of defects, merchantable, fit for a particular purpose or non-infringing.

## Disclaimer

Running Drupwn against websites without prior mutual consent may be illegal in your country. The ImmunIT Team accept no liability and are not responsible for any misuse or damage caused by Drupwn.
