# I want to find the position of ":" and then print the number behind it converted to float

text = "X-DSPAM-Confidence:    0.8475"
print text
pos=text.find(":")
print pos
print float(text[pos+1: ]) # I put pos+1 here, not to involve ":" in the conversion, otherwise it wouldn't be possible