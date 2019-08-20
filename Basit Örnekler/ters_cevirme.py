while True:
    print(
"""
(Programdan çıkmak için q tuşuna basın)
""")
    ters = input("Ters Çevirmek istediğini bir şeyler yazın: ")

   
   
    if ters == "q":
        print("Programdan çıkılıyor")
        break
    
    
    elif ters == "":
        print("Lütfen ters çevirmek istediğiniz bir şeyler yazın! \n\n ")
        break
        
   
   
    elif not ters:
        print("Boş karakter girilemez")
        continue
        
        
 
    d = ters[::]
    print("\nOrjinal hali -> ",d)
    

    t = ters[::-1]
    print("Ters Çevrilmiş Hali -> ",t, "\n\n")
