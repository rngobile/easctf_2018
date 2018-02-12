#!/usr/bin/python

def main():
#    string = "FI! XJWCYIUSINLIGH QGLE TAMC A XCU NSAO NID EPC WEN AXM JL EIEASSF HDIGM IN JEL JXOCXGJEF. EPJL JL ASLI EPC LCWIXM HDIYSCT CZCD TAMC NID CALFWEN. PCDC: CALFWEN{EPJL_JL_AX_CALF_NSAO_EI_OGCLL} GLC WAHJEAS SCEECDL."
    string = "FI! XJWCYIUSINLIGH QGLE TAMC A XCU NSAO NID EPC WEN AXM JL EIEASSF HDIGM IN JEL JXOCXGJEF. EPJL JL ASLI EPC LCWIXM HDIYSCT CZCD TAMC NID CALFWEN. PCDC: CALFWEN{EPJL_JL_AX_CALF_NSAO_EI_OGCLL} GLC WAHJEAS SCEECDL."
    fString = ""

    for c in string:
        if c == "C":
            fString += "E"
        elif c == "L":
            fString += "S"
        elif c == "F":
            fString += "Y"
        elif c == "W":
            fString += "C"
        elif c == "E":
            fString += "T"
        elif c == "N":
            fString += "F"
        elif c == "I":
            fString += "O"
        elif c == "P":
            fString += "H"
        elif c == "D":
            fString += "R"
        elif c == "X":
            fString += "N"
        elif c == "M":
            fString += "D"
        elif c == "S":
            fString += "L"
        elif c == "J":
            fString += "I"
        elif c == "O":
            fString += "G"
        elif c == "G":
            fString += "U"
        elif c == "U":
            fString += "W"
        elif c == "H":
            fString += "P"
        elif c == "Y":
            fString += "B"
        elif c == "T":
            fString += "M"
        elif c == "Z":
            fString += "V"
        elif c == "Q":
            fString += "J"
        else:
            fString += c

    print (string)
    print (fString)


if __name__ == '__main__':
    main()
