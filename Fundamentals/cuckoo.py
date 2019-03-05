# query

def query(key, table, list_of_hash_funcs):
	for func in list_of_hash_funcs:
		if key == table[func(key)]:
			return(table[func(key)])
	return('not found')

def insert(key,table,list_of_hash_funcs):
	# try inserting in slot
	for func in list_of_hash_funcs:
		if table[func(key)] == None or table[func(key)] == "dummy":
			table[func(key)] = key
			return(0)

	# insert in first slot and bump the rest around
	tried = []
	for func in list_of_hash_funcs:
		if func(key) in tried:
			return(1)
		bumped = table[func(key)]
		table[func(key)] = key
		tried.append(func(key))
		if insert(bumped,table,list_of_hash_funcs) == 0:
			return(0)
	return(1)