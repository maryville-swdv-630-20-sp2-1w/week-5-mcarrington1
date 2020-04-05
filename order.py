"""
This is an example of an abstract factory pattern.
The purpose of this class is to create order objects that are submitted via the web client.
"""
import random, string
from datetime import datetime
from abc import ABC, abstractmethod

class OrderFactory(object):
    """
    This is a factory class to create different order types.
    """    
    def createCarryOutOrder(self, *args, **kwargs):
        return CarryOutOrder(*args, **kwargs)
    def createDeliveryOrder(self, *args, **kwargs):
        return DeliveryOrder(*args, **kwargs)
    def createVolumeOrder(self, *args, **kwargs):
        return VolumeOrder(*args, **kwargs)
    
class Order(ABC):
    """
    This is the abstract Order class that will extend to different orders.
    @params account - account object
    @params orderManifest - list of menuItems that are being ordered
    """
    def __init__(self, account, orderManifest):
        self.account = account
        self.orderManifest = orderManifest
        self.status = "PENDING"
        self.orderId = generateRandomOrderId()
        self.orderPlaced = generateTimeStamp()
        self.additionalServiceCost = 0
        
    def __str__(self):
        return ('Account: {}, OrderManifest: {}, Status: {}, OrderId: {}, OrderPlaced: {}'
        .format(self.account, self.orderManifest, self.status, self.orderId, self.orderPlaced))
    
    def updateStatus(self, newStatus):
        self.status = newOrderStatus
        
    @abstractmethod
    def getOrderType(self):
        pass
    
    """
    These are additional service costs, depending on the order type.
    """
    @abstractmethod
    def calcAdditionalServiceCosts(self):
        pass

class DeliveryOrder(Order):
    
    def getOrderType(self):
        return "delivery"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 4.99
        
class CarryOutOrder(Order):
    def getOrderType(self):
        return "carry-out"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 0
    
class VolumeOrder(Order):
    def getOrderType(self):
        return "volume order"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 3.99
        
def generateRandomOrderId():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

def generateTimeStamp():
    return datetime.now();    
        
if __name__== '__main__':
    
    orderFactory = OrderFactory()
    
    deliveryOrder = orderFactory.createDeliveryOrder('1234','order')
    print(deliveryOrder)
    carryoutOrder = orderFactory.createDeliveryOrder('4567','order2')
    print(carryoutOrder)