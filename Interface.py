import pygame
#Do czyszczenia konsoli
import os

gambit = {
      "Dobranie karty"      :  1,
      "Niedopieranie karty" :  2,
      "Podwojenie stawki"   :  3,
      "Rozdwoić karty"      :  4,
      "Ubezpieczenie"       :  5
}

class Interface():

    def __init__(self,_player_cards : list,_second_player_cards :list,_casino_cards :list):
        self.player_cards = _player_cards
        self.second_player_cards = _second_player_cards
        self.casino_cards = _casino_cards
        self.__display_cards()
        self.feedback = 0

    def update(self):
        text = input()
        if text in gambit:
            if self.feedback != 0 :
                self.__display_cards()
            self.feedback = gambit[text]
        elif int(text) in gambit.values():
            if self.feedback != 0 :
                self.__display_cards()
            self.feedback = int(text)
        else:
            self.feedback = 0
            self.__display_cards(False)


    def get_feedback(self):
        feedback_copy = self.feedback
        self.feedback = 0
        return feedback_copy
    def __card_to_string(self, cards : list):
        string = ""
        for i in cards :
            if i[0] >= 100:                 #polecenie wywoływane kiedy w talii jest karta zakryta
                string +=  "X_Karta_Zakryta_X"
            else :
                string += i[1]
                string += "_"
                string += i[2]
                string += "   "
        return string

    def __clear(self):
            # check and make call for specific operating system
            os.system('cls' if os.name=='nt' else 'clear')

    def __gambit(self) -> list : #gambit - ruch funkcja zwraca listę ( numeryczną ) wszystkich dozwolonych ruchów
        gambit_list = [1,2]
        if(len(self.player_cards)==2):
            gambit_list.append(3)
        if(self.player_cards[0][1] == self.player_cards[0][1] and self.second_player_cards == [] ):
            gambit_list.append(4)
        # Poniższe kod sprawdza czy krupier ma odsłoniętego asa
        is_As = False
        if (self.casino_cards[0][1] == "As" and self.casino_cards[0][0] >= 100):
            is_As = True
        elif (self.casino_cards[1][1] and self.casino_cards[1][0] >= 100):
            is_As = True
        if (is_As):
            gambit_list.append(5)

        return gambit_list




    def __display_cards(self,error_communicat: bool = False):
        self.__clear()

        print("Karty Krupiera : ")
        print(self.__card_to_string(self.casino_cards))
        print("")
        print("Karty Gracza : ")
        print(self.__card_to_string(self.player_cards))
        print("")
        if(self.second_player_cards != [] ):
            print("Karty Gracza 2 : ")
            print(self.__card_to_string(self.second_player_cards))
            print("")

        print(" Twój ruch to : ( podaj nazwę lub numer )")
        #print(" 1: 'Dobranie karty'")
        #print(" 2: 'Niedopieranie karty' ")
        #if(len(self.player_cards)==2):
        #    print(" 3: 'Podwojenie stawki'")
        #if(self.player_cards[0](1) == self.player_cards[0](1) and self.second_player_cards == [] ):
        #    print(" 4: 'Podwojenie stawki'")
#
        ##Poniższe kod sprawdza czy krupier ma odsłoniętego asa
        #is_As = False
        #if(self.casino_cards[0](1) == "As" and self.casino_cards[0](0) >= 100):
        #    is_As = True
        #elif(self.casino_cards[1](1) and self.casino_cards[1](0) >= 100):
        #    is_As = True
        #if(is_As):
        #    print(" 5: 'Ubezpieczenie'")
        move_list = self.__gambit()
        if(1 in move_list):
            print(" 1: 'Dobranie karty'")
        if(2 in move_list):
            print(" 2: 'Niedopieranie karty' ")
        if(3 in move_list):
            print(" 3: 'Podwoić karty'")
        if(4 in move_list):
           print(" 4: 'Rozdwoić karty'")
        if(5 in move_list):
            print(" 5: 'Ubezpieczenie'")




        if(error_communicat):
            print(" Podano błędny komunikat wejściowy ! ")



