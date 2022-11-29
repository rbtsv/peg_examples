#!/usr/bin/env python3
import arithm
import arithm_nodes


expr = "((1+(10+3)) *5 )".replace(" ", "")
print(expr)

tree = arithm.parse(expr, types=arithm_nodes) # ((10+3)*5)
print(tree.compute())
