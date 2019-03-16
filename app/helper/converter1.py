import os

def insertDb(client, otherParty):
    clientMessages = os.listdir(client)
    otherPartyMessages = os.listdir(otherParty)
    clientMessages = [client + '/' + clientMessage for clientMessage in clientMessages if '.txt' in clientMessage]
    otherPartyMessages = [otherParty + '/' + otherPartyMessage for otherPartyMessage in otherPartyMessages if '.txt' in otherPartyMessage]
    
    clientActualMessages = []
    for clientMessage in clientMessages:
        clientActualMessages.append(processMessages(clientMessage))
    otherPartyActualMessages = []
    for otherPartyMessage in otherPartyMessages:
        otherPartyActualMessages.append(processMessages(otherPartyMessage))
    final_results = []
    for clientMessage in clientActualMessages:
        for otherPartyMessage in otherPartyActualMessages:
            matchResult = match(clientMessage, otherPartyMessage)
            decision = matchingOnStatus(matchResult)
            final_results.append([clientMessage, otherPartyMessage, matchResult, decision])
    return final_results



def processMessages(clientMessage):
    with open(clientMessage) as f1:
        message1 = {}
        message1['53'] = [None, None]
        message1['56'] = [None, None]
        message1['57A'] = [None, None] 
        message1['57D'] = [None, None] 
        message1['58'] = [None, None]
        passed = False 
        for line in f1.readlines()[1:-1]:
            if line.strip().rsplit(":")[1] == '32B':
                passed = True
                curr = line.strip().rsplit(":")[2].split()[0]
                amm = float(line.strip().rsplit(":")[2].split()[1])
                message1[line.strip().rsplit(":")[1]] = [curr, amm]
            elif line.strip().rsplit(":")[1] == '33B':
                curr = line.strip().rsplit(":")[2].split()[0]
                amm = float(line.strip().rsplit(":")[2].split()[1])
                message1[line.strip().rsplit(":")[1]] = [curr, amm]
            elif (line.strip().rsplit(":")[1] == '57A' or 
                line.strip().rsplit(":")[1] == '57D' or 
                line.strip().rsplit(":")[1] == '53' or 
                line.strip().rsplit(":")[1] == '58' or 
                line.strip().rsplit(":")[1] == '56'):
                if not passed:
                    message1[line.strip().rsplit(":")[1]][0] = line.strip().rsplit(":")[2]
                else:
                    message1[line.strip().rsplit(":")[1]][1] = line.strip().rsplit(":")[2]
            else:    
                message1[line.strip().rsplit(":")[1]] = line.strip().rsplit(":")[2]
    return message1

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
    if '94A' not in message1:
        message1['94A'] = None
    if '94A' not in message2:
        message2['94A'] = None
    if message1['94A'] == message2['94A']:
        matchingStatus["_94A"] = True
    
    matchingStatus["_82"] = False
    if '82' not in message1:
        message1['82'] = None
    if '87' not in message2:
        message2['87'] = None
    if message1['82'] == message2['87']:
        matchingStatus["_82"] = True

    matchingStatus["_87"] = False
    if '87' not in message1:
        message1['87'] = None
    if '82' not in message2:
        message2['82'] = None
    if message1['87'] == message2['82']:
        matchingStatus["_87"] = True

    matchingStatus["_77H"] = False
    if message1['77H'] == message2['77H']:
        matchingStatus["_77H"] = True


    matchingStatus["_30T"] = False
    if message1['30T'] == message2['30T']:
        matchingStatus["_30T"] = True

    matchingStatus["_30V"] = False
    if message1['30V'] == message2['30V']:
        matchingStatus["_30V"] = True

    matchingStatus["_36"] = False
    if message1['36'] == message2['36']:
        matchingStatus["_36"] = True


    matchingStatus["_33B"] = [False,False]
    if message1['33B'][0] == message2['32B'][0]:
        matchingStatus["_33B"][0] = True
    if message1['33B'][1] == message2['32B'][1]:
        matchingStatus["_33B"][1] = True

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
    if message1['57A'][0] == message2['57D'][1]:
        matchingStatus["_57A"][0] = True
    if message1['57A'][1] == message2['57D'][0]:
        matchingStatus["_57A"][1] = True

    matchingStatus["_57D"] = [False, False]
    if message1['57D'][0] == message2['57A'][1]:
        matchingStatus["_57D"][0] = True
    if message1['57D'][1] == message2['57A'][0]:
        matchingStatus["_57D"][1] = True


    matchingStatus["_58"] = [False,False]
    if message1['58'][0] == message2['58'][1]:
        matchingStatus["_58"][0] = True
    if message1['58'][1] == message2['58'][0]:
        matchingStatus["_58"][1] = True

    matchingStatus["_32B"] = [False, False]
    if message1['32B'][0] == message2['33B'][0]:
        matchingStatus["_32B"][0] = True
    if message1['32B'][1] == message2['33B'][1]:
        matchingStatus["_32B"][1] = True


    matchingStatus["_53"] = [False,False]
    if message1['53'][0] == message2['53'][1]:
        matchingStatus["_53"][0] = True
    if message1['53'][1] == message2['53'][0]:
        matchingStatus["_53"][1] = True
    
    return matchingStatus

def matchingOnStatus(matchingStatus):
    if (matchingStatus['_82'] == True and 
        matchingStatus['_87'] == True and 
        matchingStatus['_77H'] == True and 
        matchingStatus['_30T'] == True and 
        matchingStatus['_30V'] == True and 
        matchingStatus['_36'] == True and 
        matchingStatus['_32B'] == [True,True] and 
        matchingStatus['_56'] == [True, True] and 
        # matchingStatus['_57A'] == [True, True] and 
        # matchingStatus['_57D'] == [True, True] and 
        matchingStatus['_58'] == [True, True] and 
         matchingStatus['_33B'] == [True, True] ) :
        return "MATCHED"
    elif (matchingStatus['_30V'] == True and 
        matchingStatus['_36'] == True and 
        matchingStatus['_32B'] == [True,True] and 
        matchingStatus['_33B'] == [True, True] and
        matchingStatus['_30V'] == True):
        
        return "CLOSEFIT"
    else:
        return "UNMATCH"
    