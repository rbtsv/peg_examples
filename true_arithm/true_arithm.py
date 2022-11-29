# This file was generated from true_arithm.peg
# See https://canopy.jcoglan.com/ for documentation

from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements):
        self.text = text
        self.offset = offset
        self.elements = elements

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.x = elements[0]
        self.term = elements[0]
        self.y = elements[1]
        self.sum = elements[1]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.op = elements[0]
        self.x = elements[1]
        self.term = elements[1]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.fact = elements[0]
        self.prod = elements[1]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.op = elements[0]
        self.x = elements[1]
        self.fact = elements[1]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.x = elements[1]
        self.expr = elements[1]


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[+,-]')
    REGEX_2 = re.compile('^[*,\\/]')
    REGEX_3 = re.compile('^[\\-]')
    REGEX_4 = re.compile('^[0-9]')

    def _read_expr(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['expr'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_term()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_sum()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'PlusNode', (cls0, self._types.PlusNode), {})
        self._cache['expr'][index0] = (address0, self._offset)
        return address0

    def _read_sum(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['sum'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0, address1 = self._offset, [], None
        while True:
            index2, elements1 = self._offset, []
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append(('TrueArithm::sum', '[+,-]'))
            if address2 is not FAILURE:
                elements1.append(address2)
                address3 = FAILURE
                address3 = self._read_term()
                if address3 is not FAILURE:
                    elements1.append(address3)
                else:
                    elements1 = None
                    self._offset = index2
            else:
                elements1 = None
                self._offset = index2
            if elements1 is None:
                address1 = FAILURE
            else:
                address1 = TreeNode2(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            if address1 is not FAILURE:
                elements0.append(address1)
            else:
                break
        if len(elements0) >= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'SumNode', (cls0, self._types.SumNode), {})
        self._cache['sum'][index0] = (address0, self._offset)
        return address0

    def _read_term(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['term'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_fact()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_prod()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode3(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'MultNode', (cls0, self._types.MultNode), {})
        self._cache['term'][index0] = (address0, self._offset)
        return address0

    def _read_prod(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['prod'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0, address1 = self._offset, [], None
        while True:
            index2, elements1 = self._offset, []
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_2.search(chunk0):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append(('TrueArithm::prod', '[*,/]'))
            if address2 is not FAILURE:
                elements1.append(address2)
                address3 = FAILURE
                address3 = self._read_fact()
                if address3 is not FAILURE:
                    elements1.append(address3)
                else:
                    elements1 = None
                    self._offset = index2
            else:
                elements1 = None
                self._offset = index2
            if elements1 is None:
                address1 = FAILURE
            else:
                address1 = TreeNode4(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            if address1 is not FAILURE:
                elements0.append(address1)
            else:
                break
        if len(elements0) >= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'ProdNode', (cls0, self._types.ProdNode), {})
        self._cache['prod'][index0] = (address0, self._offset)
        return address0

    def _read_fact(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['fact'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        index3 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append(('TrueArithm::fact', '[\\-]'))
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index3:index3], index3, [])
            self._offset = index3
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index4, elements1, address3 = self._offset, [], None
            while True:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_4.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append(('TrueArithm::fact', '[0-9]'))
                if address3 is not FAILURE:
                    elements1.append(address3)
                else:
                    break
            if len(elements1) >= 1:
                address2 = TreeNode(self._input[index4:self._offset], index4, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'NumNode', (cls0, self._types.NumNode), {})
        if address0 is FAILURE:
            self._offset = index1
            index5, elements2 = self._offset, []
            address4 = FAILURE
            chunk2, max2 = None, self._offset + 1
            if max2 <= self._input_size:
                chunk2 = self._input[self._offset:max2]
            if chunk2 == '(':
                address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address4 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append(('TrueArithm::fact', '"("'))
            if address4 is not FAILURE:
                elements2.append(address4)
                address5 = FAILURE
                address5 = self._read_expr()
                if address5 is not FAILURE:
                    elements2.append(address5)
                    address6 = FAILURE
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == ')':
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append(('TrueArithm::fact', '")"'))
                    if address6 is not FAILURE:
                        elements2.append(address6)
                    else:
                        elements2 = None
                        self._offset = index5
                else:
                    elements2 = None
                    self._offset = index5
            else:
                elements2 = None
                self._offset = index5
            if elements2 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode5(self._input[index5:self._offset], index5, elements2)
                self._offset = self._offset
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'PassNode', (cls1, self._types.PassNode), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['fact'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_expr()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append(('TrueArithm', '<EOF>'))
        raise ParseError(format_error(self._input, self._failure, self._expected))


class ParseError(SyntaxError):
    pass


def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()

def format_error(input, offset, expected):
    lines = input.split('\n')
    line_no, position = 0, 0

    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1

    line = lines[line_no - 1]
    message = 'Line ' + str(line_no) + ': expected one of:\n\n'

    for pair in expected:
        message += '    - ' + pair[1] + ' from ' + pair[0] + '\n'

    number = str(line_no)
    while len(number) < 6:
        number = ' ' + number

    message += '\n' + number + ' | ' + line + '\n'
    message += ' ' * (len(line) + 10 + offset - position)
    return message + '^'
