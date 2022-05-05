# Html_to_image_python3
in this code used HTML2Image ("HTML to Image") is Python package that acts as a wrapper around the headless mode of existing web browsers to generate images from URLs and from HTML+CSS strings or files


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gajanan0707/Htlm_to_image_python3.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd project
(vnv)$ python3 html_to_image_convert.py

Result: (https://i.imgur.com/lixrqmL.png)
```