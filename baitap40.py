for x in range(101):      # trâu đứng
    for y in range(101):  # trâu nằm
        
        z = 100 - x - y   # trâu già
        
        if z >= 0 and (5*x + 3*y + z/3 == 100):
            print("Trau dung:", x, 
                  "Trau nam:", y, 
                  "Trau gia:", z)
