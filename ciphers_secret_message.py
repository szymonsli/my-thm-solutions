cipher = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"


def decipher(cipher):
  return "".join(
    chr((base := ord('A') if c.isupper() else ord('a')) + (ord(c) - base - i) % 26)
    if c.isalpha() else c
    for i, c in enumerate(cipher)
  )

print("THM{" + decipher(cipher) + "}")
