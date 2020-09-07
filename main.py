import pygame
from Interface import Interface


def main() :
    #część inicjalizacyjna :
    print("Hello")
    pygame.init()
    time = 0.0
    clock = pygame.time.Clock()
    interface = Interface(talia_gracza,talia_gracza_po_spilt,talia_krupiera)
    game_work = True

    time2 = 0.0
    #Pętla główna
    while game_work:
        #cykle
        time += clock.tick()

        if time > (1000 / 5): #20 cykli na sekunde
            time2 += time
            time = 0.0

            interface.update()
            print("")
            print(interface.get_feedback())



talia_gracza = [
        (11,"As","Pik"),
        (3,"3","Kier"),
        (5,"5","Karo"),
        (7,"7","Pik"),
        (9,"9","Trefl"),
        (10,"Dama","Pik"),
        (11,"As","Pik"),
        (10,"Król","Karo")
        ]

talia_gracza_po_spilt = [
        #(1,"As","Pik"),
        #(3,"3","Kier")
        ]

talia_krupiera = [
        (11,"As","Pik"),
        (105,"5","Trefl"),
        ]
if __name__=="__main__":
    main()