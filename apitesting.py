# Anand Basu and Maddy Fung
# Project Phase 5

from phase5 import EverythingFantasyAPI

def main():
    bf_api = EverythingFantasyAPI()

    # run query 1 a few times
    print()
    result = bf_api.run_q1("strength", 5)
    for row in result:
        print('pname: ' + str(row[0]))


    # run query 2 a few times
    print()
    result = bf_api.run_q2(7)
    for row in result:
        print('uName: ' + str(row[0]))



    print()
    bf_api.close()


# Tell the Python interpreter to begin execution at the main function
if __name__ == '__main__':
    main()