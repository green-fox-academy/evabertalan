# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# "din" => "((("
# "recede" => "()()()"
# "Success" => ")())())"
# "(( @" => "))(("

class Encoder:
    def __init__(self, word):
        self.word=word

    def character_only_once(self):
        return list()

""join(list(map(lambda c: "()" if str.count==1)))
