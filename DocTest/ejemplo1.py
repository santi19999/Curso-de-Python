def compruebaMail(mailUsuario):
    """la funcion compruebaMail evalúa un mail recibido
    en busca de la @. Si tiene una @ es correcto, 
    si tiene mas de una @ es incorrecto
    si la @ esta al final es incorrecto
    
    >>> compruebaMail('Juan@Cursos.es')
    True
    >>> compruebaMail('Juan@Cu@rsos.es')
    False
    >>> compruebaMail('Juan@Cursos.es@')
    False
    >>> compruebaMail('JuanCursos.es')
    False



    
    """
    
    arroba=mailUsuario.count('@')
    
    if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True
    
    
    
    
import  doctest
doctest.testmod()