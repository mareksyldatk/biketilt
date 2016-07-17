# bikeTilt project
Hobby project for finding most curvy roads using Google Maps and OpenStreetMap.

## Setup
- Checkout from [**git**](https://github.com/mareksyldatk/biketilt).
- Install [**miniconda**](http://conda.pydata.org/docs/install/quick.html) package.
- Go to `biketilt` folder and create virtual environment using the `requirements.txt` file
 
	```
	conda env create -f environment.yml
	```
- To activate this environment, use `source activate biketiltenv` and to deactivate this environment, use `source deactivate`.

- Export `.yml` and `requirements.txt`

	```
	source activate biketiltenv
	conda list -e > requirements.txt
	conda env export > environment.yml
	source deactivate
	```
- Install packages in requirements

	```
	source activate biketiltenv
	conda install --file requirements.txt
	source deactivate
	```

 

More info about exporting/importing/updating virtual environments can be found [**in the conda documentation**](http://conda.pydata.org/docs/using/envs.html).

## Sources
- [Open Street Map (OSM) data](http://download.geofabrik.de/europe/poland.html)
- [Open Street Map parser for Python](https://imposm.org/docs/imposm.parser/latest/)  