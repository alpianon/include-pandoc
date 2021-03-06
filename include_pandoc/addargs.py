# This is a dummy module
# The real module (containing the argument definitions for the pandoc version
# installed on the system) is created by a post-install script, and can
# be updated (if and when pandoc is updated) by calling include-pandoc --update

def dummy():
    pass

# the following is just an example of how the 'real' module may look like
# when generated

'''
def addargs_pandoc_version():
    return "pandoc 2.6 Compiled with pandoc-types 1.17.5.4, texmath 0.11.2, skylighting 0.7.5"

def add_args(parser):
    parser.add_argument("-f", "-r", "--from", "--read", metavar="FORMAT", nargs=1, action="append")
    parser.add_argument("-t", "-w", "--to", "--write", metavar="FORMAT", nargs=1, action="append")
    parser.add_argument("-o", "--output", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--data-dir", metavar="DIRECTORY", nargs=1, action="append")
    parser.add_argument("--base-header-level", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--strip-empty-paragraphs", action="store_true")
    parser.add_argument("--indented-code-classes", metavar="STRING", nargs=1, action="append")
    parser.add_argument("-F", "--filter", metavar="PROGRAM", nargs=1, action="append")
    parser.add_argument("--lua-filter", metavar="SCRIPTPATH", nargs=1, action="append")
    parser.add_argument("-p", "--preserve-tabs", action="store_true")
    parser.add_argument("--tab-stop", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--track-changes", metavar="accept|reject|all", nargs=1, action="append")
    parser.add_argument("--file-scope", action="store_true")
    parser.add_argument("--extract-media", metavar="PATH", nargs=1, action="append")
    parser.add_argument("-s", "--standalone", action="store_true")
    parser.add_argument("--template", metavar="FILE", nargs=1, action="append")
    parser.add_argument("-M", "--metadata", metavar="KEY[:VALUE]", nargs=1, action="append")
    parser.add_argument("--metadata-file", metavar="FILE", nargs=1, action="append")
    parser.add_argument("-V", "--variable", metavar="KEY[:VALUE]", nargs=1, action="append")
    parser.add_argument("-D", "--print-default-template", metavar="FORMAT", nargs=1, action="append")
    parser.add_argument("--print-default-data-file", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--print-highlight-style", metavar="STYLE|FILE", nargs=1, action="append")
    parser.add_argument("--dpi", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--eol", metavar="crlf|lf|native", nargs=1, action="append")
    parser.add_argument("--wrap", metavar="auto|none|preserve", nargs=1, action="append")
    parser.add_argument("--columns", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--strip-comments", action="store_true")
    parser.add_argument("--toc", "--table-of-contents", action="store_true")
    parser.add_argument("--toc-depth", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--no-highlight", action="store_true")
    parser.add_argument("--highlight-style", metavar="STYLE|FILE", nargs=1, action="append")
    parser.add_argument("--syntax-definition", metavar="FILE", nargs=1, action="append")
    parser.add_argument("-H", "--include-in-header", metavar="FILE", nargs=1, action="append")
    parser.add_argument("-B", "--include-before-body", metavar="FILE", nargs=1, action="append")
    parser.add_argument("-A", "--include-after-body", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--resource-path", metavar="SEARCHPATH", nargs=1, action="append")
    parser.add_argument("--request-header", metavar="NAME:VALUE", nargs=1, action="append")
    parser.add_argument("--self-contained", action="store_true")
    parser.add_argument("--html-q-tags", action="store_true")
    parser.add_argument("--ascii", action="store_true")
    parser.add_argument("--reference-links", action="store_true")
    parser.add_argument("--reference-location", metavar="block|section|document", nargs=1, action="append")
    parser.add_argument("--atx-headers", action="store_true")
    parser.add_argument("--top-level-division", metavar="section|chapter|part", nargs=1, action="append")
    parser.add_argument("-N", "--number-sections", action="store_true")
    parser.add_argument("--number-offset", metavar="NUMBERS", nargs=1, action="append")
    parser.add_argument("--listings", action="store_true")
    parser.add_argument("-i", "--incremental", action="store_true")
    parser.add_argument("--slide-level", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--section-divs", action="store_true")
    parser.add_argument("--default-image-extension", metavar="extension", nargs=1, action="append")
    parser.add_argument("--email-obfuscation", metavar="none|javascript|references", nargs=1, action="append")
    parser.add_argument("--id-prefix", metavar="STRING", nargs=1, action="append")
    parser.add_argument("-T", "--title-prefix", metavar="STRING", nargs=1, action="append")
    parser.add_argument("-c", "--css", metavar="URL", nargs=1, action="append")
    parser.add_argument("--reference-doc", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--epub-subdirectory", metavar="DIRNAME", nargs=1, action="append")
    parser.add_argument("--epub-cover-image", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--epub-metadata", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--epub-embed-font", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--epub-chapter-level", metavar="NUMBER", nargs=1, action="append")
    parser.add_argument("--pdf-engine", metavar="PROGRAM", nargs=1, action="append")
    parser.add_argument("--pdf-engine-opt", metavar="STRING", nargs=1, action="append")
    parser.add_argument("--bibliography", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--csl", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--citation-abbreviations", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--natbib", action="store_true")
    parser.add_argument("--biblatex", action="store_true")
    parser.add_argument("--mathml", action="store_true")
    parser.add_argument("--webtex", metavar="URL", nargs="?", const=True)
    parser.add_argument("--mathjax", metavar="URL", nargs="?", const=True)
    parser.add_argument("--katex", metavar="URL", nargs="?", const=True)
    parser.add_argument("--gladtex", action="store_true")
    parser.add_argument("--abbreviations", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--trace", action="store_true")
    parser.add_argument("--dump-args", action="store_true")
    parser.add_argument("--ignore-args", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--fail-if-warnings", action="store_true")
    parser.add_argument("--log", metavar="FILE", nargs=1, action="append")
    parser.add_argument("--bash-completion", action="store_true")
    parser.add_argument("--list-input-formats", action="store_true")
    parser.add_argument("--list-output-formats", action="store_true")
    parser.add_argument("--list-extensions", metavar="FORMAT", nargs="?", const=True)
    parser.add_argument("--list-highlight-languages", action="store_true")
    parser.add_argument("--list-highlight-styles", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")
'''
