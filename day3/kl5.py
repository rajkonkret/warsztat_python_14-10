# zrobic słownik z metodą, która zwraca najdłuższy klucz w słowniku
class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


dictionary = LongestKeyDict()
print(dictionary.longest_key())  # None
dictionary['tomasz'] = 45
dictionary['abraham'] = 7
dictionary['zen'] = 79
print(dictionary.longest_key())
