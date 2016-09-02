def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    arr = []
    for i in env:
        arr += [i.encode]
    return arr 
