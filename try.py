import easygui as eg

eg.msgbox('selamat datang di program program Enkripsi dan dekripsi',
            'program Enkripsi dan dekripsi')
# Input Bilangan Prima
eg.msgbox("MASUKKAN NILAI 'p' DAN 'q':")
p = eg.integerbox(msg='masukkan nilai p',
                    title='masukkan nilai p', lowerbound=2, upperbound=99999)
q = eg.integerbox(msg='masukkan nilai p',
                    title='masukkan nilai p', lowerbound=2, upperbound=99999)

# Cek input apakah prima
def cek_prima(a):
    if (a == 2):
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if not (a % i):
                return False
    return True


cek_p = cek_prima(p)
cek_q = cek_prima(q)
while (((cek_p == False) or (cek_q == False))):
    p = eg.integerbox(msg='masukkan nilai p',
                    title='masukkan nilai p', lowerbound=0, upperbound=1000)
    q = eg.integerbox(msg='masukkan nilai q',
                    title='masukkan nilai q', lowerbound=0, upperbound=1000)
    cek_p = cek_prima(p)
    cek_q = cek_prima(q)

# Modulus RSA
n = p * q
# Eulers Toitent
r = (p-1)*(q-1)

def egcd(e, r):
    while (r != 0):
        e, r = r, e % r
    return e

# Algoritma Euclid
def eugcd(e, r):
    for i in range(1, r):
        while (e != 0):
            a, b = r//e, r % e
            r = e
            e = b

# Algoritma Euclidean (Diperpanjang)
def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        return (gcd, t, s)

# Perkalian Invers
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    return s % r

# Perhitungan Nilai e
for i in range(1, 1000):
    if (egcd(i, r) == 1):
        e = i

# Nilai d, Kunci Private dan Public
eugcd(e, r)
d = mult_inv(e, r)
public = (e, n)
private = (d, n)

# Enkripsi
def enkripsi(pub_key, n_teks):
    e, n = pub_key
    x = []
    m = 0
    for i in n_teks:
        if (i.isupper()):
            m = ord(i)-60
            c = (m**e) % n
            x.append(c)
        elif (i.islower()):
            m = ord(i)-92
            c = (m**e) % n
            x.append(c)
        elif (i.isspace()):
            spc = 400
            x.append(400)
    return x

# Dekripsi
def dekripsi(priv_key, c_teks):
    d, n = priv_key
    txt = c_teks.split(',')
    x = ''
    m = 0
    for i in txt:
        if (i == '400'):
            x += ' '
        else:
            m = (int(i)**d) % n
            m += 60
            c = chr(m)
            x += c
    return x.lower()


# Pesan
pesan = eg.enterbox(msg="masukkan pesan (pisahkan angka dengan ',' untuk enkripsi): ", title="masukkan pesan yang akan di proses")
eg.msgbox(f"Pesan anda: {pesan}")
# Pilih Fungsi Enkripsi atau Dekripsi and Print
pilih = eg.choicebox(msg="Ketik '1' untuk enkripsi and '2' untuk dekripsi: ", choices=['1', '2'], title='Pilih Perintah')
if (pilih == '1'):
    pesan_enk = enkripsi(public, pesan)
    eg.msgbox(f"Pesan enkripsimu:{pesan_enk}", "hasil enkripsi")
elif (pilih == '2'):
    eg.msgbox(f"Pesan dekripsimu: {dekripsi(private, pesan),}", "hasil dekripsi")
    
eg.msgbox("Terima kasih telah menggunakan program ini", "Terima kasih")
