string = 'X-DSPAM-Confidence:0.8475'
i = string.find(":")
res = string[i+1:]
print(float(res))