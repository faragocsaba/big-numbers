def G(n):
    if n == 0:
        return 4
    return up_arrow(3, 3, G(n-1))

# a ↑^n b = a → b → n
def up_arrow(a, b, n):
    if b == 0:
        return 1
    if n == 1:
        return a**b
    return up_arrow(a, up_arrow(a, b-1, n), n-1)

print(G(64))
