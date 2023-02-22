from sys import argv
import interactive
import file_format

if len(argv) < 2:
    interactive.main()
else:
    file_format.main(argv[1])
    