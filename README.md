Average per capita nominal cash income of the population

## Data

Data is in CSV format and synced with upstream source annually. It is sourced from https://taldau.stat.gov.kz/ru/Api/GetIndexData/704447?period=7&dics=67.

Official website: https://taldau.stat.gov.kz/ru/NewIndex/GetIndex/704447?regionId=741880&periodId=7#

* `data/output.csv` - data by region, year and value.

We have also added some metadata such as column descriptions and [data packaged it][dp].

[dp]: https://frictionlessdata.io/data-package/


## Preparation

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![.github/workflows/actions.yml](https://github.com/open-data-kazakhstan/average-per-capita-nominal-cash-income/actions/workflows/actions.yml/badge.svg?branch=main)

You first need to install the dependencies:

```
pip install -r requirements.txt
```

Then run the script

```
python scripts/process.py
```


