import statistics

#Problems in code: 
# 1. Mode (if/else) statement
# 2. In get_list function, keeps asking num input question repetitively
# 3. No Value Errors in get list function
# 4. Code can be shorter!!!!!!



def get_list(prompt):
    
                
                    
            num = int(input("How many numbers (up to 5): "))
                       
                           

            if num == 2:
                
                        a = int(input(prompt))
                        b = int(input(prompt))
                        return [a, b]
                        
    
    
                    

            elif num == 3:
                
                    
                    a = int(input(prompt))
                    b = int(input(prompt))
                    c = int(input(prompt))
                    return [a, b, c]
                                    
                
                    e

            elif num == 4:
                
                        a = int(input(prompt))
                        b = int(input(prompt))
                        c = int(input(prompt))
                        d = int(input(prompt))
                        return [a, b, c, d]
            
                
                    

            elif num == 5:
                
                        a = int(input(prompt))
                        b = int(input(prompt))
                        c = int(input(prompt))
                        d = int(input(prompt))
                        e = int(input(prompt))
                        return [a, b, c, d, e]
                
            else:
                    return "N/A"

    

def get_mean():
    
    array = get_list("Int: ")
    return statistics.mean(array)

def get_median():
    
    array = get_list("Int: ")
    return statistics.median(array)

def get_mode():
    
    array = get_list("Int: ")
    
    # if there is no mode then output "N/A" - Error (Line 26-29)
    if statistics.mode != 0:
        return statistics.mode(array)
    else:
        return "N/A"



print(f"Mean: {get_mean()}\nMedian: {get_median()}\nMode: {get_mode()}")