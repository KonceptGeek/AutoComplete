Auto Complete
============

A Trie data structure based auto complete program in Python. In standard implementation of Trie data structure, the nodes are made up of each character, but in this the nodes are made up of prefixes. I chose this so that the lookup would be faster as the user is providing the prefix for which he needs suggestions, so I directly lookup for the prefix in my list of nodes and traverse the Trie from there to find the suggestions.
