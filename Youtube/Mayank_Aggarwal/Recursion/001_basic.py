def HDSA(num):
    if num==0:
        return
    print("Hello", num)
    HDSA(num-1)

if __name__ == "__main__":
    HDSA(10)