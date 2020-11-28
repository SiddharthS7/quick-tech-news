from sites import (cnet, india_today, indian_express, live_mint, ndtv, zee)

print("\n☆☆☆☆☆💥 Welcome to news Bot 💥☆☆☆☆☆")
site = input("1.CNET\n2.India Today\n3.Indian Express\n4.Live Mint\n5.NDTV\n6.ZEE\n0.EXIT\nEnter your choice\n")

while site != 0:
    if (site == '1'):
        print('\nFetching news from CNET...\n')
        s = cnet.cnet()
    elif (site == '2'):
        print("\nFetcing news from India Today...\n")
        s = india_today.today()
    elif (site == '3'):
        print("\nFetching news from Indian Express...\n")
        s = indian_express.express()
    elif (site == '4'):
        print("\nFetching news from Live Mint...\n")
        s = live_mint.mint()
    elif (site == '5'):
        print("\nFetching news from NDTV...\n")
        s = ndtv.ndtv()
    elif (site == '6'):
        print("\nFetching news from ZEE...\n")
        s = zee.zee()
    elif (site == '0'):
        exit()
    else:
        print("\nWrong choice\n")

    print("☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆")
    print(s)
    print("☆☆☆☆☆💥 Welcome to news Bot 💥☆☆☆☆☆")
    
    site = input("\n1.CNET\n2.India Today\n3.Indian Express\n4.Live Mint\n5.NDTV\n6.ZEE\n0.EXIT\nEnter your choice\n")