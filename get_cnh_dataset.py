import os
from pdf2image import convert_from_path

### Download all parts

os.makedirs("CNH/Parts", exist_ok=True)

urls = [
    "https://ia601007.us.archive.org/1/items/3.yukonho/1.%20Calvin%20and%20Hobbes.pdf", 
    "https://ia801007.us.archive.org/1/items/3.yukonho/2.%20Something%20Under%20the%20Bed%20is%20Drooling.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/3.%20Yukon%20Ho!.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/4.%20Weirdos%20from%20Another%20Planet!.pdf",
    "https://ia601007.us.archive.org/1/items/3.yukonho/5.%20The%20Revenge%20of%20the%20Baby-sat.pdf",
    "https://ia601007.us.archive.org/1/items/3.yukonho/6.%20Scientific%20Progress%20Goes%20'Boink'.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/7.%20Attack%20of%20the%20Deranged%20Mutant%20Killer%20Monster%20Snow%20Goons.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/8.%20The%20Days%20Are%20Just%20Packed.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/9.%20Homicidal%20Psycho%20Jungle%20Cat.pdf",
    "https://ia601007.us.archive.org/1/items/3.yukonho/10.%20There's%20Treasure%20Everywhere.pdf",
    "https://ia801007.us.archive.org/1/items/3.yukonho/11.%20It's%20A%20Magical%20World.pdf",
]

# # URLLIB Approach (Faster than Requests)
# from urllib.request import urlretrieve

# for i, url in enumerate(urls):
#     dlloc = f"CNH/Parts/Part{i+1:02d}.pdf"
#     urlretrieve(url, dlloc)

# # Requests Approach (Slower than urllib)
# import requests

# for i, url in enumerate(urls):
#     dlloc = f"CNH/Parts/Part{i+1:02d}.pdf"
#     response = requests.get(url)
#     if response.ok and response.status_code==200:
#         with open(dlloc, 'wb') as f:
#             f.write(response.content)

### Extract all pages

def getfilename():
    count = 1
    while True:
        yield f'page{count:03d}.png'
        count += 1

folderbase = 'CNH'
partsbase = os.path.join(folderbase,'Parts')
itemlist = os.listdir(partsbase)

for item in itemlist:
    # comicfile = 'CNH/Parts/Part01.pdf'
    if item[-3:] != 'pdf':
        continue
    else:
        comicfile = os.path.join(partsbase, item) 

    partname = os.path.splitext(os.path.basename(comicfile))[0]
    dumploc = os.path.join(folderbase, partname)
    print(dumploc)
    os.makedirs(dumploc, exist_ok=True)

    # create a generator for naming files (some issue with this)
    filenamegen = getfilename()

    pages = convert_from_path(comicfile, 1000, fmt='png', output_folder=dumploc, output_file='page')
    
    # slow when saving page by page
    # for count, page in tqdm(enumerate(pages)):
    #     page.save(os.path.join(dumploc,f'page{count:03d}.png'), 'PNG')
    #     print(os.path.join(dumploc,f'page{count:03d}.png'))

### Make a list of pages that are only black and white