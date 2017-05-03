"""
Your virus has caused a backdoor to open on the Skynet network enabling you to send new instructions in real time.
You decide to take action by stopping Skynet from communicating on its own internal network.
Skynet's network is divided into several smaller networks, in each sub-network is a Skynet agent tasked with
transferring information by moving from node to node along links and accessing gateways leading to other sub-networks.
Your mission is to reprogram the virus so it will sever links in such a way that the Skynet Agent is unable to access
another sub-network thus preventing information concerning the presence of our virus to reach Skynet's central hub.
"""


def select():
    for x in possible:
        if x in possible_S:
            return x
    return possible[0]

# - N, the total number of nodes in the level, including the gateways.
# - L, the number of links in the level.
# - E, the number of exit gateways in the level.
n, l, e = [int(i) for i in input().split()]

# generates the list of links between the notes
links = [[int(j) for j in input().split()] for i in range(l)]

# generates a list of gate indices
gates = [int(input()) for i in range(e)]

while True:
    si = int(input())  # initial start point
    possible_S = [i for i in links if si in i]  # possible indices the agent may move
    possible = [i for gate in gates for i in links if gate in i]

    # severs the link between the two nodes printed through the select function
    print("%s %s" % (select()[0], select()[1]))
