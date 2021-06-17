''' C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge. '''



def charge(self, price):
		"""
		Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed, False if charge was denied
		"""
		if not isinstance(price, (float, int)):
			raise ValueError('price must be a number.')
		if price + self._balance > self._limit:
			print(f"Credit card with account number {self._account} denied. Accrued balance over limit.")
			return False
		else:
			self._balance += price
			self._charge_count += 1
			if self._charge_count > 10:
				self._balance += 1	#$1 surcharge for all calls after 10 charges
