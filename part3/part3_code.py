from socket import *

serverPort = 6060
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    sentence = connectionSocket.recv(1024).decode()
    print(sentence+"\n")
    request = sentence.split()[1]
    print("the request is : " + request)
    if (request == '/' or request == '/index.html' or request == '/main_en.html' or request == '/en'): # The if statement checks whether the requested object is one of several specific values
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        fileminen = open("main_en.html", "rb")
        connectionSocket.send(fileminen.read())  # read the file that was open  when it called

    elif (request == '/ar'): # The if statement checks whether the requested object is one of several specific values
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        fileminen = open("main_ar.html", "rb")
        connectionSocket.send(fileminen.read())  # read the file that was open  when it called

    elif (request.endswith('.html')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filelink = open("myform.html", "rb")
        connectionSocket.send(filelink.read())

    elif (request.endswith('.css')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filecss = open("style.css", "rb")
        connectionSocket.send(filecss.read())

    elif (request.endswith('.png')):  # files with the extensions '.png' and '.jpg'.
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filepngimg = open("image3.png", "rb")
        connectionSocket.send(filepngimg.read())

    elif (request.endswith('.jpg')):  # The same process occurs for '.jpg' files,
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filejpgimg = open("image4.jpg", "rb")  # open the image with jpg extension.
        connectionSocket.send(filejpgimg.read())

    elif (request == '/so'):

        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (request == '/itc'):

        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://itc.birzeit.edu \r\n".encode())
        connectionSocket.send("\r\n".encode())

    else:  # scenario where a requested resource is not found by a client.
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        notFoundHtmlString = "<html>" \
                             "<head>" \
                             "<title>ERROR 404 </title>" \
                             "</head>" \
                             "<body>" \
                             "<pre>" \
                             "<p style ='font-size: 45px; text-align:center; color:Red'>" \
                             "The file is not found </p>" \
                             "<p style ='font-size: 25px; text-align:center; color:Black'>" \
                             "<b> Shahd Yahya 1210249 <b/></p>" \
                             "</p>" \
                             "<pre style='font-size: 25px; text-align:center;'>" \
                             f"The IP is: {ip}     " \
                             f"The port is: {port}" \
                             "</p>" \
                             "</body>" \
                             "</html>"
        notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
        connectionSocket.send(notFoundHtmlBytes)




connectionSocket.close()


