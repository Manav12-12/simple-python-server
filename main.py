import socket

SER_PORT = 8080
SER_ADD = '0.0.0.0'

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socks.bind((SER_ADD, SER_PORT))
socks.listen(5)
print(f'Server is listening on port {SER_PORT}')

while True:
  
  '''
  Accepting the connection from the client then receiving the request and decoding it to utf-8
  Then splitting the request to get the first line of the request
  Then splitting the first line to get the http method and the path
  '''
  
  konne_kon , konne_add = socks.accept()
  konne_req = konne_kon.recv(1500).decode()
  print(f'Request from client: {konne_req}')
  first_head = (konne_req.split('\n')[0]).split(' ')
  http_meth = first_head[0]
  path = first_head[1]
  
  
  '''
  Checking if the http method is GET or POST
  If the method is GET then checking the path
  If the path is '/' then opening the index.html file and reading it
  If the path is '/randm' then opening the randm.json file and reading it
  '''
  
  if http_meth == 'GET':
    
    if path == '/':
      konne_file = open('index.html')
      kontent = konne_file.read()
      konne_file.close()
      konne_headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': len(kontent),
        'Connection': 'close'
      }
    elif path == '/randm':
      konne_file = open('randm.json')
      kontent = konne_file.read()
      konne_file.close()
      konne_headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': len(kontent),
        'Connection': 'close'
      }
      
      # the place where some more magic happens where the headers are joined to the response and sent to the client
      
    header_str = ''.join(f'{key}: {value}\n' for key, value in konne_headers.items())
    response = 'HTTP/1.1 200 OK\n' + header_str + '\n' + kontent
    
  # if not proper request then sending 405 METHOD NOT ALLOWED
  
  else:
      kontent = 'ONLY GET AND POST CAN BE DONE'
      konne_headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': len(kontent),
        'Connection': 'close'
      }
      header_str = ''.join(f'{key}: {value}\n' for key, value in konne_headers.items())
      response = 'HTTP/1.1 405 METHOD NOT ALLOWED \n' + header_str + '\n' + kontent
      
  #sending the response to the client
  
  konne_kon.sendall(response.encode())
  konne_kon.close()
      
    
