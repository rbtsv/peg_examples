#!/usr/bin/env python3
import arithm_act


class Actions:   
    def pass_1(self, input, start, end, elements):        
        return elements[1]
        
    def sum(self, input, start, end, elements):
        return elements[0]+ elements[2]

    def prod(self, input, start, end, elements):
        return elements[0]* elements[2]

    def make_number(self, input, start, end, elements):
        return int(input[start:end], 10)


res = arithm_act.parse("(1+(1+2*5)*2+3)*2+13".replace(" ", ""), 
                        actions=Actions())
print(res)
