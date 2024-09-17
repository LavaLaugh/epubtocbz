import glob
import os
import shutil
import sys

choice = input("Choose 1 for AVIF\nChoose 2 for WEBP")

if choice == "1":
    format = "avif"
    quality = "48"

elif choice == "2":
    format = "webp"
    quality = "55"

else:
    print("Wrong input, use any key to exit...")
    sys.exit(0)


print("INFO: Getting all EPUB files...")
path = glob.glob("*.epub")
path.sort()

print("INFO: Creating output folder...")
if not os.path.exists("output"):
    os.makedirs("output")

index = 1
for file in path:
    folder = file.replace(".epub", "")

    print("INFO: Converting EPUB " + folder + " to zip...")
    os.system("ebook-convert " + file + " " + folder + ".zip")

    zip = folder + ".zip"

    print("INFO: Converting ZIP " + folder + " to CBZ...")
    os.system("cbconvert convert --format " + format + " --quality " + quality + " --no-nonimage=true --outdir output/ " + zip)

    index += 1
    os.remove(zip)
