# Antivirus Logs Info Extractor

Antivirus Logs Info Extractor is a program to extract data in a given format from an antivirus log.

## Problem

##### Example String:

"SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2
cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls 
cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 
cs3Label=Tags cs3=USA,Finance cs4Label=Url 
cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 
cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule 
has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1"

##### Expected Output:

{'cat': 'C2 ', 'cs1Label': 'subcat ', 'cs1': 'DNS_TUNNELING ', 'cs2Label': 'vueUrls ', 'cs2': 'https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 ', 'cs3Label': 'Tags ', 'cs3': 'USA,Finance ', 'cs4Label': 'Url ', 'cs4': 'https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 ', 'cn1Label': 'severityScore ', 'cn1': '900 ', 'msg': 'Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. ', 'dhost': 'bad.com ', 'dst': '1.1.1.1'}


## Installation

No special installation required other than python. Requirements.txt is also not required as no other packages is required to be installed

```bash
Python 3.8.1
```

## Running Guidelines

```python
if __name__ == "__main__":
    inp_str = "SAC:0|Sacumen|CAAS|2021.2.0|3|..."
    logs_dict_instance = LogsDict(inp_str)
    print(logs_dict_instance.get_response())
```

The above is an example on how to run the module to extract the data. Replace inp_str with your string/input string and create the instance of the class.
```python
    logs_dict_instance = LogsDict(inp_str)
```

Then use the get_response method to get the final dictionary with the extracted data.

##### command to run in terminal : 
```bash
python file_name.py
```

## Details of the module

The LogsDict class is used to get the dictionary which has the extracted data from the logs/input string.

There are 5 methods used in this class:

1. validate_params : Check if the input is a valid string. Return True if valid, retrun False if invalid.
2. find_match_positions : Using regular expression, creates a list of indexes of matched patterns of the required dictionary keys from the input string.
e.g.: [(45, 49), (52, 61), (68, 72), (86, 95), (103, 107)]
1st index in a tuple = starting position of matched pattern.
2nd index in a tuple = ending position of matched pattern.
3. prepare_final_dict : creates a dictionary using string slicing where key is the matched pattern. Value of the dictionary is fetched using last index of matched pattern and first index of next matched pattern.
4. Performs all required methods to get the final dictionary.


## License
[MIT](https://choosealicense.com/licenses/mit/)