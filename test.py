# import docker
# client = docker.from_env()
# image = client.images.pull("alpine")
# print(image.id)

# import docker
# client = docker.from_env()
# print(client.containers.run("alpine", ["echo", "hello", "world"]))

import docker
client = docker.from_env()
container = client.containers.run("rocker/shiny-verse", detach=True, ports={'3838/tcp':8888})
print(container.id)
container.stop()