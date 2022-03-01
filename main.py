Elder_Futhark = (
    "ᚠ", "ᚢ", "ᚦ", "ᚨ", "ᚱ", "ᚲ", "ᚷ", "ᚹ", "ᚺ", "ᚾ", "ᛁ", "ᛃ", "ᛈ", "ᛇ", "ᛉ", "ᛊ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛜ", "ᛞ",
    "ᛟ")
Elder_Futhark_Latin = (
    "f", "u", "þ", "a", "r", "k", "g", "w", "h", "n", "i", "j", "p", "ï", "z", "s", "t", "b", "e", "m", "l", "ŋ", "d",
    "o")
Anglo_Saxon = (
    "ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᚴ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ",
    "ᛟ",
    "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ")
Anglo_Saxon_Latin = (
    "f", "u", "þ", "o", "r", "c", "g", "w", "h", "n", "i", "j", "ï", "p", "x", "s", "s", "t", "b", "e", "m", "l", "ŋ",
    "œ",
    "d", "a", "æ", "y", "j", "ea")
Younger_Futhark = (
    "ᚠ", "ᚢ", "ᚦ", "ᚬ", "ᚱ", "ᚴ", "ᚼ", "ᚾ", "ᛁ", "ᛅ", "ᛋ", "ᛏ", "ᛒ", "ᛘ", "ᛚ", "ᛦ", "ᚭ", "ᚽ", "ᚿ", "ᛆ", "ᛌ", "ᛐ", "ᛓ",
    "ᛙ", "ᛧ")
Younger_Futhark_Latin = (
    "f", "u", "þ", "ą", "r", "k", "h", "n", "i", "a", "s", "t", "b", "m", "l", "ʀ", "ą", "h", "n", "a", "s", "t", "b",
    "m", "ʀ")
Medieval = (
    "ᛆ", "ᛒ", "ᛍ", "ᛑ", "ᚧ", "ᛂ", "ᚠ", "ᚵ", "ᚼ", "ᛁ", "ᚴ", "ᛚ", "ᛘ", "ᚿ", "ᚮ", "ᛔ", "ᛕ", "ᛩ", "ᚱ", "ᛌ", "ᛋ", "ᛐ", "ᚢ",
    "ᚡ",
    "ᚢ", "ᚥ", "ᛪ", "ᛦ", "ᚤ", "ᛨ", "ᛎ", "ᚦ", "ᛅ", "ᚯ")
Medieval_Latin = (
    "a", "b", "c", "d", "ð", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "p", "q", "r", "s", "s", "t", "u",
    "v",
    "u", "w", "x", "y", "y", "y", "z", "þ", "æ", "ø")
Extras = ("᛫", "᛬", "᛭", "ᛢ", "ᛛ", "ᛣ", "ᚶ")
Extras_Latin = (".", "[:]", "[.]", "q", "l", "k", "(ENG)")
transoutput = str()
To_Be_Translated = str(input("Input text for translation."))
for i in To_Be_Translated:
    if i in Elder_Futhark:
        transoutput += str(Elder_Futhark_Latin[Elder_Futhark.index(i)])
        continue
    if i in Anglo_Saxon:
        transoutput += str(Anglo_Saxon_Latin[Anglo_Saxon.index(i)])
        continue
    if i in Younger_Futhark:
        transoutput += str(Younger_Futhark_Latin[Younger_Futhark.index(i)])
        continue
    if i in Medieval:
        transoutput += str(Medieval_Latin[Medieval.index(i)])
        continue
    if i in Extras:
        transoutput += str(Extras_Latin[Extras.index(i)])
        continue
    else:
        transoutput += str(i)
        continue
print(transoutput)

