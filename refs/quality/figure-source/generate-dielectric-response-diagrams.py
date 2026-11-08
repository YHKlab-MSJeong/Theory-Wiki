from pathlib import Path
import sys
from html import escape
out=Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
def svg(name,title,desc,body):
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 380" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arr" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8Z" fill="#42556c"/></marker></defs>
<rect width="960" height="380" fill="#f7f7f5"/>
<g font-family="system-ui, sans-serif" fill="#253142">{body}</g></svg>\n'''
    (out/name).write_text(s,encoding='utf-8')
def box(x,y,w,h,lines,fill='#fff'):
    z=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#253142" stroke-width="1.5"/>'
    for i,line in enumerate(lines): z+=f'<text x="{x+w/2}" y="{y+h/2+(i-(len(lines)-1)/2)*29+6}" text-anchor="middle" font-size="18">{escape(line)}</text>'
    return z
def arrow(x1,y1,x2,y2):return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#42556c" stroke-width="2" marker-end="url(#arr)"/>'
body=''
body+=box(35,105,240,135,['절연 결정의 평형 상태','원자 κ, 분극 P'])
body+=box(355,105,240,135,['원자 κ의 작은 변위','uκβ → uκβ + δuκβ'],'#e9f1f4')
body+=box(675,105,250,135,['전자 재배치와 이온 변위','분극 변화 δPα'],'#f8ede8')
body+=arrow(275,173,355,173)+arrow(595,173,675,173)
body+='<text x="480" y="295" text-anchor="middle" font-size="22">Z*κ,αβ = Ω ∂Pα / ∂uκβ = ∂Fκβ / ∂Eα</text><text x="480" y="335" text-anchor="middle" font-size="16">선형 응답 · 다른 원자 좌표 고정 · 거시 분극의 변화율</text>'
svg('born-effective-charge-response.svg','Born 유효전하의 변위와 분극 응답','평형 상태에서 원자 하나를 미소 변위시키면 전자 재배치를 포함한 분극 변화가 생기며 그 기울기로 Born 유효전하를 정의한다.',body)
body=box(20,135,150,90,['평형 구조','바닥상태'])+box(220,30,175,80,['전기장 응답','고정 이온 ε∞'],'#e9f1f4')+box(220,235,175,80,['원자 변위 응답','Born 전하 · 힘상수'],'#f8ede8')+box(455,185,150,70,['Born 전하'])+box(455,285,150,70,['힘상수 → 포논'])+box(650,235,125,70,['이온 εion'])+box(805,105,135,85,['정적 ε⁰','ε∞ + εion'])
body+=arrow(170,155,220,70)+arrow(170,205,220,275)+arrow(395,255,455,220)+arrow(395,295,455,320)+arrow(605,220,650,260)+arrow(605,320,650,280)+arrow(395,70,805,135)+arrow(775,270,805,170)
svg('dfpt-dielectric-workflow.svg','DFPT 유전 응답의 계산 흐름','바닥상태에서 전기장과 원자 변위 응답을 계산하고 Born 전하와 포논으로 이온 응답을 구성해 전자 응답과 합한다.',body)
body=box(35,110,190,100,['원자 종류','원자 구조'])+box(300,110,210,100,['SevenNet-Polar','등변 그래프 신경망'],'#e9f1f4')+box(585,45,335,95,['Born 유효전하 텐서','BEC 전용 또는 다중과제 출력'],'#f8ede8')+box(585,235,335,95,['에너지 · 힘 · 응력','다중과제 출력'])
body+=arrow(225,160,300,160)+arrow(510,135,585,92)+arrow(510,185,585,282)
body+='<text x="480" y="365" text-anchor="middle" font-size="16">유전율 계산: 포논 정보와 전자 응답 별도 필요</text>'
svg('sevennet-polar-outputs.svg','SevenNet-Polar의 모델 출력','원자 구조를 입력으로 Born 유효전하를 예측하며 다중과제 모델은 에너지 힘 응력도 출력한다. 유전율 계산에는 별도 포논과 전자 응답이 필요하다.',body)
