#create a box/node that can store data and is able to point to the next box/node
class Box():
    def __init__(self,data=None):
        self.data=data
        self.pointer=None

#Now link the boxes together and be able to store data in them (pointing to another box)
class LinkedBox():
    def __init__(self,data):
        self.box=Box(data)
    
    #FIFO
    def add_end(self,data):
        new_box = Box(data)
        self.box.pointer=new_box

    #FILO
    def add_front(self,data):
        new_box = Box(data)
        new_box.pointer=self.box
        self.box = new_box
    
    #Everything
    @property
    def lisst(self):
        while self.box.pointer is not None:
            yield self.box.data
    
def main():
    linkedlist= LinkedBox(1)
    for i in range(1,5):
        linkedlist.add_end(i+1)
    
    for i in linkedlist.lisst:
        print(i)



if __name__ == '__main__':
    main()