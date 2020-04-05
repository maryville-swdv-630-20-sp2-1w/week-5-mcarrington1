"""
This is an example of a Singleton pattern.
This class is used to look up previous order history, which relies on a database with limited connections.
"""
class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DbConnection(metaclass=Singleton):
    def __init__(self):
        dbConnectionString = 'dbhost.example.com/orclpdb1'
        
    def __str__(self):
        return ('Db connection string is: {}'.format(self.dbConnectionString))
    
    def lookUpHistory(self, orderId):
        """
        Place the DB call which will map back to orderHistory
        @returns - orderHistory tuple where first element is orderId, 2nd is date, 3rd is what was ordered
        """
        # Stub - This is where we would place the actual call to the DB here
        orderHistory = ('5Dc2X6AOTd5EGWNK', '8/14/2020', ['item1','item2','item3'])
        return orderHistory
        

class OrderHistory:
    def __init__(self, orderId):
        self.orderId = orderId
        self.orderHistory = DbConnection.lookUpHistory(self, orderId)
        
    def __str__(self): 
        return ('Order Info is: {}'.format(self.orderHistory))
    
if __name__== '__main__':
    orderHistory = OrderHistory('5Dc2X6AOTd5EGWNK')
    print(orderHistory)