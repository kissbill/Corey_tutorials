#  mi van fent
pip list

# mibol van friss
pip list -o

# frissiteni 	
pip install  -U csomagneve

# projekt -> mi kell hozza
pip freeze

# export into a file
pip freeze > requirments.txt

# file=bol installalni ami kell a projektre
pip install -r requirments.txt

# frissiteni minden outdated package=et
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U 
# local a virt env-re , grep veszi a neveket, cut levagja ami a = jel utan van, xrargs ezt veszi inputnak es frissiti ,n1 egyesevel
pip freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U