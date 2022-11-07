# SLA assessment and Reputation computation in EFN

This is a software prototype that assesses the SLA response time and compute the cumulated reputation to evaluate the trustworthiness of fog service

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Usage

```python
import csv
from itertools import zip_longest
import pandas as pd

# m and n are the SLA assessment threshhold
m = 100
n = 95
above_counter = 0
within_counter = 0
below_counter = 0

# Default reputation value of a service
INITIAL_REPUTATION = 3

MIN_REPUTATION = 1
MAX_REPUTATION = 5

# The number of times required for a service to reach MAX or MIN reputation
POINT_ELIGIBILITY = 4
ABOVE = "above"
WITHIN = "within"
BELOW = "below"

# List of final results
list_of_average = []
list_of_percentage = []
list_of_reputation = []
```

There are two Python files helper.py and index.py to run the software.
The helper.py contains helper functions that help to format the data and output them into a folder called temp

The index.py will be using inside the temp folder to process and calculate the SLA assessment, as well as the reputation value

The order to run the software is:

- First, run the helper.py to format the data and we can change the file path inside the function called format_input_csv_file()
- Second, run the index.py to get the result

As we run the index.py by clicking the play button, it should return 3 files inside the output folder.