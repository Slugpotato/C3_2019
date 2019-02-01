
import sys
#
#
#
#
#
#

sequence_1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
sequence_2 = [(), (), (), (), (), ()]
sequence_3 = [(), (), (), (), (), ()]
sequence_4 = [(), (), (), (), (), ()]

lst_of_sequences = [sequence_1, sequence_2, sequence_3, sequence_4]

def main(argv=None):
    if argv is None:
        argv = sys.argv

    # Keep on infinite loop
    while True:

        # Try/except looking for sequence number
        try:
            path = input("Enter sequence number (1-4): \n")

            if path == 'exit':
                break

            sequence_num = int(path)

            # Make sure input is in range of acceptable numbers
            if sequence_num in [1, 2, 3, 4]:
                sequence_num = sequence_num - 1

                status = check_sequence(lst_of_sequences[sequence_num])

                if status == 'exit':
                    break

        except (ValueError, IndexError):
            pass




# Given a sequence, check that the input is entered in right sequence
def check_sequence(sequence):

    i = 0

    # Make sure the entire sequence has been iterated through
    while i != len(sequence):

        given_x = 0
        given_y = 0

        was_correct_format = False

        # Loop until coordinate is entered in the correct format
        while was_correct_format is False:
            given_coors = input("Please enter the robot's current coordinates in the following format: x,y \n")

            if given_coors == 'exit':
                return 'exit'

            if given_coors == 'back':
                return 'back'

            print('Entered: ', given_coors)

            # Try to assign the x and y coordinates from input
            try:
                given_x = int(given_coors.split(',')[0])
                given_y = int(given_coors.split(',')[1])
                was_correct_format = True

            except (ValueError, IndexError):
                was_correct_format = False
                print('Incorrect format. \n')

        # Get current sequence entry
        entry = sequence[i]

        # If both match the current entry in the sequence, iterate i and print success status
        if entry[0] == given_x and entry[1] == given_y:
            print("Correct!")
            i = i + 1
            print("Try for the next one now! \n")

        else:
            print("Incorrect!")
            # i = 0

    print("Finished sequence!! \n")

    return "Success"






if __name__ == '__main__':
    main()



