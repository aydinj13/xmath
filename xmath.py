from statistics import mean, median, mode

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

# Mean Function -> mean
def get_mean():
    
    array = get_list("Integer: ")
    return mean(array)

# Median Function -> median(s)
def get_median():
    
    array = get_list("Integer: ")
    return median(array)
    # if there are 2 medians output

# Mode Function -> mode(s)
def get_mode():
    
    array = get_list("Integer: ")
    return mode(array)
    # if there is no mode then output "N/A"
    # if there is more than 1 mode output all modes
    



print(f"Mean: {get_mean()}\nMedian: {get_median()}\nMode: {get_mode()}")
