from tkinter.ttk import Style

from HuffmanCoding import Huffman
import fileIO
import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import random


def rabinMiller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)  # a^d%n
    if x == 1 or x == n - 1:
        return True

    # square x
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    # is not prime
    return False


def isPrime(n):
    """
        return True if n prime
        fall back to rabinMiller if uncertain
    """

    # 0, 1, -ve numbers not prime
    if n < 2:
        return False

    # low prime numbers to save time
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                 991, 997]

    # if in lowPrimes
    if n in lowPrimes:
        return True

    # if low primes divide into n
    for prime in lowPrimes:
        if n % prime == 0:
            return False

    # find number c such that c * 2 ^ r = n - 1
    c = n - 1  # c even bc n not divisible by 2
    while c % 2 == 0:
        c /= 2  # make c odd

    # prove not prime 128 times
    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True


def generateKeys(keysize=1024):
    e = d = N = 0

    # get prime nums, p & q
    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    print(f"p: {p}")
    print(f"q: {q}")

    N = p * q  # RSA Modulus
    phiN = (p - 1) * (q - 1)  # totient

    # choose e
    # e is coprime with phiN & 1 < e <= phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break

    # choose d
    # d is mod inv of e with respect to phiN, e * d (mod phiN) = 1
    d = modularInv(e, phiN)

    return e, d, N


def generateLargePrime(keysize):
    """
        return random large prime number of keysize bits in size
    """

    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num


def isCoPrime(p, q):
    """
        return True if gcd(p, q) is 1
        relatively prime
    """

    return gcd(p, q) == 1


def gcd(p, q):
    """
        euclidean algorithm to find gcd of p and q
    """

    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0;
    old_s = 1
    t = 1;
    old_t = 0
    r = b;
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t


def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher


def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg



class EncryptionTool:
    """ """

class MainWindow:
    """ GUI Wrapper """


    def __init__(self, root):
        self.root = root
        self._cipher = None
        self._file_url = tk.StringVar()
        self._status = tk.StringVar()
        self._status.set("---")

        self.should_cancel = False

        root.title("TEAM DECEPTICONS")
        root.configure(bg="#eeeeee")
        root.minsize(250, 250)

        self.menu_bar = tk.Menu(
            root,
            bg="#eeeeee",
            relief=tk.FLAT
        )
        self.menu_bar.add_command(
            label="Topic!",
            command=self.show_topic_callback
        )
        self.menu_bar.add_command(
            label="Help!",
            command=self.show_help_callback
        )
        self.menu_bar.add_command(
            label="Quit!",
            command=root.quit
        )

        root.configure(
            menu=self.menu_bar
        )


        self.select_btn = tk.Button(
            root,
            text="SELECT FILE",
            command=self.selectfile_callback,
            width=42,
            bg="#1089ff",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.select_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S
        )


        self.encrypt_btn = tk.Button(
            root,
            text="ENCRYPT",
            command=self.encrypt_callback,
            bg="#00bd56",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.encrypt_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=7,
            column=0,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S
        )

        self.decrypt_btn = tk.Button(
            root,
            text="DECRYPT",
            command=self.decrypt_callback,
            bg="#ed3833",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.decrypt_btn.grid(
            padx=(6, 15),
            pady=8,
            ipadx=24,
            ipady=6,
            row=7,
            column=2,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S
        )

        self.compress_btn = tk.Button(
            root,
            text="COMPRESS",
            command=self.compress_callback,
            bg="#00bd56",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.compress_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=0,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S
        )

        self.decompress_btn = tk.Button(
            root,
            text="DECOMPRESS",
            command=self.decompress_callback,
            bg="#ed3833",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.decompress_btn.grid(
            padx=(6, 15),
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=2,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S
        )

        self.reset_btn = tk.Button(
            root,
            text="ABOUT US",
            command=self.reset_callback,
            bg="gray",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.reset_btn.grid(
            padx=15,
            pady=(4, 12),
            ipadx=24,
            ipady=6,
            row=9,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S
        )

        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg="#eeeeee",
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350
        )


        tk.Grid.columnconfigure(root, 0, weight=1)
        tk.Grid.columnconfigure(root, 1, weight=1)
        tk.Grid.columnconfigure(root, 2, weight=1)
        tk.Grid.columnconfigure(root, 3, weight=1)

    def selectfile_callback(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/",
                                             title="Select a Text File",
                                             filetypes=(("Text files",
                                                         "*.txt*"),
                                                        ("all files",
                                                         "*.*")))




    def encrypt_callback(self):
        print('hi')
        msg = open(filename, 'r').read()
        keysize = 32
        global e,d,N
        e, d, N = generateKeys(keysize)

        enc = encrypt(e, N, msg)
        file1 = open(filename, "w")
        file1.write(enc)
        file1.close()

        print(f"Message: {msg}")
        print(f"enc: {enc}")
        print(f"e: {e}")
        print(f"d: {d}")
        print(f"N: {N}")
        messagebox.showinfo("Encryption Successful !!!",
                            """The file has been successfully encrypted. """)
    def decrypt_callback(self):
        enc = open(filename, 'r').read()
        dec = decrypt(d, N, enc)
        file1 = open(filename, "w")
        file1.write(dec)
        file1.close()
        print(f"dec: {dec}")
        messagebox.showinfo("Decryption Successful !!!",
                            """The file has been successfully decrypted. """)
    def compress_callback(self):
        print('hi')
        files, original_size, huffman_file = fileIO.files_to_process(filename)
        huf=filename.replace("txt","huffman")
        print(files)
        print(original_size)
        print(huffman_file)
        huffman = Huffman(files, huf)
        exec_time = huffman.compress()
        output_size = fileIO.size(huf)
        compression_ratio = original_size / output_size
        space_saved = (1 - 1 / compression_ratio)
        messagebox.showinfo("Compression Successful !!!",
                            """The file has been successfully compressed. """)
        print("**************************************")
        print("* Compressing finished in %.2f seconds" % exec_time)
        print("* Compression Ratio %.2f" % compression_ratio)
        print("* Space Saved: {0:.2%}".format(space_saved))
        print("**************************************")
    def decompress_callback(self):

        files, original_size, huffman_file = fileIO.files_to_process(filename)
        huf = filename.replace("txt", "huffman")
        huffman = Huffman(files, huf)
        if fileIO.fileExtension(huf).lower() != "huffman":
            print("Invalid file format, *.huffman file needed")
            messagebox.showinfo("Invalid File Format !!!","""Please provide .huffman extension file. """)

            exit(1)

        exec_time = huffman.decompress()
        messagebox.showinfo("Decompression Successful !!!",
                            """The file has been successfully decompressed. """)

        print("****************************************")
        print("* Decompressing finished in %.2f seconds" % exec_time)
        print("****************************************")
    def reset_callback(self):
        messagebox.showinfo(
            "ABOUT US",
            """TEAM DECEPTICONS 
VISHAL.C (BL.EN.U4AIE19069)
Mandiga Sahasra Sai Tarun (BL.EN.U4AIE19039)
S Venkatasubramanian (BL.EN.U4AIE19055)"""
)

    def show_topic_callback(self):
        messagebox.showinfo(
            "TOPIC!",
            """ Huffman Compression and RSA Encryption """
        )


    def show_help_callback(self):
        messagebox.showinfo(
            "How To",
            """1. Open the App and Click SELECT FILE Button and select your file e.g. "abc.txt".
2. Click ENCRYPT Button to encrypt. 
3. Click DECRYPT Button to decrypt. 
3. Click COMPRESS Button to compress. 
3. Click DECOMPRESS Button to decompress (make sure you choose .huffman extension file). 
5. Click RESET Button to reset the input fields and status bar.
6. You can also Click CANCEL Button during Encryption/Decryption to stop the process."""
        )

if __name__ == "__main__":
    ROOT = tk.Tk()
    MAIN_WINDOW = MainWindow(ROOT)
    ROOT.mainloop()
