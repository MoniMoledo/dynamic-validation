class Type:

	supportedTypes = []
	typeDefinitions = []
	
	def __init__(self):
		self.supportedTypes = []
		self.typeDefinitions = []

	def set_supported_type(self, supportedType):
		if supportedType is "default":
			self.supportedTypes.extend(["string", "number", "boolean"])
		else:
			self.supportedTypes.append(supportedType)

	def set_optional_type(self, isRequired):
		if not isRequired:
			self.supportedTypes.append("null")

	def set_lenght_requirements(self, maxLen, minLen):
		typeDef = { "type" : "string" }
		hasLenghtRequirements = False
		if maxLen is not None: 
			typeDef["maxLength"] = maxLen
			hasLenghtRequirements = True
		if minLen is not None:
			typeDef["minLength"] = minLen
			hasLenghtRequirements = True

		if(hasLenghtRequirements):
			if("null" in self.supportedTypes):
				self.supportedTypes = []
				self.supportedTypes.append("null")
			else:
				self.supportedTypes = []

			self.typeDefinitions.append(typeDef)

	def get_type_requirements(self):
		for t in self.supportedTypes:
			typeDef = { "type" : t }
			self.typeDefinitions.append(typeDef)

		typeRequirements = { "anyOf" : self.typeDefinitions }
		return typeRequirements