#!/usr/bin/env python3
"""Build editable Excalicord-compatible frames from a trusted layout JSON. Stdlib only."""
import argparse
import json
import math
from pathlib import Path
import random
import time
import uuid

TYPES = {'text', 'rectangle', 'ellipse', 'diamond', 'line', 'arrow'}

def number(value, name, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    if positive and value <= 0:
        raise ValueError(f'{name} must be positive')
    return value

def base(kind, x, y, w, h):
    return dict(id=uuid.uuid4().hex, type=kind, x=x, y=y, width=w, height=h,
        angle=0, strokeColor='#243746', backgroundColor='transparent',
        fillStyle='solid', strokeWidth=2, strokeStyle='solid', roughness=1,
        opacity=100, groupIds=[], frameId=None, roundness=None,
        seed=random.randint(1, 2147483646), version=1,
        versionNonce=random.randint(1, 2147483646), isDeleted=False,
        boundElements=None, updated=int(time.time()*1000), link=None, locked=False)

def build(data):
    width=number(data.get('width',1080),'width',True)
    height=number(data.get('height',1440),'height',True)
    pages=data.get('pages')
    if not isinstance(pages,list) or not pages:
        raise ValueError('pages must be a non-empty list')
    bg=data.get('background','#fffdf8')
    if not isinstance(bg,str): raise ValueError('background must be a string')
    elements=[]
    for idx,page in enumerate(pages):
        offset=idx*(width+160)
        frame=base('frame',offset,0,width,height)
        frame.update(name=str(page.get('title',f'{idx+1:02d}')),roughness=0)
        background=base('rectangle',offset,0,width,height)
        background.update(backgroundColor=bg,strokeColor=bg,roughness=0,
            locked=True,frameId=frame['id'])
        elements.append(background)
        groups={}
        specs=page.get('elements')
        if not isinstance(specs,list) or not specs:
            raise ValueError(f'Page {idx+1}: elements must be non-empty')
        for item in specs:
            kind=item.get('type')
            if kind not in TYPES: raise ValueError(f'Unsupported type: {kind}')
            x=number(item.get('x',0),'x');y=number(item.get('y',0),'y')
            text=None;points=None
            if kind=='text':
                text=item.get('text')
                if not isinstance(text,str) or not text.strip(): raise ValueError('text must be non-empty')
                size=number(item.get('fontSize',36),'fontSize',True)
                # Conservative estimate, not a font measurement. Visual QA is required.
                w=number(item.get('width',max(sum(.62 if ord(c)<128 else 1 for c in s) for s in text.split('\n'))*size),'text width',True)
                h=len(text.split('\n'))*size*1.35
                extents=(x,y,x+w,y+h)
            elif kind in ('line','arrow'):
                points=item.get('points')
                if not isinstance(points,list) or len(points)<2: raise ValueError('line/arrow requires at least 2 points')
                points=[[number(p[0],'point x'),number(p[1],'point y')] for p in points if isinstance(p,list) and len(p)==2]
                if len(points)!=len(item['points']):raise ValueError('invalid point')
                if points[0]!=[0,0]: raise ValueError('first point must be [0,0]')
                xs=[p[0] for p in points];ys=[p[1] for p in points]
                w=max(xs)-min(xs);h=max(ys)-min(ys)
                if w==h==0:raise ValueError('zero length line')
                extents=(x+min(xs),y+min(ys),x+max(xs),y+max(ys))
            else:
                w=number(item.get('width'),'shape width',True)
                h=number(item.get('height'),'shape height',True)
                extents=(x,y,x+w,y+h)
            if extents[0]<0 or extents[1]<0 or extents[2]>width or extents[3]>height:
                raise ValueError(f'Page {idx+1}: element outside frame: {text or kind}')
            e=base(kind,x+offset,y,w,h)
            e.update(frameId=frame['id'],strokeColor=item.get('color','#243746'),
                backgroundColor=item.get('fill','transparent'))
            if not isinstance(e['strokeColor'],str) or not isinstance(e['backgroundColor'],str):raise ValueError('colors must be strings')
            if item.get('group') is not None:
                group=item['group']
                if not isinstance(group,str):raise ValueError('group must be string')
                e['groupIds']=[groups.setdefault(group,uuid.uuid4().hex)]
            if kind=='rectangle':e['roundness']={'type':3}
            if text is not None:
                e.update(text=text,originalText=text,fontSize=size,fontFamily=2,
                    textAlign='left',verticalAlign='top',containerId=None,
                    autoResize=True,lineHeight=1.35)
            if points is not None:
                e.update(points=points,startBinding=None,endBinding=None,
                    startArrowhead=None,endArrowhead='arrow' if kind=='arrow' else None,
                    lastCommittedPoint=None)
            elements.append(e)
        elements.append(frame)
    return dict(type='excalidraw',version=2,source='https://excalicord.com',
        elements=elements,appState={'viewBackgroundColor':bg,'gridSize':None},files={})

def self_test():
    import copy
    p={'title':'Test','elements':[
        {'type':'text','x':10,'y':10,'text':'中文\nText','fontSize':20,'group':'a'},
        {'type':'rectangle','x':10,'y':90,'width':100,'height':40,'group':'a'},
        {'type':'arrow','x':150,'y':160,'points':[[0,0],[-80,-20]]}]}
    data={'width':300,'height':400,'pages':[p,copy.deepcopy(p)]}
    scene=build(data);els=scene['elements'];frames=[e for e in els if e['type']=='frame']
    assert len(frames)==2 and all(e['width']/e['height']==.75 for e in frames)
    ids={e['id'] for e in els};assert len(ids)==len(els)
    assert all(e['frameId'] in {f['id'] for f in frames} for e in els if e['type']!='frame')
    texts=[e for e in els if e['type']=='text'];assert texts[0]['text']=='中文\nText'
    assert texts[0]['groupIds']!=texts[1]['groupIds']
    shapes=[e for e in els if e['type']=='rectangle' and not e['locked']]
    assert shapes[0]['groupIds']==texts[0]['groupIds']
    assert not any(e['type']=='image' for e in els)
    for bad in [dict(type='arrow',x=10,y=10,points=[[0,0],[-20,0]]),
                dict(type='text',x=290,y=10,text='越界',fontSize=40),
                dict(type='rectangle',x=0,y=0,width=-2,height=10),
                dict(type='text',x=float('nan'),y=0,text='test'),
                dict(type='group',x=0,y=0)]:
        try:build({'width':300,'height':400,'pages':[{'elements':[bad]}]})
        except ValueError:pass
        else:raise AssertionError(f'Accepted bad input {bad}')
    print('PASS: frames, references, multilingual text, per-page groups, negative arrow bounds, invalid input')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('layout',nargs='?');ap.add_argument('--output');ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    if args.self_test:self_test();return
    if not args.layout or not args.output:ap.error('layout and --output required')
    try:
        scene=build(json.loads(Path(args.layout).read_text(encoding='utf-8')))
        path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(scene,ensure_ascii=False,indent=2),encoding='utf-8')
    except (ValueError,TypeError,KeyError,OSError) as exc:ap.exit(1,f'Error: {exc}\n')
    print(f'Created {path}: {len(scene["elements"])} native elements')

if __name__=='__main__':main()
