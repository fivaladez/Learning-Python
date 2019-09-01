# EJ31_P2 Urllib

# Modules:
# request       - open URL
# response      - used internally
# error         - request exceptions
# parse         - useful URL functions
# robotparser   - robots.txt files

from urllib import request

resp = request.urlopen("https://wwww.wikipedia.org")

print type(resp)

# HTTP Status Codes
# 200: OK
# 400: Bad Request
# 403: Forbidden
# 404: Not Found

print resp.code
