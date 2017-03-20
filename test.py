from pyparsing import *

info = Word(alphas)
Infoline = Literal("#")+info
VoiceIdentifier = Word(alphas)|Literal("global")
PITCH= oneOf("A B C D E F G")
OCTAVE= oneOf("<< < 0 1 2 3 4 5 6 7 8 9 > >>")
liste=''
for i in range(1,128):
    liste = liste + ' %s'%(i)
MPN = oneOf("%s"%(liste))
SIGN = oneOf("+ -")
IPN = [SIGN] + PITCH + OCTAVE
EOS= IPN|MPN
SSIG= Literal("\$") + [EOS]
VoiceLine = Literal("O") + VoiceIdentifier + SSIG





assignmentTokens = VoiceLine.parseString("O  flute \$C6 # bar-based notation")
