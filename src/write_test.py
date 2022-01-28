import os

outdir = "output"
outfile = os.path.join(outdir, "test.txt")

if os.path.isdir(outdir):
    os.makedirs(outdir, exist_ok=True)

with open(outfile) as f:
    f.write("test...")
