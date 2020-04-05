"""
Check that our payment method was authorized. We check two
This is an example of a Facade.
"""
class ValidatePayment:
    """
    This will validate our payment method when we call Authorize()
    @param paymentId - This is our payment id, which is used in the authorization of the payment.
    This would typically be a hash of various values that the payment system(s) can decrypt.
    """
    def __init__(self, paymentId):
        self.paymentId = paymentId
        self._previousDeclinedPaymentsStatus = False
        self._fraudCheckSystemStatus = False
        self._authCheckSystemStatus = False
        
    def __str__(self):
        return ('PaymentId: {}, previousDeclinedPayments: {}, fraudCheckSystem: {}, authCheckSystem: {}'
        .format(self.paymentId, self._previousDeclinedPaymentsStatus, self._fraudCheckSystemStatus, self._authCheckSystemStatus))
        
    def authorize(self):
        self._previousDeclinedPaymentsStatus = DeclinedOrderSystem.checkDeclinedOrders(self.paymentId)
        self._fraudCheckSystemStatus = FraudCheckSystem.fraudCheck(self.paymentId)
        self._authCheckSystemStatus = AuthCheckSystem.authCheck(self.paymentId)
        
class DeclinedOrderSystem:
    def checkDeclinedOrders(paymentId):
        # Stub - Here our system would check to see if payment was previously declined
        return True
    
class AuthCheckSystem:
    def authCheck(paymentId):
        # Stub - This might have an underlying call to some other system as well on whether the payment was authorized
        return True
    
class FraudCheckSystem:
    def fraudCheck(paymentId):
        # Stub - This might have an underlying call to some other system as well on whether the payment was reported lost / stolen / etc
        return True    

        
if __name__== '__main__':
    
    validatePayment = ValidatePayment('737388040230310231031231')
    #Pre-auth
    print(validatePayment)
    
    #Post-Auth
    validatePayment.authorize()
    print(validatePayment)