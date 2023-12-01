from time import sleep

def very_long_function():
    print("Be patient, this will take some time...")
    sleep(3)
    a = []
    for i in range(10000000):
        a.append(i*i)

very_long_function()

# Tutorial - Steps to Follow
# ------------------------------------------
# python -m cProfile .\demo.py
# pip install snakeviz
# python -m cProfile -o demo.prof .\demo.py
# snakeviz .\demo.prof