#!/usr/bin/python3

# sample code to show version
#import sys
#print(sys.version_info)

import bin_digit
import bin_digits_nodes
import bin_digits_nodes_classes

bin_str = "1011"
tree = bin_digit.parse(bin_str, types=bin_digits_nodes)
tree.compute()
print(bin_str, tree.val, tree.ord)
