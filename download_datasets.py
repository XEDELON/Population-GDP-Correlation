import os
import subprocess
import pandas as pd

population_dataset = 'kaggleashwin/population-dataset'
gdp_dataset = 'gwenaelmouthuy/gdp-per-capita-between-1960-and-2021'

download_dir = '.'

def download_and_unzip(dataset_slug, target_dir):
    print(f"Downloading dataset: {dataset_slug} ...")
    subprocess.run([
        'kaggle', 'datasets', 'download',
        '-d', dataset_slug,
        '-p', target_dir,
        '--unzip'
    ], check=True)
    print(f"Downloaded and extracted {dataset_slug} to {target_dir}")

def main():
    download_and_unzip(population_dataset, download_dir)
    download_and_unzip(gdp_dataset, download_dir)

    print("Files in download directory:")
    files = os.listdir(download_dir)
    print(files)

    pop_files = [f for f in files if 'population' in f.lower() and f.endswith('.csv')]
    gdp_files = [f for f in files if 'gdp' in f.lower() and f.endswith('.csv')]

    print(f"Population files found: {pop_files}")
    print(f"GDP files found: {gdp_files}")

    if pop_files:
        pop_df = pd.read_csv(os.path.join(download_dir, pop_files[0]))
        print("\nPopulation dataset preview:")
        print(pop_df.head())
    else:
        print("Population CSV file not found!")

    if gdp_files:
        gdp_df = pd.read_csv(os.path.join(download_dir, gdp_files[0]))
        print("\nGDP dataset preview:")
        print(gdp_df.head())
    else:
        print("GDP CSV file not found!")

if __name__ == "__main__":
    main()
