class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
        return True
    def make_payment(self, amount):
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""

  def __init__(self, customer, bank, acnt, limit, apr):
    """Create new predatory credit card instance.
    
    The initial balance is zero.

    customer  the name of the customer (e.g. 'John Brown')
    bank      the name of the bank (e.g. 'Bank of America')
    acnt      the acount identifier (e.g. '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit) # call super constructor
    self._apr = apr

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.
    
    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    success = super().charge(price) # call inherited method
    if not success:
      self._balance += 5 # assess penalty
    return success # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor
      

