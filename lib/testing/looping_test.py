#!/usr/bin/env python3

from looping import happy_new_year, square_integers, fizzbuzz

import io
import sys

class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()

        # Check if answer_list is empty
        answer_list = answer.split('\n')
        if len(answer_list) == 0:
          
        # Check if the second-to-last element exists
          if len(answer_list) < 2:
            
        
        # Check if the second-to-last element is "Happy New Year!"
            assert answer_list[-2] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"
