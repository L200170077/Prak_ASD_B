class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimat ini mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
#No.1 A
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False
        
#No.1 B
    def hitungKonsonan(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() not in vowel :
                jml+=1
        return jml
    
#No.1 C
    def hitungVokal(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() in vowel :
                jml+=1
        return jml
