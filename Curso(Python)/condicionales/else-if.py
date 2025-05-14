ingresp_mensual = 20000
gasto_mensual = 80000

#if anidados y else if(elif)

if ingresp_mensual >10000:
    if ingresp_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingresp_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("hay que ver si te alcanza")
    
elif ingresp_mensual > 1000:
    print("esta bien en latinoamerica")
else:
    print("sos pobre")