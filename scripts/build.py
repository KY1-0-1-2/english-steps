"""Validate lesson content and build a portable static website. Python 3.9+."""
from pathlib import Path
import json,re,shutil
ROOT=Path(__file__).resolve().parents[1]
def validate(lessons):
    assert isinstance(lessons,list) and lessons,'至少需要一課'
    ids=set();orders=set()
    for l in lessons:
        required={'id','level','order','title','minutes','goals','vocabulary','grammar','examples','quiz','task','sources','sourceNote'}
        assert required<=l.keys(),f'缺少欄位：{required-l.keys()}'
        assert re.fullmatch(r'(junior|senior|college)-[a-z0-9]+(?:-[a-z0-9]+)*',l['id']), 'id 格式錯誤'
        assert l['id'] not in ids,'id 重複';ids.add(l['id'])
        assert l['level'] in ('junior','senior','college') and l['id'].startswith(l['level']+'-'),'階段不一致'
        assert type(l['order']) is int and l['order']>0 and l['order'] not in orders,'排序需為唯一正整數';orders.add(l['order'])
        assert type(l['minutes']) is int and 5<=l['minutes']<=60,'預估時間需為 5–60 分鐘'
        for k in ('title','grammar','sourceNote'): assert isinstance(l[k],str) and l[k].strip(),f'{k} 不可空白'
        for k in ('goals','task'): assert isinstance(l[k],list) and l[k] and all(isinstance(s,str) and s.strip() for s in l[k]),f'{k} 格式錯誤'
        assert len(l['vocabulary'])>=3 and len(l['examples'])>=2 and len(l['quiz'])>=2,'需要 3 單字、2 例句與 2 題練習'
        for v in l['vocabulary']: assert all(isinstance(v.get(k),str) and v[k].strip() for k in ('word','meaning')),'單字格式錯誤'
        for e in l['examples']: assert all(isinstance(e.get(k),str) and e[k].strip() for k in ('en','zh')),'例句需中英對照'
        for q in l['quiz']:
            assert isinstance(q['question'],str) and q['question'].strip(),'題幹不可空白'
            assert isinstance(q['options'],list) and len(q['options'])==3 and len(set(q['options']))==3 and all(isinstance(o,str) and o.strip() for o in q['options']),'每題需要 3 個不重複選項'
            assert type(q['answer']) is int and 0<=q['answer']<3,'答案索引應為 0–2'
            assert isinstance(q['explanation'],str) and q['explanation'].strip(),'每題需要解析'
        assert isinstance(l['sources'],list),'sources 應為陣列'
        for s in l['sources']: assert s['url'].startswith('https://') and s['title'].strip(),'來源需要 HTTPS 與標題'
    return sorted(lessons,key=lambda l:l['order'])
if __name__=='__main__':
    lessons=validate(json.loads((ROOT/'content/lessons.json').read_text()))
    out=ROOT/'dist';out.mkdir(exist_ok=True)
    for name in ('index.html','styles.css','app.js'):shutil.copy2(ROOT/'web'/name,out/name)
    encoded=json.dumps(lessons,ensure_ascii=False).replace('<','\\u003c')
    (out/'lessons.js').write_text('const LESSONS = '+encoded+';\n')
    shutil.copy2(ROOT/'AGENTS.md',out/'AGENTS.md')
    print(f'PASS: {len(lessons)} lessons, {sum(len(l["quiz"]) for l in lessons)} questions; built dist/')
