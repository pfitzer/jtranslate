import argparse
import fnmatch
import os
import re

class JTranslate(object):

    def __init__(self, args):
        """

        :param args:
        """
        self.args = args
        self.search_pattern = r'JText::_\((\'|"){1}(.*?)(\'|"){1}\)'

    def read_dir(self):
        """

        :return:
        """
        patterns = []
        for folder, dirs, files in os.walk(self.args.path, topdown=False):
            for filename in fnmatch.filter(files, '*.php'):
                with open (os.path.join(folder, filename), 'rb') as dest:
                    for l in dest.readlines():
                        try:
                            pattern = re.search(self.search_pattern, l).group(2)
                            if self.args.com.upper() in pattern:
                                patterns.append(pattern)
                        except:
                            continue

        self.write_file(patterns)

    def write_file(self, patterns):
        """

        :param patterns:
        :return:
        """
        file_name = os.path.join(self.args.out, '%s.%s.ini' % (self.args.lang, self.args.com.lower()))
        if not os.path.isfile(file_name):
            f = open(file_name, 'w+')
            f.close()
        with open(file_name, 'r+') as f:
            for p in patterns:
                found = any(p in line for line in f)
                if not found:
                    f.seek(0, os.SEEK_END)
                    f.write('%s=""\n' % p)
                    f.seek(0, os.SEEK_SET)
        f.close()


def main():
    parser = argparse.ArgumentParser(description='A translation ini file generator for joomla developers')
    parser.add_argument('--source', dest='path', help="directory to search in", required=True)
    parser.add_argument('--com', dest='com', help="the name of the component", required=True)
    parser.add_argument('--lang', dest='lang', default='en-GB', help="language localisation. default is en-GB")
    parser.add_argument('--out', dest='out', default='.', help="where to save the file")
    args = parser.parse_args()
    jf = JTranslate(args=args)
    jf.read_dir()


if __name__ == "__main__":
    main()
