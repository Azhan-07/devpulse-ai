import json,random
from datetime import datetime
from pathlib import Path
root=Path(__file__).resolve().parents[1]
quotes=json.loads((root/'scripts'/'quotes.json').read_text())
q=random.choice(quotes)
d=datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
readme=(root/'README.md').read_text()
def repl(txt,s,e,val):
 i=txt.index(s)+len(s); j=txt.index(e)
 return txt[:i]+"\n"+val+"\n"+txt[j:]
readme=repl(readme,'<!--QUOTE_START-->','<!--QUOTE_END-->',q)
readme=repl(readme,'<!--DATE_START-->','<!--DATE_END-->',d)
(root/'README.md').write_text(readme)
print('Updated README')
