def wsgiApp(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = environ['QUERY_STRING'].split("&")
	str = ""
	for item in body:
		str += item
		str += "\n"
	start_response(status, headers)
	return [str]