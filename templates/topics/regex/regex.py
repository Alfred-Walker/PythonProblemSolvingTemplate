"""re module usage examples with single line summary

Python re module documentation:
   https://docs.python.org/3/library/re.html
"""

import re


class RegexExample:
    @staticmethod
    def re_findall():
        """findall() finds compiled regular expression from the text in args"""
        text = "__example__text__Example"
        regex = re.compile("example", re.IGNORECASE)
        result = regex.findall(text)

        # all match results will be printed
        print(result)
        # >>> ['example', 'Example']

    @staticmethod
    def re_search():
        """search() scan through string looking for the first location where the regex pattern produces a match."""
        text = "__example__text__example"
        regex = re.compile(r"example")
        match_object = regex.search(text)

        # return type is Match object
        print(type(match_object))
        # >>> <class 're.Match'>

        # print subgroups of the 'match object'
        print(match_object.group())
        # >>> example

    @staticmethod
    def decimal_pattern():
        """digit can be parsed via regex \\d."""
        text = "Phone number: 032-232-3245"
        regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        match_object = regex.search(text)
        print(match_object.group())
        # >>> 032-232-3245

    @staticmethod
    def start_char_pattern():
        """^ is used to find texts begins with specific string"""
        text = "start_with"
        regex = re.compile(r"^art")
        result = regex.findall(text)
        print(result)
        # >>> [] (not found)

        regex = re.compile(r"^start")
        result = regex.findall(text)
        print(result)
        # >>> ['start']

    @staticmethod
    def end_char_pattern():
        """$ is used to find texts ends with specific string"""
        text = "end_with"
        regex = re.compile(r"wit$")
        result = regex.findall(text)
        print(result)
        # >>> [] (not found)

        regex = re.compile(r"with$")
        result = regex.findall(text)
        print(result)
        # >>> ['with']

    @staticmethod
    def greedy_qualifier_pattern():
        """.* is used to find entire match string"""
        text = "start_end"
        regex = re.compile(r"art.*")
        result = regex.findall(text)
        print(result)
        # >>> ['art_end']

    @staticmethod
    def decimal_range_pattern():
        """split pattern can be with range decimal condition"""
        text = "ab12ab3456"
        pattern = r'ab[1-3]'  # split by ab1, ab3
        result = re.split(pattern, text)
        print(result)
        # >>> ['', '2', '456']

    @staticmethod
    def range_and_count_pattern():
        """[] for range, {} for count. be aware of parentheses """
        text = "010-12312-1111"

        target = r"(\d{3})-(\d{3,5}-\d{4})"  # [('010', '12312-1111')]
        # target = r"(\d{3})-([1-3]{3,5}-\d{4})"  # [('010', '12312-1111')]
        # target = r"(\d{3})-[1-3]{3,5}-\d{4}"  # ['010'] (parentheses is applied d{3} only)
        # target = r"\d{3}-[1-3]{3,5}-\d{4}"  # ['010-12312-1111'] (no parentheses)

        regex = re.compile(target)
        result = regex.findall(text)
        print(result)
        # >>> [('010', '12312-1111')]

    @staticmethod
    def split():
        """split() is used to split string by pattern"""
        text = "___split1||||split2____split3||||"
        pattern = r'split[1-3]'
        result = re.split(pattern, text)
        print(result)
        # >>> ['___', '||||', '____', '||||']

    @staticmethod
    def text_with_ranged_decimal_pattern():
        """split pattern can be the text with range decimal condition"""
        text = "ab12ab3456"
        pattern = r'ab[1-3]'  # split by ab1, ab3
        result = re.split(pattern, text)
        print(result)
        # >>> ['', '2', '456']


RegexExample.re_findall()
RegexExample.re_search()
RegexExample.decimal_pattern()
RegexExample.start_char_pattern()
RegexExample.end_char_pattern()
RegexExample.greedy_qualifier_pattern()
RegexExample.decimal_range_pattern()
RegexExample.range_and_count_pattern()
RegexExample.split()
RegexExample.text_with_ranged_decimal_pattern()
