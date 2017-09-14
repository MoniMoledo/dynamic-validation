class Type:

	supported_types = []
	type_definitions = []
	
	def __init__(self):
		self.supported_types = []
		self.type_definitions = []

	def set_supported_type(self, supported_type):
		if supported_type is "default":
			self.supported_types.extend(["string", "number", "boolean"])
		else:
			self.supported_types.append(supported_type)

	def set_optional_type(self, is_required):
		if not is_required:
			self.supported_types.append("null")

	def set_lenght_requirements(self, maxLen, minLen):
		type_def = { "type" : "string" }
		has_lenght_requirements = False
		if maxLen is not None: 
			type_def["maxLength"] = maxLen
			has_lenght_requirements = True
		if minLen is not None:
			type_def["minLength"] = minLen
			has_lenght_requirements = True

		if(has_lenght_requirements):
			if("null" in self.supported_types):
				self.supported_types = []
				self.supported_types.append("null")
			else:
				self.supported_types = []

			self.type_definitions.append(type_def)

	def get_type_requirements(self):
		for t in self.supported_types:
			type_def = { "type" : t }
			self.type_definitions.append(type_def)

		type_requirements = { "anyOf" : self.type_definitions }
		return type_requirements