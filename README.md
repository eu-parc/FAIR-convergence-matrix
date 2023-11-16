# FAIR-convergence-matrix
Basic code to create FAIR convergence matrix from nanodash nanopublications

## Prerequisites

- Basic knowledge on how to run python code
- Selecting data using pandas

## How to use

Change the input and output paths to your liking. The source for the new_matrix.csv in this repository is: https://github.com/peta-pico/dsw-nanopub-api/blob/main/tables/new_matrix.csv

There are two ways to run the code.

1. Run `main.py`
2. Run `create_FAIR_convergence_matrix.ipynb`

In both cases you will have to change the selection of the data manually, to fit your needs. You can do this in many ways using python and pandas. Some of the methods are described here: https://pandas.pydata.org/docs/user_guide/indexing.html

The lines to change are indicated in both files respectively. 

The current implementation selects all communities with an `A` in their name.

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/eu-parc/FAIR-convergence-matrix/issues) to report any issues or ask for requests.
