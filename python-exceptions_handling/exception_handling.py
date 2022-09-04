import builtins

cloud_envs = ["AWS","AZURE","GCP"]

try:
    print(cloud_envs[200])
    raise("This is a new exception")
except:
    print("exceptions handled")
finally:
    print("I will execute code anyways")

print("This code should run")

try:
    print(cloud_envs[200])
    a=10,
    b=0,
    c=a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)

print(dir(builtins))
