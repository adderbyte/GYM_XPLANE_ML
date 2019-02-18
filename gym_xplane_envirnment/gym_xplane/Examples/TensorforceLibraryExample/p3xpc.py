import socket
import struct
import select

class XPlaneConnect(object):
	'''XPlaneConnect (XPC) facilitates communication to and from the XPCPlugin.'''
	socket = None

	# Basic Functions dicker
	def __init__(self, xpHost = '127.0.0.1',clientAddr='0.0.0.0', xpPort = 49009 ,port = 1, timeout = 1000):
		'''Sets up a new connection to an X-Plane Connect plugin running in X-Plane.
			xpPort = 49009
			port = 0
			xpHost = 'localhost'
			Args:
			  xpHost: The hostname of the machine running X-Plane.
			  xpPort: The port on which the XPC plugin is listening. Usually 49007.
			  port: The port which will be used to send and receive data.
			  timeout: The period (in milliseconds) after which read attempts will fail.
		'''

		# Validate parameters
		#xpIP = None
		try:
			#temp = socket.gethostbyname(xpHost)
			#print('hostname address temp defined by me...', temp)
			#xpIP = temp
			socket.inet_pton(socket.AF_INET,xpHost)
			socket.inet_pton(socket.AF_INET,clientAddr)
			
			

		
		except:
			raise ValueError("Unable to resolve xpHost.")
		
		if xpPort < 0 or xpPort > 65535:
			raise ValueError("The specified X-Plane port is not a valid port number.")
		if port < 0 or port > 65535:
			raise ValueError("The specified port is not a valid port number.")
		if timeout < 0:
			raise ValueError("timeout must be non-negative.")

		print('checking Client Port ...', port)
		# Setup XPlane IP and port
		self.xpDst = (xpHost, xpPort)
		print('checking Destination Addr ...', self.xpDst)
		# Create and bind socket 10.42.0.1       
		clientAddr = (clientAddr, port)
		print('checking Client Addr ...', clientAddr)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		
		self.socket.bind(clientAddr)

		

		
		
		print('my socket', self.socket.getsockname())

		print('finished ...')

		timeout /= 1000.0
		self.socket.settimeout(timeout)

	def __del__(self):
		self.close()

	# Define __enter__ and __exit__ to support the `with` construct.
	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.close()

	def close(self):
		'''Closes the specified connection and releases resources associated with it.'''
		if self.socket is not None:
			self.socket.close()
			self.socket = None

	def sendUDP(self, buffer):
		'''Sends a message over the underlying UDP socket.'''
		# Preconditions
		if(len(buffer) == 0):
			raise ValueError("sendUDP: buffer is empty.")

		self.socket.sendto(buffer, 0, self.xpDst)

	def readUDP(self):
		'''Reads a message from the underlying UDP socket.'''
		#msgLen = 16384
		#chunks = []
		#bytes_recd = 0;

		
		
		return self.socket.recv(16384)
	
	# Configuration
	def setCONN(self, port):
		'''Sets the port on which the client sends and receives data.
		
			Args:
			  port: The new port to use.
		'''
		#Validate parameters        
		if port < 0 or port > 65535:
			raise ValueError("The specified port is not a valid port number.")

		#Send command
		buffer = struct.pack(("<4sxH", "CONN", port).encode('utf-8'))
		self.sendUDP(buffer)
		
		#Rebind socket
		clientAddr = (clientAddr, port)
		timeout = self.socket.gettimeout();
		self.socket.close();
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.socket.bind(clientAddr)

		self.socket.settimeout(timeout)

		#Read response
		buffer = self.socket.recv(1024)


	def getPOSI(self, ac = 0):
		'''Gets position information for the specified aircraft.

		Args:
		  ac: The aircraft to set the control surfaces of. 0 is the main/player aircraft.
		'''
		# Send request packed_data = s.pack(string.encode('ascii'))
		# the syntax below is also correct

		# buffer = struct.pack("<4sxB".encode('utf-8'), "GETP".encode('utf-8'),ac)
		buffer = struct.pack(b"<4sxB", b"GETP", ac)
		self.sendUDP(buffer)

		# Read response
		resultBuf = self.readUDP()
		#results = struct.unpack("<4sxBfffffff", resultBuf[:34])
		#print('I am position buffer', resultBuf)
		if len(resultBuf) != 34:
			raise ValueError("Unexpected response length.")

		result = struct.unpack("<4sxBfffffff", resultBuf)
		
		if result[0].decode("utf-8") != "POSI":
			raise ValueError("Unexpected header: " + result[0])

		# Drop the header & ac from the return value
		return result[2:]

	def sendPOSI(self, values, ac = 0):
		'''Sets position information on the specified aircraft.

			Args:
			  values: The position values to set. `values` is a array containing up to
				7 elements. If less than 7 elements are specified or any elment is set to `-998`,
				those values will not be changed. The elements in `values` corespond to the
				following:
				  * Latitude (deg)
				  * Longitude (deg)
				  * Altitude (m above MSL)
				  * Pitch (deg)
				  * Roll (deg)
				  * True Heading (deg)
				  * Gear (0=up, 1=down)
			  ac: The aircraft to set the control surfaces of. 0 is the main/player aircraft.
		'''
		# Preconditions
		if len(values) < 1 or len(values) > 7:
			raise ValueError("Must have between 0 and 7 items in values.")
		if ac < 0 or ac > 20:
			raise ValueError("Aircraft number must be between 0 and 20.")

		# Pack message
		buffer = struct.pack(b"<4sxB", b"POSI", ac)
		for i in range(7):
			val = -998
			if i < len(values):
				val = values[i]
			buffer += struct.pack("<f", val)

		# Send
		self.sendUDP(buffer)

	# Controls
	def getCTRL(self, ac = 0):
		'''Gets the control surface information for the specified aircraft.

		Args:
		  ac: The aircraft to set the control surfaces of. 0 is the main/player aircraft.
		'''
		# Send request
		buffer = struct.pack(b"<4sxB", b"GETC", ac)
		self.sendUDP(buffer)

		# Read response
		resultBuf = self.readUDP()
		msgL = type(resultBuf)
		length = len(resultBuf)
		#results = struct.unpack("<4sxBfffffff", resultBuf)
		#print('I am control buffer', results)
		#print('I am message length: ... ',msgL,length)

		#resultBuf = resultBuf[:31]
		#print(resultBuf)
		if len(resultBuf) != 31:
			raise ValueError("Unexpected response length.")

		result = struct.unpack("<4sxffffbfBf", resultBuf)
		if result[0].decode("utf-8") != "CTRL":
			raise ValueError("Unexpected header: " + result[0])

		# Drop the header from the return value
		result =result[1:7] + result[8:]
		return result

	def sendCTRL(self, values, ac = 0):
		'''Sets control surface information on the specified aircraft.

			Args:
			  values: The control surface values to set. `values` is a array containing up to
				6 elements. If less than 6 elements are specified or any elment is set to `-998`,
				those values will not be changed. The elements in `values` corespond to the
				following:
				  * Latitudinal Stick [-1,1]
				  * Longitudinal Stick [-1,1]
				  * Rudder Pedals [-1, 1]
				  * Throttle [-1, 1]
				  * Gear (0=up, 1=down)
				  * Flaps [0, 1]
				  * Speedbrakes [-0.5, 1.5]
			  ac: The aircraft to set the control surfaces of. 0 is the main/player aircraft.
		'''
		# Preconditions
		if len(values) < 1 or len(values) > 7:
			raise ValueError("Must have between 0 and 6 items in values.")
		if ac < 0 or ac > 20:
			raise ValueError("Aircraft number must be between 0 and 20.")

		# Pack message
		buffer = struct.pack(b"<4sx", b"CTRL")
		for i in range(6):
			val = -998
			if i < len(values):
				val = values[i]
			if i == 4:
				val = -1 if (abs(val + 998) < 1e-4) else val
				
				buffer += struct.pack(b"b", val)
			else:
				buffer += struct.pack("<f", val)
		buffer += struct.pack("B", ac)
		if len(values) == 7:
			buffer += struct.pack(b"<f", values[6])

		# Send
		self.sendUDP(buffer)


		
	# DREF Manipulation    
	def sendDREF(self, dref, values):
		'''Sets the specified dataref to the specified value.

			Args:
			  dref: The name of the datarefs to set.
			  values: Either a scalar value or a sequence of values.
		'''
		self.sendDREFs([dref], [values])

	def sendDREFs(self, drefs, values):
		'''Sets the specified datarefs to the specified values.

			Args:
			  drefs: A list of names of the datarefs to set.
			  values: A list of scalar or vector values to set.
		'''
		if len(drefs) != len(values):
			raise ValueError("drefs and values must have the same number of elements.")

		buffer = struct.pack(b"<4sx", b"DREF")
		for i in range(len(drefs)):
			dref = drefs[i]
			value = values[i]
			# Preconditions
			if len(dref) == 0 or len(dref) > 255:
				raise ValueError("dref must be a non-empty string less than 256 characters.")
			if value == None:
				raise ValueError("value must be a scalar or sequence of floats.")
		
			# Pack message
			if hasattr(value, "__len__"):
				if len(value) > 255:
					raise ValueError("value must have less than 256 items.")
				fmt = b"<B{0:d}sB{1:d}f".format(len(dref), len(value))
				buffer += struct.pack(fmt, len(dref), dref, len(value), value)
			else:
				fmt = b"<B{0:d}sBf".format(len(dref))
				buffer += struct.pack(fmt, len(dref), dref, 1, value)

		# Send
		self.sendUDP(buffer)

	def getDREF(self, dref):
		'''Gets the value of an X-Plane dataref.
			
			Args:
			  dref: The name of the dataref to get.

			Returns: A sequence of data representing the values of the requested dataref.
		'''
		return self.getDREFs([dref])#[0]

	def getDREFs(self, drefs):
		'''Gets the value of one or more X-Plane datarefs.

			Args:
			  drefs: The names of the datarefs to get.

			Returns: A multidimensional sequence of data representing the values of the requested
			 datarefs.
		'''
		# Send request
		buffer = struct.pack("<4sxB", b"GETD", len(drefs))
		for dref in drefs:
			#fmt = "<B{0:d}s".format(len(dref))
			fmt=bytes('<B{0:d}s'.format(len(dref), dref), 'utf-8')
			buffer += struct.pack(fmt, len(dref), dref.encode('utf-8'))
		self.sendUDP(buffer)

		# Read and parse response
		buffer = self.readUDP()
		resultCount = struct.unpack_from("B", buffer, 5)[0]
		#print(resultCount)
		offset = 6
		result = []
		for i in range(resultCount):
			rowLen = struct.unpack_from("B", buffer, offset)[0]
			offset += 1
			fmt = "<{0:d}f".format(rowLen)
			row = struct.unpack_from(fmt, buffer, offset)
			result.append(row)
			offset += rowLen * 4
		return result

	# Drawing
	def sendTEXT(self, msg, x = -1, y = -1):
		'''Sets a message that X-Plane will display on the screen.

			Args:
			  msg: The string to display on the screen
			  x: The distance in pixels from the left edge of the screen to display the
				 message. A value of -1 indicates that the default horizontal position should
				 be used.
			  y: The distance in pixels from the bottom edge of the screen to display the
				 message. A value of -1 indicates that the default vertical position should be
				 used.
		'''
		if y < -1:
			raise ValueError("y must be greater than or equal to -1.")

		if msg == None:
			msg = ""

		msgLen = len(msg)
		buffer = struct.pack("<4sxiiB" + str(msgLen) + "s", "TEXT", x, y, msgLen, msg)
		self.sendUDP(buffer)

	def sendVIEW(self, view):
		'''Sets the camera view in X-Plane

			Args:
			  view: The view to use. The ViewType class provides named constants
					for known views.
		'''
		# Preconditions
		if view < ViewType.Forwards or view > ViewType.FullscreenNoHud:
			raise ValueError("Unknown view command.")

		# Pack buffer
		buffer = struct.pack("<4sxi", "VIEW", view)

		# Send message
		self.sendUDP(buffer)

	def sendWYPT(self, op, points):
		'''Adds, removes, or clears waypoints. Waypoints are three dimensional points on or
		   above the Earth's surface that are represented visually in the simulator. Each
		   point consists of a latitude and longitude expressed in fractional degrees and
		   an altitude expressed as meters above sea level.

			Args:
			  op: The operation to perform. Pass `1` to add waypoints,
				`2` to remove waypoints, and `3` to clear all waypoints.
			  points: A sequence of floating point values representing latitude, longitude, and
				altitude triples. The length of this array should always be divisible by 3.
		'''
		if op < 1 or op > 3:
			raise ValueError("Invalid operation specified.")
		if len(points) % 3 != 0:
			raise ValueError("Invalid points. Points should be divisible by 3.")
		if len(points) / 3 > 255:
			raise ValueError("Too many points. You can only send 255 points at a time.")

		if op == 3:
			buffer = struct.pack(b"<4sxBB", b"WYPT", 3, 0)
		else:
			buffer = struct.pack(b"<4sxBB" + str(len(points)) + b"f", b"WYPT", op, len(points), *points)
		self.sendUDP(buffer)

	
class ViewType(object):
	Forwards = 73
	Down = 74
	Left = 75
	Right = 76
	Back = 77
	Tower = 78
	Runway = 79
	Chase = 80
	Follow = 81
	FollowWithPanel = 82
	Spot = 83
	FullscreenWithHud = 84
	FullscreenNoHud = 85
