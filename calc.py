#  -*- coding: utf-8 -*-

import sys

s = "我是大海的石头"
print s

ARG_TYPE_OPERATOR   = 1
ARG_TYPE_OPERAND    = 2

OPERATION_LIST = \
    {
        "+": lambda opr1, opr2: opr1 + opr2,
        "-": lambda opr1, opr2: opr1 - opr2,
        "*": lambda opr1, opr2: opr1 * opr2,
        "/": lambda opr1, opr2: opr1 / opr2
    }


def stringToNum(str):
    ret = dict()
    ret['state'] = False
    try:
        ret['num'] = int(str)
        # print "i'm a integer!", ret['num']
        ret['state'] = True
    except:
        # print str, "is not an integer, keep trying..."
        try:
            ret['num'] = float(str)
            # print "i'm a float!"
            ret['state'] = True
        except:
            print str, ": well, none int nor float, bye..."
    finally:
        return ret

# print stringToNum('09.9909')



def processArg(arg):
    ret = {}
    if arg in OPERATION_LIST.keys():
        ret['ARG_TYPE'] = ARG_TYPE_OPERATOR
        ret['ARG'] = arg
        return ret
    elif stringToNum(arg)['state']:
        # print "hi, i'm a operand!"
        ret['ARG_TYPE'] = ARG_TYPE_OPERAND
        ret['ARG'] = stringToNum(arg)['num']
        return ret
    else:
        print "Error! Invalid argument: ", arg
        raise TypeError

# print processArg('*')



class ArgChecker:
    ''' check in coming args '''

    def check(self):
        pass



class StackMng:
    ''' stack manager '''

    def __init__(self, lst):
        ''' using list as stack  '''

        if isinstance(lst, list):
            self.stack = lst
        else:
            print 'Error! not of type "list"'
            raise Exception


    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def operate(self, prcedArg):
        if prcedArg['ARG_TYPE'] == ARG_TYPE_OPERAND:
            self.push(prcedArg['ARG'])
        elif prcedArg['ARG_TYPE'] == ARG_TYPE_OPERATOR:
            # order
            opt2 = self.pop()
            opt1 = self.pop()
            res = OPERATION_LIST[prcedArg['ARG']](opt1, opt2)
            # print res
            self.push(res)





class Calc:

    # def main(self):
    ''' main '''





if __name__ == '__main__':
    # init stack
    stkMng = StackMng([])
    splittedArgs = sys.argv[1].split(" ")
    print splittedArgs
    # print type(sys.argv)
    for arg in splittedArgs:
        if arg == " " or arg == '':
            continue

        print arg
        stkMng.operate(processArg(arg))
        print stkMng.stack

    print "\n\nResult is:", stkMng.pop()







# a.a = 1
# a["b"] = funcL
# print OPERATION_LIST["+"](9, 1000)
# lista = [ 'a', 'b', 'c']
# print type(lista)
# enumA = enumerate(lista)
# print enumA, type(enumA)
