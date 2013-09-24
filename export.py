class Export:

	html = ""
	json = ""
	
	def print_to_console(self):
	
		print self.html
	
	def save_new_file(self):
		
		filename = raw_input("Give name for the file: ")
		
		if filename[-4:] != '.htm':
			filename+='.htm'
		
		with open(filename, "wt") as out:
			for line in open("template.txt"):
				out.write(line.replace('{content}', self.html))
		
		print 'File has been created'
		
	def write_vam_table(self):
	
		self.html = """
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>Room</th>
					<th>Original Location</th>
					<th>Year</th>
				</tr>
			</thead>
			
			<tbody>
		"""
		
		if self.json['meta']['result_count'] == 0:
			self.html+='<tr><td colspan="4">No results to display</td></tr>'
			
		else:
			for item in self.json['records']: 
				
				self.html+='<tr>'
				
				if item['fields']['title']:
					self.html+='<td>' + item['fields']['title'] + ' - ' + item['fields']['object'] + '</td>'
					
				else:
					self.html+='<td>' + item['fields']['object'] + '</td>'
					
				self.html+='<td>' + item['fields']['location'] + '</td>'
				self.html+='<td>' + item['fields']['place'] + '</td>'
				self.html+='<td>' + str(item['fields']['year_start']) + '</td>'
				self.html+='</tr>' + "\n"
			
			self.html+= """
				</tbody>
			</table>
			"""
			
			return self.html