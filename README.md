<!-- badges: start -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10556249.svg)](https://doi.org/10.5281/zenodo.10556249)

<!-- badges: end -->

# FAIR-convergence-matrix

Basic code to create FAIR convergence matrix from nanodash nanopublications

## Prerequisites

- Basic knowledge on how to run r/python code
- Filtering data using pandas (python) or tidyverse (r)

## How to use

Change the input and output paths to your liking. The source for the new_matrix.csv in this repository is: https://github.com/peta-pico/dsw-nanopub-api/blob/main/tables/new_matrix.csv

### Python

The Python code is available in the `python ` folder.
There are two ways to run the code.

1. Run `main.py`
2. Run `create_FAIR_convergence_matrix.ipynb`

In both cases you will have to change the selection of the data manually, to fit your needs. You can do this in many ways using python and pandas. Some of the methods are described here: https://pandas.pydata.org/docs/user_guide/indexing.html

The lines to change are indicated in both files respectively.

The current implementation selects all communities with an `A` in their name.

### R

The R code is available in the `r` folder.
You can run the code in the [Quarto](https://quarto.org/) document `fcm.qmd`

You will have to change the selection of the data manually, to fit your needs. Currently this is done using the tidyverse, selecting data from all FICs that have "ENVRI" as supercommunity. More information on filtering using the information in the excellent "R for Data Science" book: https://r4ds.had.co.nz/transform.html?q=filter#filter-rows-with-filter.

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/eu-parc/FAIR-convergence-matrix/issues) to report any issues or ask for requests.
