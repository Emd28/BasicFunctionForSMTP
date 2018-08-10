import smtplib


class Gmail:
	"""docstring for Gmail"""
	def __init__(self):
		super(Gmail, self).__init__()
		global smtp
		smtp = smtplib.SMTP('smtp.gmail.com:587') # Current server for gmail connection.

	def connectToGmail(self, user, password):
		self.user = user
		self.password = password
		self.smtp = smtp

		self.smtp.ehlo()
		self.smtp.starttls()

		return self.smtp.login(user, password) # Basic authentication and this keep connection alive

	def sendSimpleMailWithGmail(self, content, to_addrs, from_addr):
		self.content = content.encode('utf-8')
		self.from_addr = from_addr
		self.to_addrs = to_addrs
		self.smtp = smtp

		return self.smtp.sendmail(self.from_addr, self.to_addrs, self.content), self.smtp.quit()

	def sendMultipleMailWithGmail(self, content, from_addr, some_contact):
		self.content = content.encode('utf-8')
		self.from_addr = from_addr
		self.some_contact = some_contact
		self.smtp = smtp

		self.elements = [
			self.content,
			self.from_addr,
			self.some_contact,
			self.smtp
		]

		with open(self.some_contact, 'r') as infile:
			for line in infile:
				self.to_addrs = line.strip('\r\n')
				
				return self.smtp.sendmail(self.from_addr, self.to_addrs, self.content), self.smtp.quit()

class Live:
	"""docstring for Live"""
	def __init__(self):
		super(Live, self).__init__()
		global smtp
		smtp = smtplib.SMTP('smtp.live.com:587') # Current server for Live (like outlook) connection.

	def connectToLive(self, user, password):
		self.user = user
		self.password = password
		self.smtp = smtp

		self.smtp.ehlo()
		self.smtp.starttls()

		return self.smtp.login(user, password) # Basic authentication and this keep connection alive

	def sendSimpleMailWithLive(self, content, to_addrs, from_addr):
		self.content = content.encode('utf-8')
		self.from_addr = from_addr
		self.to_addrs = to_addrs
		self.smtp = smtp

		return self.smtp.sendmail(self.from_addr, self.to_addrs, self.content)

	def sendMultipleMailWithLive(self, content, from_addr, some_contact):
		self.content = content.encode('utf-8')
		self.from_addr = from_addr
		self.some_contact = some_contact
		self.smtp = smtp

		self.elements = [
			self.content,
			self.from_addr,
			self.some_contact,
			self.smtp
		]

		with open(self.some_contact, 'r') as infile:
			for line in infile:
				self.to_addrs = line.strip('\r\n')

				return self.smtp.sendmail(self.from_addr, self.to_addrs, self.content)
			
