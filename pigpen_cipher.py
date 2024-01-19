dict = {'a': '⁅', 'ą': '⁆', 'b': '<', 'c': '>', 'ć': '⌈', 'd': '⌉', 'e': '«', 'ę': '»', 'f': '⌊', 'g': '⌋', 'h': '⟨', 'i': '⟩', 'j': '⟦', 'k': '⟧', 'l': '⟪', 'ł': '⟫', 'm': '⟬', 'n': '⟭', 'o': '‡', 'ó': '¶', 'p': '⁋', 'q': '⁕', 'r': '‣', 's': '⁌', 'ś': '⁜', 't': '※', 'u': '♪', 'v': '✕', 'w': '⌀', 'x': '⏕', 'y': '⏔', 'z': '⁒', 'ź': '‽', 'ż': '⸘'}


def encrypt(text, key):
    text = text.lower()
    pigpen_text = ""
    for i in text:
        if i in dict:
            index = (list(dict.keys()).index(i) + key) % len(dict)
            pigpen_text += list(dict.values())[index]
        else:
            pigpen_text += i
    return pigpen_text


def decrypt(pigpen_text, key):
    pigpen_text = pigpen_text.lower()
    text = ""
    for i in pigpen_text:
        if i in dict.values():
            index = (list(dict.values()).index(i) - key) % len(dict)
            text += list(dict.keys())[index]
        else:
            text += i
    return text
