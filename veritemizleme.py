import re
import json

def temizle(metin):
   
    metin = re.sub(r'<.*?>', '', metin)  
    metin = re.sub(r'http\S+|www\S+', '', metin)
    metin = re.sub(r'[^\w\sğüşıöçĞÜŞİÖÇ]', '', metin)  
    metin = re.sub(r'\s+', ' ', metin)  
    return metin.strip().lower()  

def veritabanindan_veri_al(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        return json.load(f)

def temizlenmis_sohbetleri_isle(veritabani_verisi):
    
    temiz_veri = []
    rol_esleme = {'user': 'user', 'ai': 'assistant'}  
    
    for mesaj in sorted(veritabani_verisi, key=lambda x: x['timestamp']): 
        temiz_icerik = temizle(mesaj['content'])
        rol = rol_esleme.get(mesaj['message_type'], 'user')  
        temiz_veri.append({'role': rol, 'content': temiz_icerik})
    
    return temiz_veri


veritabani_verisi = veritabanindan_veri_al('/kaggle/input/project-data-json/project_data.json')  
temizlenmis_veri = temizlenmis_sohbetleri_isle(veritabani_verisi)


print("Örnek Temizlenmiş Veri:")
for msg in temizlenmis_veri[:3]:
    print(f"{msg['role']}: {msg['content']}")