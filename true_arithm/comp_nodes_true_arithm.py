#!/usr/bin/env python3
import true_arithm
import true_arithm_nodes


tree = true_arithm.parse("-3*((32/4+3*9)+1+3+25*13*17/-13/25)/2/7".replace(" ", ""),
                         types=true_arithm_nodes)
                         
print(tree.compute())
