
class Stack(): 
    def __init__(self,stack_cap): initialises the stack empty 
        self.data_stack=[]
        self.cap=(stack_cap) #Remove line to get rid of stack limit

    def add(self,new_entry): #This function adds a new variable to the top of the stack
        if len(self.data_stack) < self.cap: #Remove logic to get rif of stack limit
            self.data_stack.append(new_entry)
            print('new entry to stack') #Confirms to the user that a new item was added to the stack
        else:
            print('Stack is full') #Notify the user stack is full
        

    def pick(self): #Pick from the top of the stack
        picked=self.data_stack.pop(-1)
        return picked

    def empty(self): #empty stack
        for i in range(len(self.data_stack)):
            self.data_stack.pop(0)
            
        print('Stack is empty')

    def show(self): #Show the list of items in the stack
        print(self.data_stack)

if __name__=='__main__':
    

