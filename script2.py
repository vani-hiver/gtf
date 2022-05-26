def decryption(txt, key = 3):
    dec_text = ""
    try: 
        for index in range(len(txt)):
            if txt[index].isAlpha():
                if txt[index].isUpper():
                    temp = (ord(txt[index]) - ord('A') - key)
                    if temp < 0: temp += 26
                    temp += ord('A')
                    dec_text += chr(temp)

                elif txt[index].isLower():
                    temp = (ord(txt[index]) - ord('a') - key)
                    if temp < 0: temp += 26
                    temp += ord('a')
                    dec_text += chr(temp)
            else:
                dec_text += txt[index]
    except:
        return "WUHU! DEBUG AGAIN!!!"
    return dec_text
    
print(decryption(".bwoa"))