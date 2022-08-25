def main():
    # Escribe tu código abajo de esta línea
    Ana  = input("Elige una opción. 'a' para piedra, 'p' para papel, 't' para tijeras")
    Juan = input("Elige una opción. 'a' para piedra, 'p' para papel, 't' para tijeras")
    
    if Juan == Ana:
        print('Empate')
        
    elif Ana == 'a' and Juan == 't':
        print('Ana gana')
    
    elif Ana == 'p' and Juan == 'a':
        print('Ana gana')
    
    elif Ana == 't' and Juan == 'p':
        print('Ana gana')
        
    elif Ana == 't' and Juan == 'a':
        print('Juan gana')
        
    elif Ana == 'a' and Juan == 'p':
        print('Juan gana')
        
    elif Ana == 'p' and Juan == 't':
        print('Juan gana')

if __name__ == '__main__':
    main()
