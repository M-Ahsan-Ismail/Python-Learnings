# List = ['a', 'b', 'c', 'e', 'e', 'c', 'b', 'a', 'g']
# Done = []
# Duplicates = []
#
# R1 = [
#     (f'Item: {x} Occurs: {List.count(x)}', Duplicates.append(x) if List.count(x) > 1 else None) for x in List if
#     (x not in Done and not Done.append(x))
# ]

# ---------------------------: Removing -: None :- coming as 2nd chr in tuple  :------------------------

# By Comprehension :

# R2 = []
# Removing_Comprehension = [
#     R2.append(tuple(i for i in value if i is not None)) for index, value in enumerate(R1) if len(value) > 1
# ]
# R1.clear()
# R1.extend(R2)
# print(R1)

# By Looping :

# R2 = []
# for index, value in enumerate(R1):
#     if len(value) > 0:
#         List_Tuple = [i for i in value if i is not None]
#         R2.append(tuple(List_Tuple))
# R1.clear()
# R1.extend(R2)
# print(R1)


# -------------------:    Select specific indexes in tuple , discard remaining   :------------Old Way--------------------
# R1 = [
#     (f'Item: {x} Occurs: {List.count(x)}', Duplicates.append(x) if List.count(x) > 1 else None) for x in List if
#     (x not in Done and not Done.append(x))
# ]

# Tuples are immutable so we have to create new to rearrange them and select indexes manually.
# Tuple = ((1,2,3),(4,5,6),(7,8,9))
# Tuple = ((Tuple[0][0],Tuple[0][1]),) + Tuple[1:]
# print(Tuple) # ((1, 2), (4, 5, 6), (7, 8, 9))

# for index , value in enumerate(R1):
#     if len(value) > 1:
#         print(f'Hitting --->  Index: {index}  Value: {value[1]}')
#         R1[index] = (value[0],)
#         print(R1)
#
# Removing = [
#     (f'Hitting --->  Index: {x}  Value: {v[1]}' , (v[0],))   for x, v in enumerate(R1) if len(v) > 1
# ]
#
# print(Removing)


R1 = [
    ('A', 'B', 'C'),
    ('B', 'D'),
    ('M', 'P')
]

opened = []
opened_list = []
Result = []
Duplicte = []

for index, value in enumerate(R1):
    for inx, item in enumerate(value):
        vals = R1[index][inx]
        opened.append(vals)
        opened_list.append([index, vals])

# print('Opened: ',opened)
# print('Opened List: ',opened_list)

for index, value in enumerate(opened_list):
    for inx in range(index, len(opened_list)):
        if index != inx and value[0] != opened_list[inx][0] and value[1] == opened_list[inx][1]:
            Duplicte.append(value)

# print('Duplicates: ',Duplicte)

# if opened_list[index][1] != opened_list[inx][1]:
#     # print(value,opened_list[inx])
#     Result.append(value)
#     Result.append(opened_list[inx])


# -------------------- Rest Apis ---------------------------:
#
#
# Rest api means REpresentational state transfer , allows for communication b/w devices over internet as client and server.
# Send Request , Receive response in JSOn format
# Rest is architectural design , HTTP is protocol for data transfer and rules for communication over web.
# Rest uses http to interact with resources(databases).
#
# HTTP method ----> POST, GET, PUT, PATCH, DELETE
#
# Features----:
#   1): Stateless:- every http request from client to server must contains all data required to understand the request, as server does not store any information about any past interaction.
#       Server does not store any info or session.
#       So that's why:
#               Simple:   no need to manage sessions
#               Reliable: server crash won't loose user session info.
#               Scalable: Since server does not store any clint session data so any request from any client can be handled by any server(horizontal scaling).
#                         If you have 10 servers, a load balancer can send request to any.
#
#   2): Client-Server Architecture:
#                                   RESTful APIs are based on a client-server model, where the client and server operate independently, allowing scalability.
#
#   3): Cacheable:  cacheability means that responses from the server can be saved by the client or (browsers, proxies , CDNs ) so that same future request dont have to go to server for data.
#                   Performance improved and reduces load on server
#
#
#   4): Layered system: means api architecture can be organized into multiple layers, like security , load-balancing , caching etc.
#       Example:
#               client                      → Web browser, mobile app, or frontend.
#               API Gateway / Load Balancer → Routes traffic to backend servers.
#               Caching Layer               → e.g., Cloudflare, Varnish — stores previous responses.
#               Authentication Layer        → Validates API keys, JWT tokens, CSRF tokens.
#               API logic                   → Handles business logic and serves data.
#               Database Layer              → Stores user and application data.
#
# 1. GET Method: The HTTP GET method is used to read or retrieve  a resource.
#               In the safe path, GET returns a data in XML or JSON and an HTTP response code of 200 (OK).
#               In an error case, it most often returns a 404 (NOT FOUND) or 400 (BAD REQUEST).
#
# 2. POST Method: POST method commonly used to create new resources.
#                Upon successful creation, the server returns HTTP status 201 (Created).
#
# 3. PUT Method: Used for full object-data replacement.
#               When we use put we says here the final versio of that record, even original record have 5 fields having data but now we send 2 other 3 will be lost.
#               So if we are using put , should send whole object not partial.
#               Odoo is smarter and does NOT follow this strict rule, Even if you're using PUT.
#
# 4. PATCH Method: PATCH is an HTTP method used to partially update a resource.
#                 Unlike PUT, PATCH only requires the fields that need to be updated to be sent in the request.
#                 It modifies specific parts of the resource rather than replacing the entire resource.
#
# 5. DELETE Method: It is used to delete a resource.
#
#
#
#
#












