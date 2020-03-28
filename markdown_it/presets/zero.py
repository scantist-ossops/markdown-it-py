"""
"Zero" preset, with nothing enabled. Useful for manual configuring of simple
modes. For example, to parse bold/italic only.
"""


def make():
    return {
        "options": {
            "maxNesting": 20,  # Internal protection, recursion limit
            "html": False,  # Enable HTML tags in source
            # this is just a shorthand for .disable(["html_inline", "html_block"])
            # used by the linkify rule:
            "linkify": False,  # autoconvert URL-like texts to links
            # used by the replacements and smartquotes rules:
            # Enable some language-neutral replacements + quotes beautification
            "typographer": False,
            # used by the smartquotes rule:
            # Double + single quotes replacement pairs, when typographer enabled,
            # and smartquotes on. Could be either a String or an Array.
            # For example, you can use '«»„“' for Russian, '„“‚‘' for German,
            # and ['«\xA0', '\xA0»', '‹\xA0', '\xA0›'] for French (including nbsp).
            "quotes": "\u201c\u201d\u2018\u2019",  # /* “”‘’ */
            # Renderer specific; these options are used directly in the HTML renderer
            "xhtmlOut": False,  # Use '/' to close single tags (<br />)
            "breaks": False,  # Convert '\n' in paragraphs into <br>
            "langPrefix": "language-",  # CSS language prefix for fenced blocks
            # Highlighter function. Should return escaped HTML,
            # or '' if the source string is not changed and should be escaped externaly.
            # If result starts with <pre... internal wrapper is skipped.
            # function (/*str, lang*/) { return ''; }
            "highlight": None,
        },
        "components": {
            "core": {"rules": ["normalize", "block", "inline"]},
            "block": {"rules": ["paragraph"]},
            "inline": {"rules": ["text"], "rules2": ["balance_pairs", "text_collapse"]},
        },
    }
