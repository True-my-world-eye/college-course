import os
import zipfile

class ZipTest:
    def make_txt(self,fname):
        with open(fname,"w") as f:
            f.write("hello world")
    
    def zip_and_remove(self,fname):
        zname = fname + ".zip"
        with zipfile.ZipFile(zname,"w",zipfile.ZIP_DEFLATED) as zf:
            zf.write(fname)
        os.remove(fname)
    
    def unzip_and_print(self,zname):
        with zipfile.ZipFile(zname, "r") as zf:
            zf.extractall()
            for f in zf.namelist():
                if f.endswith(".txt"):
                    with open(f, encoding="utf-8") as fobj:
                        print(fobj.read())


if __name__ == "__main__":
    zt = ZipTest()
    zt.make_txt("t.txt")
    zt.zip_and_remove("t.txt")
    zt.unzip_and_print("t.txt.zip")