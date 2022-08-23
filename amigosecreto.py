numparticipantes = int(input("Digite quantas pessoas estão participando: "))

participantes = {}

for pessoa in range(numparticipantes):
    participanteEPresentes = input("Digite o nome do participante e 3 presentes que ele gosta: ")
     
    listaParticipantes = participanteEPresentes.split()
    
    participante = listaParticipantes[0]
    
    participantes[participante] = (listaParticipantes[1], listaParticipantes[2], listaParticipantes[3])

cond = "continuar"

while(cond != "Fim."):
    chute = input("Digite o nome da pessoa e seu chute: ")

    if chute == "FIM":
        cond = "Fim."
        continue

    listaChute = chute.split()

    participante = listaChute[0]

    if participante not in participantes:
        print("Seu amigo não está participando do amigo secreto!")
        continue
    
    listaPresentes = participantes[participante]

    if listaChute[1] in listaPresentes:
        print("Uhul! Seu amigo secreto vai adorar")
    else:
        print("Tente Novamente!")