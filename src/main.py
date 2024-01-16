enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


def encrypt(text, key):
    text = text.lower()
    pigpen_text = ""
    for i in text:
        if i in enc:
            index = (enc.index(i) + key) % len(enc)
            pigpen_text += dec[index]
        else:
            pigpen_text += i
    return pigpen_text


def decrypt(pigpen_text, key):
    pigpen_text = pigpen_text.lower()
    text = ""
    for i in pigpen_text:
        if i in dec:
            index = (dec.index(i) - key) % len(dec)
            text += enc[index]
        else:
            text += i
    return text
