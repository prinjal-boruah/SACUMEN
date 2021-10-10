import re

class LogsDict():

    def __init__(self, input_str):
        self.input_str = input_str
        #patterns to search in the input string
        self.pattern = re.compile(r'(cat=|cs1Label=|cs1=|cs2Label=|cs2=|cs3Label=|cs3=|cs4Label=|cs4=|cn1Label=|cn1=|msg=|dhost=|dst=)')

    def validate_params(self):
        '''
        Check if the input is a valid string. 
        Return True if valid, retrun False if invalid.
        ''' 
        message = False
        if isinstance(self.input_str, str) and self.input_str is not None and len(self.input_str) > 0:
            message = True
        return message

    def find_match_positions(self):
        '''
        Using regular expression, creates a list of indexes of matched 
        patterns of the required dictionary keys from the input string.
        e.g.: [(45, 49), (52, 61), (68, 72), (86, 95), (103, 107)]
        1st index in a tuple = starting position of matched pattern.
        2nd index in a tuple = ending position of matched pattern.
        '''
        matches = self.pattern.finditer(self.input_str)
        matched_positions = [ match.span() for match in matches ]
        return matched_positions

    def prepare_final_dict(self, matched_positions):
        '''
        creates a dictionary using string slicing where key is the matched pattern.
        Value of the dictionary is fetched using last index of matched pattern and 
        first index of next matched pattern.
        '''
        final_dict = dict()
        len_matched_list = len(matched_positions)
        for i in range(len_matched_list):
            if i != (len_matched_list-1):
                final_dict[self.input_str[ matched_positions[i][0] : (matched_positions[i][1] - 1) ]] = self.input_str[ matched_positions[i][1] : (matched_positions[i+1][0]) ]
            else:
                final_dict[self.input_str[ matched_positions[i][0] : (matched_positions[i][1] - 1) ]] = self.input_str[ matched_positions[i][1] : ]
        return final_dict

    def get_response(self):
        '''
        Performs all required methods to get the final dictionary.
        '''
        message = self.validate_params()
        if message == False:
            return "Invalid Log string. Please enter a valid string !"
        matched_positions = self.find_match_positions()
        final_dict = self.prepare_final_dict(matched_positions)
        return final_dict

if __name__ == "__main__":
    inp_str = "SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1"
    logs_dict_instance = LogsDict(inp_str)
    print(logs_dict_instance.get_response())