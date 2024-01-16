import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import os

# Specifica il percorso alla directory contenente i file FITS
percorso_cartella = '/SunhalphaStageOATO/Ottimizzazione_parametri_camera/SET3/AS_P100'

# Trova tutti i file FITS nella directory
files_fits = [f for f in os.listdir(percorso_cartella) if f.endswith('.fit')]

# Definisci il numero di bin per l'istogramma
#num_bin =1000  # Puoi personalizzare questo valore

# Inizializza un contatore per numerare gli istogrammi
contatore = 1

# Per ogni immagine FITS, crea e salva un istogramma separato
for nome_immagine in files_fits:
    with fits.open(os.path.join(percorso_cartella, nome_immagine)) as hdul:
        data = hdul[0].data
        pixel_values = data.flatten()
        
# Calcola il numero di bin basato sull'intervallo dei valori dei pixel e la larghezza del bin desiderata
        valore_minimo = 0
        valore_massimo = 65000
        larghezza_bin_desiderata = 255  # Personalizza la larghezza del bin secondo le tue esigenze
        num_bin = int((valore_massimo - valore_minimo) / larghezza_bin_desiderata)
        print(pixel_values)
        print(valore_massimo)
        print(valore_minimo)
    
        # Calcola l'istogramma
        hist, bin_edges = np.histogram(pixel_values, bins=num_bin, range=(0, 65500))
        print(bin_edges)
        # Crea un nuovo grafico
        plt.bar(bin_edges[:-1], hist, width=larghezza_bin_desiderata)
        plt.xlabel('Valore del Pixel')
        plt.ylabel('Numero di Pixel')
        plt.title(f'Istogramma {contatore}')
        plt.ylim(0, 10**6)
        plt.yscale('log')
        # Salva l'istogramma come immagine separata (opzionale)
        nome_istogramma = f'istogramma_{contatore}.png'
        plt.savefig(nome_istogramma)
        
        # Mostra l'istogramma
        plt.show()
        
        # Incrementa il contatore
        contatore += 1
