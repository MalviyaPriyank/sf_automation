
import re

class ValidateString:
    def __init__(self):
        pass

    def starts_with_alphabet(self,value):
        if value[0].isalpha():
            return True
        else:
            return False
        
    def has_space(self,value):
        if ' ' in value:
            return True
        else:
            return False
        
    def has_special_characters(self,value):
        if re.search(r'[^a-zA-Z0-9]',value):
            return True
        else:
            return False
    
    def is_enclosed_in_double_quotes(self,value):
        if value[0] == '"' and value[-1] == '"':
            return True
        else:
            return False

