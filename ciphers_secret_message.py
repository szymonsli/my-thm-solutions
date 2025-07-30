cipher = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"

def decipher(cipher):
  return "".join(
    [chr(a) for a in range(ord("A"), ord("z") + 1) if ((a - (base := ord('A') if c.isupper() else ord('a')) + i) % 26 == ord(c) - base) and c.isupper() == chr(a).isupper() and chr(a).isalpha()][0]
    if c.isalpha() else c
    for i, c in enumerate(cipher)
  )

print("THM{" + decipher(cipher) + "}")
