#get the external gateway address using sockets

import subprocess

def get_external_ip():

    url = "http://ipecho.net/plain"
    p = subprocess.Popen(["wget", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = p.communicate()
    return output

print(get_external_ip())

#I think this is now in repo

