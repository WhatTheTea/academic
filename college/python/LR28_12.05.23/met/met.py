from dataclasses import dataclass
import easygui as eg

@dataclass
class Country:
    name : str
    capital : str
    currency : str
    imgPath : str

countries = {'Україна' : Country('Україна', 'Київ', "Гривня", "ukr.png"),
             'Хорватія' : Country('Хорватія', 'Загреб', "Євро", 'cro.png'), 
            }#'Чехія', 'Фінляндія'
choice = eg.choicebox('Оберіть країну:', 'Довідник країн', map(lambda x: x.name, countries.values()))
chosen = countries[choice]

infoCs = ["Столиця", "Валюта"]
infoToAttr = {infoCs[0] : 'capital',
              infoCs[1] : 'currency'
}
countryInfo = eg.buttonbox(image=chosen.imgPath, 
                           choices=infoCs,
                           title=chosen.name
                           )

eg.msgbox(chosen.__dict__[infoToAttr[countryInfo]],countryInfo)