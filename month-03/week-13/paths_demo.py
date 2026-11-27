from pathlib import Path

folder = Path('data/raw/lga_facilities')

print( 'Folder exists:', folder.exists() )

for path in sorted(folder.glob('*.csv')):
    print(path.name, "| stem:",path.stem, "| suffix:",path.suffix)
Output = Path('data/processed')/"lga_points"
Output.mkdir(parents=True ,exist_ok=True)
print('Output folder exists:', Output)