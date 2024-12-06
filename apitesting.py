# Anand Basu and Maddy Fung
# Project Phase 5

from phase5 import EverythingFantasyAPI

def main():
    bf_api = EverythingFantasyAPI()

    # run query 1 a few times
    print()
    result = bf_api.run_q1(5)
    for row in result:
        print('pname: ' + str(row[0]))

    print()
    result = bf_api.run_q1(9)
    for row in result:
        print('pname: ' + str(row[0]))

    # run query 2 a few times
    print()
    result = bf_api.run_q2(7)
    for row in result:
        print('uName: ' + str(row[0]))

    print()
    result = bf_api.run_q2(9)
    for row in result:
        print('uName: ' + str(row[0]))


    # run query 3 a few times
    print()
    result = bf_api.run_q3(8)
    for row in result:
        print(f'pname: {row[0]}, strength: {row[1]}')


    # run query 4 a few times
    print()
    result = bf_api.run_q4('Barack Obama')
    print('Barack Obama matches: ' + str(result))
    
    print()
    result = bf_api.run_q4('Lime')
    print('Lime matches: ' + str(result))

    

    # run query 5 a few times
    print()
    result = bf_api.run_q5(7)
    print('Users with avg intelligence > 7: ')
    for row in result:
        print('uName: ' + str(row[0]) + ', with average intelligence ' + str(row[1]))

    print()
    result = bf_api.run_q5(9)
    print('Users with avg intelligence > 9: ')
    for row in result:
        print('uName: ' + str(row[0]) + ', with average intelligence ' + str(row[1]))

    #query 6
    result = bf_api.run_q6()
    for user in result:
        print('uName: ' + str(user[0]))

    bf_api.close()



# Tell the Python interpreter to begin execution at the main function
if __name__ == '__main__':
    main()