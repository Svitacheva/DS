def data_types():
    one = 21        
    two = 'School'       
    three = 36.6   
    four = True  
    five = [1, 2, 3, 4, 5]
    six = {'num1': 10, 'num2': 20}     
    seven = (True, False)     
    eight = {1, 2, 3} 

    print([type(one).__name__,
           type(two).__name__,
           type(three).__name__,
           type(four).__name__,
           type(five).__name__,
           type(six).__name__,
           type(seven).__name__,
           type(eight).__name__])


if __name__ == '__main__':
    data_types()
    
