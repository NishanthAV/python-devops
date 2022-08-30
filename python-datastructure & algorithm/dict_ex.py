server_1 = {
  "env":"DEV",
  "server":"aws linux 2",
  "ram":8096,
  "cpu":4,
  "active":True
}
server_2 = {
  "env":"QA",
  "server":"ubuntu linux",
  "ram":10240,
  "cpu":8,
  "active":False
}

env_details = [server_1,server_2]

for env in env_details:
    for key,value in env.items(): 
        if key == "active" and value==True:
            print(env.values())   
    
#print(env)
#print(dict_of_items.get("env"))

#if dict_of_items["active"]:
#    print("server details")
#   print("Environment: ")