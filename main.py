enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


key = int(input())


def encrypt(text):
    text = text.lower()
    text = ""
    key_for_enc = (key // (key * 8))**2 
    for i in text:
        if (ord(i) - key_for_enc < 98):
            text += chr(ord(i) - key_for_enc + key)
        else:
            text += chr(ord(text) - key_for_enc)
    return text


def decrypt():
    pass
