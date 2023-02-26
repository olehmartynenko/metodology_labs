from sys import argv
import interactive
import file_format

if len(argv) < 2:
    interactive.main()
elif len(argv) == 2:
    file_format.main(argv[1])
else: 
    print('You can pass only 0 or 1 paths of files')