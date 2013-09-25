def dftuv(M,N):
    """
    Funcion para realizar meshgrids de frecuencias(Gonzalez, Goods, pag:128)
    Parametros:
    ------------------------------------------------------------------------
    M : entero
        Dimension en U
        
    N : entero
        Dimension en V
    
    Salida
    ------------------------------------------------------------------------
    meshgrid ---> U, V 
    

    
    """
    u = np.arange(0,M)
    v = np.arange(0,N)
    
    idx = np.where(u > M/2)
    u[idx] = u[idx] - M
    idy = np.where(v > N/2)
    v[idy] = v[idy] - N
    
    V, U = np.meshgrid(v,u)
    
    return V,U
    
        
