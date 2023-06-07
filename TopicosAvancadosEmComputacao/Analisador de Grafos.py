def printGrafo(grafo):
    print()
    for i in grafo:
        print(i)
    print()

def construirGrafo(arestas, grafo):
    for i in range(arestas):
        vo = int(input( "Informe o vertice origem: "))
        vd = int(input( "Informe o vertice destino: "))
        grafo[vo][vd] = 1
        grafo[vd][vo] = 1
    return grafo

def obtemGrau( l ):
    grau = 0
    for i in l:
        if i > 0:
            grau += 1
    return grau        

def isEuleriano( grau):
    if grau % 2 != 0:
        return False
    return True

def isCompleto(grau, nVertices):
    if(grau == (nVertices -1)):
        return True
    return False
    
def isEstrela(flagEstrela, grau, nVertice):
    if grau == 1:
        return True, flagEstrela
    if grau == (nVertice -1):
        if(flagEstrela == 0):
            flagEstrela += 1
            return True, flagEstrela
        else:
            return False, flagEstrela
    return False, flagEstrela;
    
def realizaVerificacoes(regular, euleriano, completo, estrela):
    if regular:
        print( "Grafo é regular\n" )
    else:    
        print( "Grafo não é regular\n" )
    
    if euleriano:
        print( "Grafo é euleriano\n" )
    else:
        print( "Grafo não é euleriano\n" )
    
    if completo:
        print( "Grafo é completo\n" )
    else:
        print( "Grafo não é completo\n" )
        
    if estrela:
        print( "Grafo é estrela\n" )
    else:
        print( "Grafo não é estrela\n" )

def main():
    l=[]
    m=[]
    v = int(input( "Informe o numero de vertices: ")) 
    for i in range( v ):
        l.append( 0 )
    for i in range( v ):
        m.append( l[:] )    
        
    printGrafo(m)    
        
    a = int(input( "Informe o numero de arestas: "))
    m = construirGrafo(a, m)

    printGrafo(m)

    regular = True
    euleriano = True
    completo = True
    flagEstrela = 0
    estrela = True
    g = obtemGrau(m[0])
    for i in m:
        g2 = obtemGrau(i)
        if g2 != g:
            regular = False
        euleriano = isEuleriano(g2)
        completo  = isCompleto(g2, v)
        estrela, flagEstrela = isEstrela(flagEstrela, g2, v)
    
    realizaVerificacoes(regular, euleriano, completo, estrela)
    
main()
