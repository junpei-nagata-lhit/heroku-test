import os

outdir = "output"
outfile = os.path.join(outdir, "test.txt")

if not os.path.isdir(outdir):
    os.makedirs(outdir, exist_ok=True)

with open(outfile, "w") as f:
    f.write("test...")

with open(outfile, "r") as f:
    print(outfile, "contains", f.read())
