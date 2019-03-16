import os

def insertDb(client, otherParty):
    clientMessages = os.listdir(client)
    otherPartyMessages = os.listdir(otherParty)
    clientMessages = [client + '/' + clientMessage for clientMessage in clientMessages if '.txt' in clientMessage]
    otherPartyMessages = [otherParty + '/' + otherPartyMessage for otherPartyMessage in otherPartyMessages if '.txt' in otherPartyMessage]
    for clientMessage in clientMessages:
        with open(clientMessage) as f1:
            message1 = {}
            message1['53'] = [None, None]
            message1['56'] = [None, None]
            message1['57A'] = [None, None] 
            message1['58'] = [None, None]
            passed = False 
            for line in f1.readlines()[1:-1]:
                if line.strip().rsplit(":")[1] == '32B':
                    passed = True
                if line.strip().rsplit(":")[1] == '57A':
                    if not passed:
                        message1[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                    else:
                        message1[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                elif line.strip().rsplit(":")[1] == '53':
                    if not passed:
                        message1[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                    else:
                        message1[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                elif line.strip().rsplit(":")[1] == '58':
                    if not passed:
                        message1[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                    else:
                        message1[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                elif line.strip().rsplit(":")[1] == '56':
                    if not passed:
                        message1[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                    else:
                        message1[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                else:    
                    message1[line.strip().rsplit(":")[1]] = line.strip().rsplit(":")[2]
            for otherPartyMessage in otherPartyMessages:
                with open(otherPartyMessage) as f2:
                    message2 =  {}
                    message2['53'] = [None, None]
                    message2['56'] = [None, None]
                    message2['57A'] = [None, None] 
                    message2['58'] = [None, None]
                    passed = False 
                    for line in f2.readlines()[1:-1]:
                        if line.strip().rsplit(":")[1] == '32B':
                            passed = True
                        if line.strip().rsplit(":")[1] == '57A':
                            if  not passed:
                                message2[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                            else:
                                message2[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                        elif line.strip().rsplit(":")[1] == '53':
                            if  not passed:
                                message2[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                            else:
                                message2[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                        elif line.strip().rsplit(":")[1] == '58':
                            if  not passed:
                                message2[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                            else:
                                message2[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                        elif line.strip().rsplit(":")[1] == '56':
                            if  not passed:
                                message2[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                            else:
                                message2[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
                        else:    
                            message2[line.strip().rsplit(":")[1]] = line.strip().rsplit(":")[2]
                    matchingStatus = match(message1, message2)



def match(message1, message2):
    matchingStatus = {}
    matchingStatus["_20"] = False
    if message1['20'] == message2['20']:
        matchingStatus["_20"] = True

    matchingStatus["_22A"] = False
    if message1['22A'] == message2['22A']:
        matchingStatus["_22A"] = True


    matchingStatus["_22C"] = False
    if message1['22C'] == message2['22C']:
        matchingStatus["_22C"] = True


    matchingStatus["_94A"] = False
    if message1['94A'] == message2['94A']:
        matchingStatus["_94A"] = True
    
    matchingStatus["_82"] = False
    if message1['82'] == message2['87']:
        matchingStatus["_82"] = True

    matchingStatus["_87"] = False
    if message1['87'] == message2['82']:
        matchingStatus["_87"] = True

    matchingStatus["_77H"] = False
    if message1['77H'] == message2['77H']:
        matchingStatus["_77H"] = True


    matchingStatus["_30T"] = False
    if message1['30T'] == message2['30T']:
        matchingStatus["_30T"] = True

    matchingStatus["_30T"] = False
    if message1['30T'] == message2['30T']:
        matchingStatus["_30T"] = True

    matchingStatus["_30V"] = False
    if message1['30V'] == message2['30V']:
        matchingStatus["_30V"] = True

    matchingStatus["_36"] = False
    if message1['36'] == message2['36']:
        matchingStatus["_36"] = True


    matchingStatus["_33B"] = False
    if message1['33B'] == message2['32B']:
        matchingStatus["_33B"] = True

    matchingStatus["_53"] = False
    if '53' not in message1:
        message1['53'] = None
    if '53' not in message2:
        message2['53'] = None
    if message1['53'] == message2['53']:
        matchingStatus["_53"] = True

    matchingStatus["_56"] = [False, False]
    if message1['56'][0] == message2['56'][1]:
        matchingStatus["_56"][0] = True
    if message1['56'][1] == message2['56'][0]:
        matchingStatus["_56"][1] = True

    matchingStatus["_57A"] = [False, False]
    if message1['57A'][0] == message2['57A'][1]:
        matchingStatus["_57A"][0] = True
    if message1['57A'][1] == message2['57A'][0]:
        matchingStatus["_57A"][1] = True


    matchingStatus["_58"] = [False,False]
    if message1['58'][0] == message2['58'][1]:
        matchingStatus["_58"][0] = True
    if message1['58'][1] == message2['58'][0]:
        matchingStatus["_58"][1] = True

    matchingStatus["_32B"] = False
    if message1['32B'] == message2['33B']:
        matchingStatus["_32B"] = True


    matchingStatus["_53"] = [False,False]
    if message1['53'][0] == message2['53'][1]:
        matchingStatus["_53"][0] = True
    if message1['53'][1] == message2['53'][0]:
        matchingStatus["_53"][1] = True
    
    return matchingStatus

    

