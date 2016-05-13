def wsgiApp(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = environ['wsgi.input'].read()
	start_response(status, headers)
	return [body]