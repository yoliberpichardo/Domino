#palindromes
#letra = "all"

#pali = letra[::-1]

#print(pali.find(letra))

#def suma(a,b):   
#    return a + b + b + a

#print(suma("a","b"))

#buscando la segunda
#def find_second(a,b):
#    result = a.find(b)
    
 #   return a.find(b,result + 1)
#a = "1 2 3 4 5 6 7 8 9 5 4"

#print(find_second(a,"4"))

#cuantos multiplos tiene cada numero

#def stamp(a):
    #cont_1 = 0
    #cont_2 = 0
    #cont_3 = 0
    #p1 = 1
    #p2 = 2
    #p5 = 5

    #while a != 0:
        #if a >= p5:
            #a -= p5
            #cont_1 += 1
        
        #elif a >= p2:
         #   a -= p2
          #  cont_2 += 1
        #elif a >= p1:
         #   a -= p1
          #  cont_3 += 1
    #return (cont_1,cont_2,cont_3)

#print(stamp(int(input("introduzca un numero: ")))) 


#contador de dias

def cont_day(day1,month1,year1,day2,month2,year2):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    total_day = 0
    while True:
        if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
            meses[1] = 29
        else: 
            meses[1] = 28
        day1 += 1
        if day1 > meses[month1-1]:
            month1 += 1
            day1 = 1
        if month1 > len(meses):
            year1 += 1
            month1 = 1
        total_day +=1
        if year1 == year2:
            if month1 == month2:
                if day1 == day2:
                    return total_day 

print(cont_day(4,8,2004,13,1,2021))
            
    

