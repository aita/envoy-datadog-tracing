from bottle import route, run, template, install
from ddtrace import tracer
from ddtrace.contrib.bottle import TracePlugin


@route('/')
def index():
    return 'hello'

plugin = TracePlugin(service="hello-app")
install(plugin)
run(host='0.0.0.0', port=8000)