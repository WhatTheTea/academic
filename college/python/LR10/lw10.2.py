string = """The Web Hypertext Application Technology Working Group
(WHATWG) is a community of people interested in evolving
HTML and related technologies. The WHATWG was founded
by individuals from Apple Inc., the Mozilla Foundation and
Opera Software, leading Web browser vendors, in 2000."""

i = string.find("2")

res = string[0:i]
res += "2004."

print("was: \n" + string + '\n')
print("now: \n" + res)

spaces = string.count(" ")
print("Пробілів: ", spaces, "Символів: ", len(string) - spaces)