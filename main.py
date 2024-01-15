enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


def encrypt(pigpen_text, key):
    pigpen_text = str(pigpen_text.lower())
    text = ""
    for i in pigpen_text:
        if i in enc:
            index = (enc.index(i) - key) % len(enc)
            text += dec[index]
        else:
            text += i
    return text


def decrypt(text, key):
    text = str(text.lower())
    pigpen_text = ""
    for i in text:
        if i in dec:
            index = (dec.index(i) + key) % len(dec)
            pigpen_text += enc[index]
        else:
            pigpen_text += i
    return pigpen_text
