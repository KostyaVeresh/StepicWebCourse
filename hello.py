from string import maketrans

def wsgiApp(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = (environ.get('wsgi.input')).translate(maketrans('&', '\n'))
	start_response(status, headers)
	return [body]