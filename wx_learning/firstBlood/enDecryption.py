import base64 as bs
import re

class enDecryption():

    def encryption(self,str):
        STR="^[a-zA-Z]{1}[a-zA-Z0-9]{4,8}$"
        r = re.compile(STR)
        if r.match(str):
            levelOne = bs.encodestring(str)
            final = self.__alcohol(levelOne)
            return final
        else :
            pass

    def decryption(self,str):
        if str :
            levelOne = self.__vinegar(str)
            final = bs.decodestring(levelOne)
            return final
        else :
            pass
    def __alcohol(self,str):
        return str[::-1]
    def __vinegar(self,str):
        return str[::-1]

if __name__ == "__main__":
    name = "banana"
    password = "pineApple"

    obj = enDecryption()
    print "-----------------------------------"
    print "original name : [ %s ]\n password : [ %s ]"%(name,password)
    print "-----------------------------------"
    nameAfter = obj.encryption(name)
    passwordAfter = obj.encryption(password)
    print "nameAfter : [ %s ]\n passwordAfter : [ %s ]"%(nameAfter.strip(),passwordAfter.strip())
    print "-----------------------------------"
    nameFinal = obj.decryption(nameAfter)
    passwordFinal = obj.decryption(passwordAfter)
    print "decoded name : %s\n decoded password : %s"%(nameFinal,passwordFinal)
    print "-----------------------------------"

