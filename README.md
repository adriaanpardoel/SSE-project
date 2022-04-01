# Static Estimation of Energy Cost for scikit-learn Models
_authors: Adriaan Pardoel, Dyon van der Ende, Sam Heslenfeld_

This code repository is part of the paper [Static Estimation of Energy Cost for 
scikit-learn Models](https://www.overleaf.com/read/qmjhdybsrfzr) and contains
all the scripts to reproduce the results.
It is required to use Windows in order for everything to work.
Also make sure to have[Intel Power Gadget](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html)
installed.

## Reproducing the results

1. Make sure your computer is not running any non-essential background tasks and
run [script.cmd](/measurements/script.cmd) in the `measurements` folder.
This will automatically run [train_network.py](/measurements/train_network.py) with
different configurations and store power logs in the default location set in the Power 
Gadget settings. 
A second `results.csv` file will be created with the results from the experiments.

2. Collect the data with [read_data.py](/analysis/read_data.py) to create a single
file that can be used for training a model.
For reproduction of the results in the paper, use the data from the `Results` folder.

3. Train the model with [regression.py](/analysis/regression.py). 
For reproduction of the results in the paper, use [out.csv](/analysis/out.csv).