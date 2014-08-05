# coding: utf-8


from __future__ import unicode_literals
import os
import pexpect


class parser:
    """The parser class
    
    It opens a new process of the jar file, and waits for sentences.

    Example usage:
        >>> p = parser(jar, gr)
        >>> tree = p.parse("This is an apple")
        >>> print tree
        ( (S (NP (DT This)) (VP (VBZ is) (NP (DT an) (NN apple)))) )

    It's recommended to call the terminate method after all work,
    since the parser occupies quite a lot memory.
    """
    
    def __init__(self, jar_path, grammar_path):
        """Specify the path to the parser jar file
        and the grammar file.
        """

        # Check input
        if not jar_path.endswith('.jar') or not os.path.isfile(jar_path):
            raise Exception("Invalid jar file")
        if not grammar_path.endswith('.gr') or \
           not os.path.isfile(grammar_path):
            raise Exception("Invalid grammar file")

        cmd = 'java -jar %s -gr %s' % (jar_path, grammar_path)
        self.parser = pexpect.spawn(cmd)

    def parse(self, sent):
        """Parse a sentence into a tree string.
        
        Sentence more than 200 words can't be parsed due to the Berkeley
        parser limitation.
        """

        self.parser.sendline(sent)
        self.parser.expect('\r\n.*\r\n')
        return self.parser.after.strip()

    def terminate(self):
        self.parser.terminate()


def demo():
    import os
    jar = os.path.join(os.environ['HOME'],
                       'bin/berkeley_parser/BerkeleyParser-1.7.jar')
    gr = os.path.join(os.environ['HOME'],
                      'bin/berkeley_parser/eng_sm6.gr')

    print "Initializing the parser..."
    p = parser(jar, gr)
    print "Done\n"

    sentences = ["This is an apple",
                 "This is a tree",
                 "Please read the document",
                 "Thanks for your help",
                 "It 's a funny day"]

    for s in sentences:
        print p.parse(s)

    p.terminate()

if __name__ == '__main__':
    demo()
