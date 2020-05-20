# Drupwn [v1.0.4]

## Description

Drupwn claims to provide an efficient way to gather drupal information.

Enumeration
[![asciicast](https://asciinema.org/a/5InNWAotigwM4bRscUi7yKAtt.svg)](https://asciinema.org/a/5InNWAotigwM4bRscUi7yKAtt)

Exploitation
[![asciicast](https://asciinema.org/a/bZmopDt4lyix1D9sgxwQMCRfn.svg)](https://asciinema.org/a/bZmopDt4lyix1D9sgxwQMCRfn)

Further explaination on our [blog post article](https://www.immunit.ch/en/blog/2018/04/10/yet-another-drupal-scanner-drupwn-2/)

## Supported tested version

* Drupal 7
* Drupal 8

## Execution mode

Drupwn can be run, using two seperate modes which are **enum** and **exploit**.
The enum mode allows performing enumerations whereas the exploit mode allows checking and exploiting CVEs.

## Functionalities

### Enum mode

* User enumeration
* Node enumeration
* Default files enumeration
* Module enumeration
* Theme enumeration
* Cookies support
* User-Agent support
* Basic authentication support
* Request delay
* Enumeration range
* Logging
* Socks and HTTP proxy support

### Exploit mode

* Vulnerability checker
* CVE exploiter

## Installation

```bash
pip3 install -r requirements.txt
python3 drupwn --help
```

or

```bash
python3 setup.py install
drupwn --help
```

## Usage

```
$ drupwn -h

        ____
       / __ \_______  ______ _      ______
      / / / / ___/ / / / __ \ | /| / / __ \
     / /_/ / /  / /_/ / /_/ / |/ |/ / / / /
    /_____/_/   \__,_/ .___/|__/|__/_/ /_/
                     /_/

usage: drupwn [-h] [--mode MODE] [--target TARGET] [--users] [--nodes] [--modules] [--dfiles] [--themes]
              [--version VERSION] [--cookies COOKIES] [--thread THREAD]
              [--range RANGE] [--ua UA] [--bauth BAUTH]
              [--delay DELAY] [--log] [--update] 
              [--proxy PROXY | --proxies PROXIES]

Drupwn aims to automate drupal information gathering.

optional arguments:
  -h, --help         show this help message and exit
  --mode MODE        enum|exploit
  --target TARGET    hostname to scan
  --users            user enumaration
  --nodes            node enumeration
  --modules          module enumeration
  --dfiles           default files enumeration
  --themes           theme enumeration
  --version VERSION  Drupal version
  --cookies COOKIES  cookies
  --thread THREAD    threads number
  --range RANGE      enumeration range
  --ua UA            User Agent
  --bauth BAUTH      Basic authentication
  --delay DELAY      request delay
  --log              file logging
  --update           update plugins and themes
  --proxy PROXY      [http|https|socks]://host:port
  --proxies PROXIES  Proxies file
```

## Docker alternative

### Official image

You can pull the official Drupwn image from the dockerhub registry using the following command:

```
docker pull immunit/drupwn
```

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

The output generated is stored in the **/tmp/** folder.
When using docker, run your container using the following option

```bash
-v YOUR_PATH_FOLDER:/tmp/
```

## Enhancement

To add a new module, follow the template used in the *User.py* file.
Then, add a reference in the Parser as well as in the Dispatcher in order to ensure its support by the reflective factory.

## Disclaimer of Warranty

Drupwn is provided under this License on an "as is" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Drupwn is free of defects, merchantable, fit for a particular purpose or non-infringing.

## Disclaimer

Running Drupwn against websites without prior mutual consent may be illegal in your country. The ImmunIT Team accept no liability and are not responsible for any misuse or damage caused by Drupwn.
