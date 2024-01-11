enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


def encrypt(text):
    text = str(text.lower())
    pigpen_text = ""
    # key_for_enc = (key // (key * 8))**2 
    for i in text:
        if i in dec:
            pigpen_text += enc[dec.index(i)]
        else:
            pigpen_text += i
    return pigpen_text


def decrypt(pigpen_text):
    pigpen_text = str(pigpen_text.lower())
    text = ""
    # key_for_enc = (key // (key * 8))**2 
    for i in pigpen_text:
        if i in enc:
            text += dec[enc.index(i)]
        else:
            text += i
    return text
