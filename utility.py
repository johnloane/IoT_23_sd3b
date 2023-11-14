def main():
    #print(square(2.5))
    ciaran = None
    print(hello(ciaran))
    

def hello(to="World"):
    return f"Hello {to}!"

# The types seem to be a suggestion to the compiler not enforced
def square(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError('x must be an integer')
    return x * x

if __name__ == '__main__':
    main()