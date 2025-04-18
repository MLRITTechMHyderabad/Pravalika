def Calculator(a,b,operator):
    try:
        if type(a)not in [int,float] or type(b) not in [int,float]:
            raise TypeError("invalid input type")
        if operator == '+':
            return a+b
        
        elif operator == '-':
            return a-b
        
        elif operator == '*':
            return a*b
        
        elif operator == '/':
            if b==0:
                raise ZeroDivisionError("Division by zero")
            return a/b
        
        elif operator == '%':
            if b==0:
                raise ZeroDivisionError("Division by zero")
            return a%b
        
        elif operator == '**':
            return a**b
        else:
            raise ValueError("unsupported operator")
    except ZeroDivisionError:
        return "Error:Division by zero"
    except TypeError:
        return "Error:Invalid input type"
    except ValueError:
        return "Error:unsupported operator"
    except Exception as e:
        return f"Error:{str(e)}"

print(Calculator(10,0,"/"))
print(Calculator(10,"five","+"))
print(Calculator(10,5,"$"))



    
        
            

        
        
        
    
