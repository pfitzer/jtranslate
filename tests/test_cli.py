import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from jootranslate.cli import JooTranslate

class Args(object):
    path = os.path.join(myPath, 'files')
    com = 'com_test'
    lang = 'en-GB'

class TestCli(object):
    @classmethod
    def setup_class(self):
        args = Args()
        self.jt = JooTranslate(args=args)
        self.jt.read_dir()
        self.admin_lang = os.path.join(self.jt.paths['admin'], 'language', args.lang, self.jt.get_filename())
        self.com_lang = os.path.join(self.jt.paths['component'], 'language', args.lang, self.jt.get_filename())

    @classmethod
    def teardown_class(self):
        os.remove(self.admin_lang)
        os.rmdir(os.path.dirname(self.admin_lang))
        os.remove(self.com_lang)
        os.rmdir(os.path.dirname(self.com_lang))

    def test_files_exist(self):
        assert os.path.isfile(self.admin_lang)
        assert os.path.isfile(self.com_lang)

    def test_file_content(self):
        af = open(self.admin_lang, 'r')
        assert af.read() == 'COM_TEST_TEST_STRING=""\n'
        af.close()
        cf = open(self.com_lang, 'r')
        assert cf.read() == 'COM_TEST_TEST_STRING=""\n'
        cf.close()