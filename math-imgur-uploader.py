import tempfile
import os

testVar = input("Enter your equation (dont include \[ \]).\n")
preamble = "\\documentclass[convert={density=300,size=1080x800,outext=.png}]{standalone}\n\\usepackage{amsmath} \n\\usepackage{varwidth} \n \\begin{document}\n\\begin{varwidth}{\\linewidth}\\["
# preamble = "\\documentclass{standalone} \n\\usepackage{amsmath} \n\\begin{document}\n\["
finish = "\\]\n\\end{varwidth}\n\\end{document}"
print(preamble,testVar,finish)

# tmpdir = tempfile.TemporaryDirectory()
tmpdir = tempfile.mkdtemp()

# texfile = os.path.join(tmpdir.name,"texfile.tex")
# pdffile = os.path.join(tmpdir.name , "texfile.pdf")
# imgfile = os.path.join(tmpdir.name , "out.png")
texfile = os.path.join(tmpdir,"texfile.tex")
pdffile = os.path.join(tmpdir , "texfile.pdf")
imgfile = os.path.join(tmpdir , "out.png")

texfilewrite = open(texfile,"w")
texfilewrite.writelines([preamble,testVar,finish])
texfilewrite.seek(0)
texfilewrite.close()
# print(texfile.name)

os.system("pdflatex "+texfile)
# os.system("mv texfile.pdf " + tmpdir.name)
os.system("mv texfile.pdf " + tmpdir)
os.system("convert -density 300 " + pdffile + " -quality 90 " + imgfile)
# print(imgfile)


client_id = os.environ.get('IMGUR_API_ID')
client_secret = os.environ.get('IMGUR_API_SECRET')

from imgurpython import ImgurClient
if client_id is None or client_secret is None:
    print("could not be uploaded - no client_id")
else:
    client = ImgurClient(client_id, client_secret) 

    response = client.upload_from_path(imgfile)
    print("Formula uploaded to " + response['link'])
