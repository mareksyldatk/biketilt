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
Install homebrew 

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install protocol buffers

```
brew install protobuf
```

To install `imposm.parser` one needs `c` compiler, e.g. `xcode`. When available, activate virtuale nvironment and install parser

```
source biketiltenv/bin/activate
CC=clang // this shit according to http://stackoverflow.com/questions/32846806/compilation-error-when-using-gcc-in-osx-10-10-5
pip install imposm.parser
```

Install Google Maps Services Python

```
pip install -U googlemaps
```

## Sources
- [Open Street Map (OSM) data](http://download.geofabrik.de/europe/poland.html)
- [Open Street Map parser for Python](https://imposm.org/docs/imposm.parser/latest/)  