import datetime as dt
from collections import namedtuple

Person = namedtuple("Person", "ПІБ Дата_народження")

people = [
    Person("CІЛ", dt.date(2005,5,25)),
    Person("CRE", dt.date(2004,3,5)),
    Person("CKE", dt.date(2006,6,11)),
    Person("CGT", dt.date(2012,3,16)),
    Person("CVF", dt.date(2001,2,22)),
    Person("CAD", dt.date(2003,3,16)),
    Person("CDF", dt.date(2005,1,16)),
    Person("CHF", dt.date(2006,3,21)),
    Person("CQW", dt.date(2005,6,16)),
    Person("CTE", dt.date(2003,8,16)),
    Person("HFD", dt.date(2005,3,20))
]

def checkBD(var : dt.date) -> bool:
    today = dt.date.today()
    return var.day == today.day and var.month == today.month

birthday = [print("З днем народження, ", p.ПІБ) for p in people if checkBD(p.Дата_народження)]
