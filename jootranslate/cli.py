import argparse
import fnmatch
import os
import re


class JooTranslate(object):
    paths = {}

    def __init__(self, args):
        """

        :param args:
        """
        self.args = args
        self.search_pattern = r'JText::_\((\'|"){1}(.*?)(\'|"){1}\)'
        self.set_file_paths()

    def read_dir(self):
        """

        :return:
        """
        for key, value in self.paths.items():
            patterns = []
            for folder, dirs, files in os.walk(value, topdown=False):
                for filename in fnmatch.filter(files, '*.php'):
                    with open(os.path.join(folder, filename), 'rb') as dest:
                        for l in dest.readlines():
                            try:
                                pattern = re.search(self.search_pattern, l.decode(('utf8'))).group(2)
                                if self.args.com.upper() in pattern:
                                    patterns.append(pattern)
                            except:
                                continue

            self.write_file(value, patterns)

    def write_file(self, path, patterns):
        """

        :param path:
        :param patterns:
        :return:
        """
        lang_file = os.path.join(path, 'language', self.args.lang, self.get_filename())
        if not os.path.exists(os.path.dirname(lang_file)):
            os.mkdir(os.path.dirname(lang_file))
        with open(lang_file, 'w+') as f:
            for p in patterns:
                found = any(p in line for line in f)
                if not found:
                    f.seek(0, os.SEEK_END)
                    f.write('%s=""\n' % p)
                    f.seek(0, os.SEEK_SET)
        f.close()

    def get_filename(self):
        """

        :return:
        """
        return '%s.%s.ini' % (self.args.lang, self.args.com.lower())

    def set_file_paths(self):
        """

        :return:
        """
        self.paths['component'] = os.path.join(self.args.path, 'components', self.args.com)
        self.paths['admin'] = os.path.join(self.args.path, 'administrator', 'components', self.args.com)


def main():
    parser = argparse.ArgumentParser(description='A translation ini file generator for joomla developers')
    parser.add_argument('--source', dest='path', help="directory to search in", required=True)
    parser.add_argument('--com', dest='com', help="the name of the component", required=True)
    parser.add_argument('--lang', dest='lang', default='en-GB', help="language localisation. default is en-GB")
    args = parser.parse_args()
    jt = JooTranslate(args=args)
    jt.read_dir()


if __name__ == "__main__":
    main()
