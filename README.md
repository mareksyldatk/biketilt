# bikeTilt project
Hobby project for finding most curvy roads using Google Maps and OpenStreetMap.

## Virtualenv setup

Virtual environment was created

```
cd Documents/git/biketilt/
virtualenv biketiltenv
```

To activate virtual environment, type `source biketiltenv/bin/activate` and to deactivate type `deactivate`.


## Installation
To install `imposm.parser`
- get [easy_install]( http://askubuntu.com/questions/27519/can-i-use-easy-install )
- install [this](http://stackoverflow.com/questions/26053982/error-setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-wit)
- and [this](https://imposm.org/docs/imposm.parser/latest/install.html)

Install Google Maps Services Python

```
pip install -U googlemaps
```

## Sources
- [Open Street Map (OSM) data](http://download.geofabrik.de/europe/poland.html)
- [Open Street Map parser for Python](https://imposm.org/docs/imposm.parser/latest/)  