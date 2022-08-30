list_of_cloud_serv =list(["aws","azure","gcp"]) #1
list_of_envs = ["dev","stage","prod","tst","qa"]
list_of_envs.append("client")

for i in list_of_envs:
    print("Deploying the source code")
    print(i)


a = 2
list_of_envs.insert(1,"testing")
print(list_of_envs)

