from pyscript import document, window

def checkTeamStatus():
    teamSelect = document.getElementById('selectTeam')
    selectedTeam = teamSelect.value
    resultDiv = document.getElementById('result')
    
    if selectedTeam == 'Team A':
        registered = document.getElementById('registered').checked
        medicalCert = document.getElementById('medicalCert').checked
        
        if registered and medicalCert:
            resultDiv.innerHTML = 'you are in red bulldogs, you are now fully able 2 participate! ( ´ ꒳ ` ) ♡' #when both boxes r checked
        elif registered:
            resultDiv.innerHTML = 'you are in red bulldogs, you are registered but you dont have a medical certificate (￣ ￣|||)'
        elif medicalCert:
            resultDiv.innerHTML = 'you are in red bulldogs, but you are not registered...`(°ー°〃)'
        else:
            resultDiv.innerHTML = 'you are not able to participate!(＃`Д´)' #these r here so that when the user doesnt check any of the boxes this shows up
    elif selectedTeam == 'Team B':
        registered = document.getElementById('registered').checked
        medicalCert = document.getElementById('medicalCert').checked
        
        if registered and medicalCert:
            resultDiv.innerHTML = 'you are in blue bears, you are now fully able 2 participate! ( ´ ꒳ ` ) ♡'
        elif registered:
            resultDiv.innerHTML = 'you are in blue bears, you are registered but you dont have a medical certificate (￣ ￣|||)' #when only the registered box has only been checked
        elif medicalCert:
            resultDiv.innerHTML = 'you are in blue bears, but you are not registered...`(°ー°〃)'
        else:
            resultDiv.innerHTML = 'you are not able to participate!(＃`Д´)'
    elif selectedTeam == 'Team C':
        registered = document.getElementById('registered').checked
        medicalCert = document.getElementById('medicalCert').checked
        
        if registered and medicalCert:
            resultDiv.innerHTML = 'you are in green hornets, you are now fully able 2 participate! ( ´ ꒳ ` ) ♡'
        elif registered:
            resultDiv.innerHTML = 'you are in green hornets, you are registered but you dont have a medical certificate (￣ ￣|||)'
        elif medicalCert:
            resultDiv.innerHTML = 'you are in green hornets, but you are not registered...`(°ー°〃)' #when the medical certificate box has only been checked
        else:
            resultDiv.innerHTML = 'you are not able to participate!(＃`Д´)'
    elif selectedTeam == 'Team D':
        registered = document.getElementById('registered').checked
        medicalCert = document.getElementById('medicalCert').checked
        
        if registered and medicalCert:
            resultDiv.innerHTML = 'you are in yellow tigers, you are now fully able 2 participate! ( ´ ꒳ ` ) ♡'
        elif registered:
            resultDiv.innerHTML = 'you are in yellow tigers, you are registered but you dont have a medical certificate (￣ ￣|||)'
        elif medicalCert:
            resultDiv.innerHTML = 'you are in yellow tigers, but you are not registered...`(°ー°〃)'
        else:
            resultDiv.innerHTML = 'you are not able to participate!(＃`Д´)'
    else:
        resultDiv.innerHTML = 'select a team plz' #when they havent done anything and just pressed the check button...

def clearStatus():
    document.getElementById('registered').checked = False
    document.getElementById('medicalCert').checked = False
    document.getElementById('selectTeam').value = ''
    document.getElementById('result').innerHTML = ''

window.checkTeamStatus = checkTeamStatus

window.clearStatus = clearStatus
