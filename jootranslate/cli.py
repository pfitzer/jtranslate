import argparse
import fnmatch
import os
import re


class JooTranslate(object):
    paths = {}

    def __init__(self, args):
        """

        :param args: console arguments
        :type args: argparse
        """
        self.args = args
        self.search_pattern = r'(label=|description=|JText::_\()(\'|"){1}(.*?)(\'|"){1}'
        self.set_file_paths()

    def read_dir(self):
        """
        reads all php and xml files and searches for regex pattern

        :return void:
        """
        for key, value in self.paths.items():
            patterns = []
            for folder, dirs, files in os.walk(value, topdown=False):
                for filename in files:
                    if filename.endswith(('.php', '.xml')):
                        with open(os.path.join(folder, filename), 'rb') as dest:
                            for l in dest.readlines():
                                try:
                                    pattern = re.search(self.search_pattern, l.decode(('utf8'))).group(3)
                                    if self.args.com.upper() in pattern:
                                        patterns.append(pattern)
                                except:
                                    continue

            self.write_file(value, patterns)

    def write_file(self, path, patterns):
        """
        writes all found patterns to the ini file if pattern not exist

        :param path: the path to administrator or component root
        :type path: str
        :param patterns: list of found translation strings
        :type patterns: list
        :return void:
        """
        lang_file = os.path.join(path, 'language', self.args.lang, self.get_filename())
        if not os.path.exists(os.path.dirname(lang_file)):
            os.mkdir(os.path.dirname(lang_file))
        try:
            text = open(lang_file, 'r').read()
        except:
            text = False
        with open(lang_file, 'a+') as f:
            for p in patterns:
                found = any(p in line for line in f)
                if not found:
                    f.seek(0, os.SEEK_END)
                    if text and not text[-1:] == '\n':
                        f.write('\n')
                    f.write('%s=""\n' % p)
                    f.seek(0, os.SEEK_SET)
        f.close()

    def get_filename(self):
        """

        :return: name of the language ini file
        :rtype: str
        """
        return '%s.%s.ini' % (self.args.lang, self.args.com.lower())

    def set_file_paths(self):
        """
        sets the needed paths to administrator and component part

        :return: void
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
