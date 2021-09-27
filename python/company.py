class Company:
	# This is the constructor of the class. It gets called every time a new Company object is created.
	def __init__(self, name):
		self.name = name
		self.catalog = {}
		self.employees = []
		# Add other fields here!

	# This is the constructor of the employee.
	def __init__(self, name, company, role = 1):
		self.name = name
		self.company = company
		self.role = role
	
	# The self parameter is a reference to the current instance of the class,
	# and is used to access variables that belong to the class.
	# Don't forget to add other parameters (arguments) as required.
	def add_product(self, name, price):
		self.catalog[name] = price
		return
	
	def add_employee(self, employee):
		self.employees.append[employee]
		return