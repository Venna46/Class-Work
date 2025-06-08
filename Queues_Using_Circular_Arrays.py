
class CIRCULARARRAYQUEUE:
    """
    A QUEUE AS DISCUSSED WILL USE THE FIFO PRINCIPLE, FIRST IN FIRST OUT.

    This is a CIRCULAR QUEUE - imagine the array as a circle where after the last position, we wrap back to the first position.
    This prevents us from having to shift all elements when we remove/Dequeue items from the front.
    """

    #we start by defining the max no. of elements that our queue will hold
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        we continue to create an empty queue by initializing three important things:
        i. _data: which is basically a list filled with None values, the array...
        ii. _size: How many actual elements are at a given timestamp, we will initialize it to zero.
        iii. _front: The index/position where the 1st element is located, we initialize to zero too.
        """
        #Create a list/our array, with DEFAULT_CAPACITY slots, all filled with None.
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY

        #here we keep track of how many elements are actually in the list.
        self._size = 0

        #And here we keep track of the first car we parked at the lot
        self._front = 0

    def __len__(self):
        """
        This is an inbuilt constructor method or rather a dunder method, just like the __init__.
        It returns the size of an attribute created in the primary constructor.
        In this case, it is the elements currently in the queue. This is like counting how many cars we have in our circular parking lot.
        """
        return self._size

    def is_Empty(self):
        """
        This method will return a boolean, denoted by the double equal sign operator, which is a comparison operator.
        Thus, it will return True if the array is empty, including when it is filled none, And false if it has at least one element.
        """
        return self._size == 0

    def first(self):
        """
        This method is analogous to the PEEK() method in stacks, which will return the element at the front of the queue without removing it.
        It is like looking at the 1st car to be parked in a lot without making it leave.
        This method will raise an Empty exception if the queue is empty.
        """
        if self.is_Empty():
            raise Empty('Queue is empty') #How this exception is raised is by calling the class Exception and passing the exception type/message.

        #The front element is at position self._front in our array
        return self._data[self._front]

    def dequeue(self):
        """
        this method will remove and return the 1st element of the queue, fulfilling our FIFO principle.
        here we have another concept as in Circularly linked list, which is instead of shifting all elements left which is slow.
        we just move our _front pointer to the next position and use MODULO arithmetic to wrap around when we reach the end of the array.
        start by checking if the queue is empty

        """
        if self.is_Empty():
            raise Empty('Queue is empty')

        #Here we get the element at the front of the queue, and save it in an attribute.
        item_to_dequeue = self._data[self._front]

        #then clear the old front position to help with garbage collection, python will clean up the memory better this way
#GARBAGE COLLECTION: is a technique/process/procedure manual or autonomous, that handles memory allocation and deallocation, ensuring efficient use of memory.
                     #it is done manually in C and C++

        self._data[self._front] = None

        #Here's the magic:
        #Move the front pointer to the next position
        #The MODULO (%) operator makes it "wrap around", if we're at last position then add 1, which will go back to position 0 like a circular parking.
        self._front = (self._front + 1) % len(self._data)

        #We now have one less element in the queue, so remember to decrease the Queue size by one.
        self._size -= 1

        """
         Of course the method should return the dequeued element.
        """
        return item_to_dequeue

    def enqueue(self, element):
        """
        This is adding an element to the rear/back of our queue.
        Is like a new person joining a queue, which will be at the back of the line.

        AGAIN, HERE'S THE MAGIC: We calculate where the "back" of the queue is, using modulo arithmetic: (front + size) % capacity.
        This automatically wraps around the array needed.
        """
        #We will start with IS_FULL check, and if True, we increase the size of our queue;
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) #double the capacity

            #Calculate where to put the new element (at the back of the queue)
        back_of_the_queue = (self._front + self._size) % len(self._data)

            #Place the new element at the newly obtained back position of our queue, where enqueueing takes place.
        self._data[back_of_the_queue] = element

            #We now have one more element in the queue, thus we increase the size
        self._size += 1
#WHAT IF THE QUEUE IS FULL BUT WE STILL NEED TO ENQUEUE
    def _resize(self, new_capacity):
        """
        THIS METHOD WILL DOUBLE THE SIZE OF OUR QUEUE, ONLY WHEN THERE ARE NO EMPTY SLOTS.
        THE CURRENT SIZE OF THE QUEUE IS MULTIPLIED BY A FACTOR SPECIFIED BY THE USER, IN THIS CASE; new_capcity.

        You need to note that when we resize, we need to 'unwrap' the circular structure/array.
        And create a new linear arrangement starting from index 0 so that we can double the capacity quite easily.
        """
        #Create a new, bigger array
        old_data  = self._data #hold the existing data in our queue in the old_data attribute.
        self._data = [None] * new_capacity #Resizing by new_capacity factor

        #Then, we copy all elements from the old array/queue to the new one, starting from the front and going in the queue order.
        current_index = self._front
        for item in range(self._size):
            #Copy each element to the new array in order
            self._data[item] = old_data[current_index]
            #Move to the next element, and of course remember to wrap around if necessary
            current_index = (current_index + 1) % len(old_data)

        #Finally, we reset the front to position 0 since we've reorganized everything
        self._front = 0

    @property
    def front(self):
        return self._front

    @property
    def data(self):
        return self._data


#This is the clas we spoke of earlier, with a custom exception message for empty queue operations
class Empty(Exception):
    """
    Exception will be raised when trying to access elements from an empty queue.
    """
    def __init__(self, message="Queue is empty"):
        self.message = message
        super(). __init__(self.message)


#After preparing the ingredients and the recipe, let's now put it to use
if __name__ == '__main__':
    #Create a new queue
    queue = CIRCULARARRAYQUEUE()

    print("QUEUE USING CIRCULAR ARRAYS")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is queue empty? {queue.is_Empty()}")

    #ENQUEUE OUR QUEUE
    print("\n Enqueueing our Queue")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    #Show the front element without removing it
    print(f"\nPerson at the front of the line: {queue.first()}")

    #Remove some elements dequeue operations, then return it.
    print(f"\nServing people from the front of the queue:")
    for i in range(4):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    #To demo the circular nature, we can induce an overflow and see if it behaves correctly
    print("\nAdding more people to induce a wrap around in the array")
    more_people = ['Frank', 'Linda', 'Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    #Show what's left in the queue
    print(f"\nPerson currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    #Demo the wrap around by showing internal state
    print(f"\nInternal details:")
    print(f"Front index: {queue.front}")
    print(f"Array contents: {queue.data}")






