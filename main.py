
from core.brain import NexusBrain
from memory.database import init_db


init_db()

nexus = NexusBrain()

print("==============================")
print("       NEXUS AI SYSTEM")
print("==============================")

print(nexus.start())
print("NEXUS : Tu peux me dire 'retiens que...' pour mémoriser une information.")

while True:

    message = input("\nToi : ")

    if message.lower().strip() in ["quit", "exit", "stop"]:
        print("NEXUS : À bientôt champion !")
        break

    response = nexus.respond(message)

    print("NEXUS :", response)
