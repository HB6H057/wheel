import re

rep = {"condition1": "", "condition2": "text"} # define desired replacements here

# use these three lines to do the replacement
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
