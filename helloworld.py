
h = ord('H')
e = ord('e')
l = ord('l')
L = ord('l')
o = ord('o')
space = ord(' ')
w = ord('W')
o = ord('o')
r = ord('r')
l = ord('l')
d = ord('d')
ex = ord('!')

def hello(current_number = 0):
    ah = chr(h)
    ae = chr(e)
    al = chr(l)
    aL = chr(L)
    ao = chr(o)
    aspace = chr(space)
    aw = chr(w)
    ao = chr(o)
    ar = chr(r)
    al = chr(l)
    ad = chr(d)
    aex = chr(ex)

    hello = ah + ae + al + aL + ao + aspace + aw + ao + ar + al + ad + aex
    hello = list(hello)
    hello_len = len(hello)
    while current_number < hello_len:
        print(hello[current_number], end = '')
        current_number = current_number + 1
hello()

