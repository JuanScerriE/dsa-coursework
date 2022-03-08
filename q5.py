class PeekStream:
    def __init__(self, stream):
        self.stream = stream
        self.len = len(stream)
        self.pos = 0

        if self.len > 0:
            self.current = stream[0]
        else:
            self.current = None

    def peek(self):
        if self.current != None:
            return self.current
        else:
            return None

    def next(self):
        if self.current != None:
            ret = self.current

            self.pos += 1

            if self.pos < self.len:
                self.current = self.stream[self.pos]
            else:
                self.current = None

            return ret
        else:
            return None


class Token:
    def __init__(self, typ, val):
        self.typ = typ
        self.val = val

    def is_opr(self):
        if self.typ == "OPR":
            return True
        else:
            return False

    def is_num(self):
        if self.typ == "NUM":
            return True
        else:
            return False

    def get_val(self):
        return self.val


class Stack:
    def __init__(self):
        self.arr = []
        self.len = 0

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.arr.pop(self.len)
        else:
            return None

    def push(self, item):
        self.arr.append(item)
        self.len += 1

    def get_len(self):
        return self.len

    def out(self):
        print("Base [", end="")

        for i in range(self.len - 1):
            print(str(self.arr[i]), end=", ")

        print(str(self.arr[self.len - 1]) + "] Top")


def get_num(peek_expr):
    val = ""

    floating = False

    while '0' <= peek_expr.peek() <= '9' or peek_expr.peek() == '.':
        if peek_expr.peek() == '.':
            if not floating:
                floating = True
            else:
                raise Exception("InvalidFloat")

        val += peek_expr.next()

    return Token("NUM", float(val))

def get_opr(peek_expr):
    return Token("OPR", peek_expr.next())


def lex(expr):
    peek_expr = PeekStream(expr)

    tok_list = []

    while peek_expr.peek() != None:
        if peek_expr.peek() == ' ':
            peek_expr.next()
        elif peek_expr.peek() in { '+', '-', '*', '/' }:
            tok_list.append(get_opr(peek_expr))
        elif '0' <= peek_expr.peek() <= '9' or peek_expr.peek() == '.':
            tok_list.append(get_num(peek_expr))
        else:
            raise Exception("InvalidExpression")
    
    return tok_list


def eval(tok_list):
    stack = Stack()

    for tok in tok_list:
        if tok.is_num():
            stack.push(tok.get_val())
        elif tok.is_opr():
            opr = tok.get_val()
            a = stack.pop()
            b = stack.pop()

            if opr == '+':
                stack.push(a + b)
            elif opr == '-':
                stack.push(b - a)
            elif opr == '*':
                stack.push(a * b)
            elif opr == '/':
                stack.push(b / a)
            else: # This can never happen.
                raise Exception("UnknownError")
        else: # This can never happen.
            raise Exception("UnknownError")

        stack.out()

    if stack.get_len() == 1:
        return stack.pop()
    else:
        raise Exception("InvalidExpression")



expr = input("Input RPN Expression: ")

print("Result: " + str(eval(lex(expr))))
