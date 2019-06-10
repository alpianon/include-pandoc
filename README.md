# include-pandoc

A wrapper for pandoc that processes include lines (like `!include path/to/included/file`) in markdown files before passing them to pandoc for further processing. 

It allows to assemble complex/modular texts with link texts referring to headers or link definitions contained in different files. 

It supports unlimited nested includes, and handles also relative include paths.

Include-pandoc should work on any Linux version and distribution. It should work also on Windows and OSX but it is untested on such platforms yet.

## 1. Installation

`sudo pip install include-pandoc && sudo include-pandoc --update`

or (as user)

`pip install --user include-pandoc && include-pandoc --update`

## 2. Usage

```bash
include-pandoc [PANDOC_OPTIONS] [FILES] | [--update]
```

Just call `include-pandoc` instead of `pandoc`, with the same syntax you would use with `pandoc`. Without putting any files, standard input will be processed.

If you update Pandoc on your system, before using `include-pandoc` again, you have to run `include-pandoc --update` (otherwise you will get an error); this will update the wrapper with possible new Pandoc options implemented by the new installed version. If you installed `pandoc-update` as root, you have to call `include-pandoc --update` as root (f.e. with sudo).

## 3. Include Syntax

Includes must be on **separate lines**, with the **include statement at the very beginning of the line**, with **no quotes** and **no escaped characters**. Some examples:

`!include relative_path/to/included/file.md`

`!include /absolute_path/to/included/file.md`

`!include path with spaces/to/included file.md`

If relative paths are used in includes, they are regarded as relative to the path of the file that contains the include line; also in nested/recursive includes, relative paths are regarded as relative to the path of the nested file that contains the include line, not to the main/parent file path.

So if `main.md` includes `parts/part1.md` and the latter in turn includes `parts/subparts/subpart1.md`:

- the include line in `main.md` will be `!include parts/part1.md`
- the include line in `part1.md` will be `!include subparts/subpart1.md`.

## 4. Rationale

### 4.1 The Problem

Existing solutions to implement includes in Pandoc are generally incomplete.

There are **filters that handle only code block includes**, like [pandoc-include-code](https://github.com/owickstrom/pandoc-include-code), that work well but **only for a specific purpose** (i.e. including code within a markdown guide).

There are **filters** like [pandoc-include](https://pypi.org/project/pandoc-include/) that allow to **include any kind of file** at any point of the markdown 'parent' file; however, they are all **limited by the architecture of Pandoc**.
As explained in [Pandoc's guide](https://pandoc.org/filters.html):

>«A “filter” is a program that modifies the AST, between the reader and the writer:
`INPUT --reader--> AST --filter--> AST --writer--> OUTPUT`.
Filters are “pipes” that read from standard input and write to standard output. They consume and produce a JSON representation of the pandoc AST».

The problem is that links and link definitions are processed by Pandoc's reader, and filters come only after it, and they can process Pandoc's AST and not the 'original' text.

As a consequence, when using Pandoc's include filters, if for instance a link text (`[Super Goof]`) contained in an included file (`part1.md`):

- references a header (`# Super Goof`) contained in another included file (`part2.md`), 

or 

- is defined (`[Super Goof]: #super_goof_id`) in another included file (`definitions.md`), 

such link will remain 'unresolved' (i.e, it will be rendered as `[Super Goof]`, without being changed to a link), because Pandoc processes links before the include filter merges all included files.

**This limitation prevents you to assemble working modular text documents through include filters in Pandoc**. 

Alternative workarounds seem not viable, too.

- Some propose to [concatenate files when calling pandoc](https://stackoverflow.com/a/5529508) (`pandoc 01.md 02.md 03.md`), but it is a solution that may get very complicated to manage compared to an include based solution, especially when coming to complex modular texts:
    - you would need to split the main document into small pieces, and further split -- or re-merge -- such pieces every time you want to move or change something, while it is much simpler to work on a main document that includes snippets from other files.   
- Some propose to [use m4 as a pre-processor](https://stackoverflow.com/a/36104553), but this would lead to a lot of complications, too, because of the way m4 processes quotes and macros:
    - for instance, if your text contains words corresponding to m4 macros like `changequote` or `define()` or others, m4 processes them as macros, even if they are in the middle of a line (and in some cases, even if no parentheses follow the reserved word!); so you should avoid to use any m4 reserved words in your text, but this is not an acceptable limitation; 
    - moreover, you cannot use in your text, for any reason, the character sequences you set as begin-quote and end-quote delimiters for m4 - otherwise you may get m4 errors like `dangling quote error-->m4:stdin:2: ERROR: end of file in string`; so you should choose very long and unlikely sequences of characters as begin-quote and end-quote delimiters, that in turn may lead to very awkward include lines.

### 4.2 The solution

I created a wrapper for Pandoc in order to process includes before passing the text(s) to Pandoc. It handles all the available options from the Pandoc version installed in your system and passes them transparently to Pandoc, but, before that, it processes the includes contained in the given file(s) (or in standard input if no filename is given). The chosen include syntax should not interfere with the remainder of the markdown text (like it happens instead with the m4 syntax).
In this way, you can create very complex modular texts with working links, no matter where the link is defined or where the referenced header is.


