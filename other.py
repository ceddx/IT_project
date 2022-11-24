from InquirerPy import *

import unittest
class Test(unittest.TestCase):
    def test_article_generation(self):
        questions = [{
                'type': 'confirm',
                'name': 'cancel',
                'message': 'Do you want to cancel the operation?',
                'default': False
            },
            {
                'type': 'input',
                'name': 'playername',
                'message': 'Enter your player_name',
                'when': lambda answers: not answers['cancel']
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter your password',
                'when': lambda answers: not answers['cancel']
            }
            ]
        answer=prompt(questions)
        answer['playername']



if __name__ == "__main__":
    unittest.main()
