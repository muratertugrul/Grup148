import pandas as pd
from langchain_community.llms import Ollama  # ✅ BU DOĞRU
import json
import random
import re


RANDOM_SAMPLE = 10
TOTAL_ROWS = 1615940

llm = Ollama(
    model="llama3:instruct",
    temperature=0,    
    num_ctx=512,
    top_k=10
)

def clean_json_response(response):
    try:
        json_str = re.search(r'\{.*\}', response, re.DOTALL).group()
        json_str = json_str.replace("'", '"')
        json_str = re.sub(r'[\n\t]', ' ', json_str)
        return json.loads(json_str)
    except Exception:
        return {"Technologies": [], "Summary": ""}

def analiz_et(metin, job_title):
    prompt = f"""
AŞAĞIDAKİ KURALLARA KESİNLİKLE UY:
1. SADECE aşağıdaki JSON formatında cevap ver
2. EKSTRA AÇIKLAMA YAZMA
3. "Technologies" = teknik + soft beceriler
4. "Summary" = 10 kelimeyi geçmesin

{{
  "Technologies": ["Python", "FastAPI", "Liderlik"],
  "Summary": "Python ile veri işleme ve ekip yönetimi"
}}

İŞ METNİ:
Job Title: {job_title}
Skills: {metin[:300]}
"""
    try:
        response = llm.invoke(prompt)
        print(f"\n[DEBUG] Yanıt:\n{response}\n")  
        parsed = clean_json_response(response)
        return {
            "Job Title": job_title,
            "Technologies": parsed.get("Technologies", []),
            "Summary": parsed.get("Summary", "")
        }
    except Exception as e:
        print(f"Hata: {str(e)}")
        return {
            "Job Title": job_title,
            "Technologies": [],
            "Summary": ""
        }

random_indices = random.sample(range(TOTAL_ROWS), RANDOM_SAMPLE)

results = []
with pd.read_csv("deneme.csv", chunksize=1000) as reader:
    for chunk in reader:
        selected = chunk[chunk.index.isin(random_indices)]
        if not selected.empty:
            for _, row in selected.iterrows():
                skills_text = str(row.get("skills", ""))
                job_title = str(row.get("Job Title", ""))[:100]

                if len(skills_text.strip()) < 5:
                    continue

                sonuc = analiz_et(skills_text, job_title)
                results.append({
                    "Job Title": sonuc["Job Title"],
                    "Technologies": ", ".join(sonuc["Technologies"]),
                    "Summary": sonuc["Summary"]
                })

                print(f"İşlenen: {len(results)}/{RANDOM_SAMPLE}", end='\r')

        if len(results) >= RANDOM_SAMPLE:
            break

output_df = pd.DataFrame(results)
output_df.to_csv("final_output.csv", index=False)

print("\n✅ İşlem tamamlandı! Kaydedilen veriler:")
print(output_df.head())
