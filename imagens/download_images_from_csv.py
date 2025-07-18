import csv
import os
import requests

def download_image(url, save_folder,filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # status!= 200
    except requests.RequestException as e:
        print(f"Falha ao fazer download {url}: {e}")
        return False

    save_path = os.path.join(save_folder, filename)

    with open(save_path, 'wb') as f:
        f.write(response.content)

    print(f"Baixado {url} para {save_path}")
    return True

def download_images_from_csv(csv_file_path, save_folder, url_column_index=0):
   
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader, start=0):
            if len(row) <= url_column_index:
                print(f"Pulando linha {i}: url não encontrada na coluna {url_column_index}")
                continue

            url = row[url_column_index].strip()
            if not url:
                print(f"Pulando linha {i}: sem URL")
                continue

            download_image(url, save_folder,f"image_{i}.jpg")

download_images_from_csv("jaguatirica.csv", "jaguatirica2")
