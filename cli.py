import os, re
from optparse import OptionParser

s = r'JText::_\((\'|"){1}(.*?)(\'|"){1}\)'

def read_dir(option):
    patterns = []
    for folder, dirs, files in os.walk(option.path, topdown=False):
        with open(os.path.join(folder, '*.php'), 'rb') as dest:
            for filename in files:
                with open(os.path.join(folder, filename), 'r') as src:
                    for l in src.readlines():
                        try:
                            pattern = re.search(s, l).group(2)
                            if option.name.upper() in pattern:
                                patterns.append(pattern)
                        except:
                            continue

    file_name = os.path.join(option.out, '%s.%s.ini' % (option.lang, option.name.lower()))
    with open(file_name, 'w') as f:
        for p in patterns:
            f.write('%s=""\n' % p)
    f.close()



def main():
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="path", help="directory to search in")
    parser.add_option("-d", "--destination", dest="out", default='.', help="destination for the ini file")
    parser.add_option("-c", "--component", dest="name", help="the name of the component")
    parser.add_option("-l", "--language", dest="lang", default="en-GB", help="language localisation. default is en-GB")

    (option, args) = parser.parse_args()
    # if len(args) != 1:
    #     parser.error("incorrect number of arguments. use cli.py -h for more information")
    read_dir(option)


if __name__ == "__main__":
    main()
