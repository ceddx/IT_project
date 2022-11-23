from pprint import pprint
import regex
from PyInquirer import  prompt
from prompt_toolkit.validation import ValidationError, Validator

class PasswordValidator(Validator):
    '''
    Classe permettant de vérifier qu'un mot de passse est valide.
    '''
    def validate(self, document):
        ok = regex.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$", document.text)
        if not ok:
            return 'Please enter a valid password'
        else:
            return ok