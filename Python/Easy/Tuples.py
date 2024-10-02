''' Para solucionar este ejercicio, es necesario cambiar el "Lenguage" a Pypy3
    ya que en python3 por lo general el sistema arroja diferente resultado con 
    hash() '''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    r = tuple(integer_list)
    print(hash(r))