#! /usr/bin/env python

records = {}

filename = "swg.txt"

def getRecords():
	search = "record name is "
	file = open(filename, "r")
	
	for line in file:
		line = line.replace("\r\n", "")
		if search in line:
			match = line[len(search):]
			
			recordname = match[0:match.index(" ")]
			# print >> newfile, match[0:match.index(" ")]
			# print recordname
			records[recordname] = []
		
		if line != "":
			if "field " in line:
				if "ordered by field" in line:
					continue	
				field = line[len("field "):]
				varType = field[field.index("is ") + len("is "):]

				field = field[0:field.index(" ")]

				# print "\t" + field + ":\t" + varType
				if "indexed by" in varType:
					varType = varType[0: varType.index("indexed by") - 1]

				if "alnum size " in varType:
					pos = varType.index("alnum size ") + len("alnum size ")
					if " " in varType[pos:]:
						varType = varType[pos:]
						varType = "VARCHAR(" + varType[0:varType.index(" ")] + ")"
					else:
						varType = "VARCHAR(" + varType[pos:] + ")"
				if "long by " in varType:
					varType = "DECIMAL(10)"
				if "long decimals " in varType:
					pos = varType.index("long decimals ") + len("long decimals ")
					varType = "DECIMAL(10," + varType[pos:] + ")"
				if "short decimals " in varType:
					pos = varType.index("short decimals ") + len("short decimals ")
					varType = "DECIMAL(10," + varType[pos:] + ")"
				if "float decimals " in varType:
					pos = varType.index("float decimals ") + len("float decimals ")
					varType = "DECIMAL(10," + varType[pos:] + ")"
				if "date" in varType:
					varType = "VARCHAR(30)"
				# if "record " in varType:
				# 	print "record name: " + recordname + "\nfield: " + field + "\nvalue: " + varType + "\n"

				records[recordname].append({field:varType})
	file.close()

def createPrimaryKey(name):

	new_name = []

	if "_" in name:
		name = name.split("_")

		for elem in name:
			new_name.append(elem.title())
		new_name[0] = new_name[0].lower()

		converted_str = "".join(new_name) + "ID"
	else:
		converted_str = name.lower() + "ID"

	return converted_str


def createQuery():
	file = open("queries.txt", "w")
	target_file = open("target_records.txt", "r")

	for line in target_file:
		for name in records:
			line = line.replace("\n", "")
			if line == name:
				# print "line: " + line + "\tname: " + name
				primaryKey = createPrimaryKey(name)
				query = "CREATE TABLE `" + name + "` (`" + primaryKey + "` int(11) NOT NULL AUTO_INCREMENT, "
				# print >> file, name + "["

				for elem in records[name]:
					for key, val in elem.items():
						if "record" not in val:
							query += "`" + key + "` " + val + " DEFAULT NULL,"
							# print >> file, key + ":" + val + "|"
						else:
							print "in table '" + name + "', field '" + key + "' is record '" + val[len("record "):] + "'"
				# print >> file, "]"
				query += "PRIMARY KEY (`" + primaryKey + "`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;\n"
				print >> file, query
	file.close()
	target_file.close()

getRecords()
createQuery()