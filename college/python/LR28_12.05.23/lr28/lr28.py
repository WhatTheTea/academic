from dataclasses import dataclass
import easygui as eg

@dataclass
class Sport:
    name : str
    origin : str
    isOlympic : bool
    imgPath : str

class App:
    _sportAttrs = [*Sport.__annotations__.keys()]
    INFO_CHOICES = "Країна походження", "Олімпійський?"
    choiceToAttr = {
        INFO_CHOICES[0] : _sportAttrs[1], # Країна походження : origin
        INFO_CHOICES[1] : _sportAttrs[2]
    }
    sports = [Sport('Бадмінтон', "Італія", True, 'badm.jpg'), 
              Sport('Баскетбол', "США", True, 'bskt.jpg')]
    chosenSport : Sport = None
    
    def __init__(self) -> None:
        self.chooseSport()
        self.chooseInfo()
    
    def chooseSport(self) -> None:
        choice = eg.choicebox('Оберіть вид спорту:', 'Літні спортивні ігри', map(lambda x: x.name, self.sports))
        self.chosenSport = [*filter(lambda x : x.name == choice, self.sports)][0]

    def chooseInfo(self) -> None:
        choice = eg.buttonbox(image=self.chosenSport.imgPath, 
                              choices=self.INFO_CHOICES
                              )
        selection = self.selectInfo(choice)
        eg.msgbox(self.chosenSport.__dict__[selection[1]], selection[0])
        self.__init__()

    def selectInfo(self, choice : str) -> tuple:
        if not '.' in choice:
            return choice, self.choiceToAttr[choice]
        else:
            return 'Назва', self._sportAttrs[0]

app = App()