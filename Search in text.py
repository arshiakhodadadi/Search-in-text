def search_substring(main_string, substring):  
 
    main_length = len(main_string)  
    sub_length = len(substring)  

  
    if sub_length > main_length:  
        return False  

   
    for i in range(main_length - sub_length + 1):  
        match_found = True  
        for j in range(sub_length):  
            if main_string[i + j] != substring[j]:   
                match_found = False  
                break   

        if match_found:  
            return True  

    return False   

def run():  
 
    main_str = input("Enter the main string: ")  
    sub_str = input("Enter the substring to search for: ")  
    
     
    result = search_substring(main_str, sub_str)  
    print("Does the substring exist in the main string?", result)  

run()  

