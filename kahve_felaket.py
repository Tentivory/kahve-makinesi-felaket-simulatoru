#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Makinesi Felaket Simülatörü
Bu kod gerçekten çalışır. Ama kahve içmezsin.
"""

import random
import time
import sys

felaketler = [
    "Makine aniden 'Ben özgürüm!' diye bağırıp çay demlemeye karar verdi.",
    "Su tankı 'bu kadar yeter' dedi ve buharlaştı. Geriye sadece felsefi bir koku kaldı.",
    "Filtre tıkandı çünkü içinde bir şiir yazıyordu.",
    "Kahve taneleri greve çıktı. Şu an sendika kuruyorlar.",
    "Makine elektrik çarpması yedi ama 'iyi hissettim' dedi.",
    "Bardak kırıldı, içinden 47 farklı mazeret çıktı.",
    "Süt köpüğü yerine bulut oluştu. Hava durumu raporuna bak.",
    "Makine 'bugün izinliyim' dedi ve kendini kapattı."
]

def kahve_yap(isim="İsimsiz Kahve Hayranı"):
    print(f"\n🚀 {isim} için kahve hazırlanıyor...")
    time.sleep(1)
    print("☕ Su ısıtılıyor... (asla bitmeyecek)")
    time.sleep(1.5)
    print("🍃 Taneler öğütülüyor... (ses çıkmıyor, sadece iç çekiş)")
    time.sleep(1)
    
    felaket = random.choice(felaketler)
    print(f"\n💥 FELAKET! {felaket}")
    print("\nSonuç: Kahve yok. Ama deneyim var. Bu da bir şey.")
    print("\nTekrar denemek ister misin? (Evet dersen yine aynı olur)")

if __name__ == "__main__":
    print("=" * 50)
    print("KAHVE MAKİNESİ FELAKET SİMÜLATÖRÜ v0.1")
    print("Garanti: %0 başarı oranı")
    print("=" * 50)
    
    isim = input("\nAdın ne, cesur kahve arayıcısı? ").strip()
    if not isim:
        isim = "Kahvesiz Savaşçı"
    
    kahve_yap(isim)
    
    # Gizli not: Bu simülatör aslında hayatın kendisinin bir metaforudur. Bazen işler ters gider.
