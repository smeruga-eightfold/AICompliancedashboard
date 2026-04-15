"""
AI Compliance Dashboard
=======================
Run:  pip3 install streamlit pandas numpy plotly reportlab
      python3 -m streamlit run app.py
"""
import streamlit as st, pandas as pd, numpy as np, plotly.graph_objects as go
from datetime import datetime, timedelta
from io import BytesIO

st.set_page_config(page_title="AI Compliance Dashboard", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

# ━━━ CSS ━━━
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');
.stApp{background:#fff;font-family:'DM Sans',sans-serif}
[data-testid="stSidebar"]{background:#fff;border-right:1px solid #e0e0e0}
.sb{padding:1rem 1rem .8rem;border-bottom:1px solid #e0e0e0;margin-bottom:.5rem}
.sb-t{font-size:.72rem;font-weight:700;color:#1a73e8;text-transform:uppercase;letter-spacing:1px}
.sb-s{font-size:.62rem;font-weight:600;color:#5f6368;text-transform:uppercase}
.ss{font-size:.78rem;font-weight:700;color:#202124;padding:.8rem 0 .4rem}
.sc{display:inline-block;background:#e8eaed;color:#5f6368;font-size:.65rem;font-weight:600;padding:.1rem .4rem;border-radius:10px;margin-left:.3rem}
.pt{font-size:1.25rem;font-weight:400;color:#202124;padding-bottom:.8rem;border-bottom:1px solid #e0e0e0;margin-bottom:1.2rem}
.st_{font-size:1rem;font-weight:600;color:#202124;margin:1.5rem 0 .6rem}
.fl{font-size:.72rem;font-weight:600;color:#5f6368;text-transform:uppercase;letter-spacing:.3px;margin-bottom:.25rem}
.mt{width:100%;background:#fff;border:1px solid #e0e0e0;border-radius:8px;overflow:hidden;margin-bottom:.3rem}
.mth{display:flex;padding:.6rem 1.2rem;background:#f8f9fa;border-bottom:1px solid #e0e0e0;font-size:.72rem;font-weight:600;color:#5f6368;text-transform:uppercase;letter-spacing:.4px}
.mr{display:flex;align-items:center;padding:.75rem 1.2rem;border-bottom:1px solid #f1f3f4}
.mr:last-child{border-bottom:none}
.mrn{font-size:.88rem;color:#3c4043}
.mrs{font-size:.95rem;font-weight:600;color:#202124;text-align:center}
.pill{display:inline-flex;align-items:center;gap:5px;padding:.15rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600}
.pd{width:7px;height:7px;border-radius:50%;display:inline-block}
.pe .pd{background:#0d904f}.pe{background:#e6f4ea;color:#0d904f}
.pg .pd{background:#34a853}.pg{background:#e6f4ea;color:#1e7e34}
.po .pd{background:#f9ab00}.po{background:#fef7e0;color:#92400e}
.pf .pd{background:#ea4335}.pf{background:#fce8e6;color:#c5221f}
.pp .pd{background:#0d904f}.pp{background:#e6f4ea;color:#0d904f}
.pfl .pd{background:#ea4335}.pfl{background:#fce8e6;color:#c5221f}
.gl{font-size:.78rem;color:#5f6368;padding:.5rem 1.2rem;line-height:1.6}
.glr{display:flex;align-items:center;gap:8px;margin-bottom:.2rem}
.gld{width:7px;height:7px;border-radius:50%;flex-shrink:0;display:inline-block}
.ab{background:#fce8e6;border-left:3px solid #ea4335;padding:.7rem 1rem;border-radius:0 6px 6px 0;font-size:.84rem;color:#7f1d1d;margin:.5rem 0;line-height:1.5}
.ab strong{color:#991b1b}
.cb{background:#e8f0fe;border-left:3px solid #1a73e8;padding:.7rem 1rem;border-radius:0 4px 4px 0;font-size:.85rem;color:#174ea6;margin-bottom:1rem}
.dc{background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:1.2rem;min-height:140px}
.dt{display:inline-block;font-size:.68rem;font-weight:600;color:#1a73e8;background:#e8f0fe;padding:.12rem .5rem;border-radius:4px;margin-bottom:.7rem}
.dct{font-size:.95rem;font-weight:600;color:#202124;margin-bottom:.5rem}
.dcd{font-size:.82rem;color:#5f6368;line-height:1.45}
#MainMenu{visibility:hidden}footer{visibility:hidden}header{visibility:hidden}
.block-container{padding-top:1.5rem}
[data-testid="stRadio"] label,[data-testid="stRadio"] label span,[data-testid="stRadio"] label p{color:#202124!important}
[data-testid="stRadio"] div[role="radiogroup"] label span[data-testid="stMarkdownContainer"] p{color:#3c4043!important;font-size:.85rem!important}
[data-testid="stMultiSelect"] span{color:#202124!important}
.stRadio>label,.stSelectbox>label,.stMultiSelect>label,.stDateInput>label{color:#202124!important}
[data-testid="stCaptionContainer"]{color:#5f6368!important}
[data-testid="stDownloadButton"] button{border:1px solid #e0e0e0!important;background:#fff!important;color:#202124!important;font-family:'DM Sans',sans-serif!important;font-weight:500!important;font-size:.82rem!important}
[data-testid="stDownloadButton"] button:hover{background:#f8f9fa!important}

/* Force text visible — targeted, not breaking dropdowns */
.stMarkdown p,.stMarkdown span,.stMarkdown li,.stMarkdown strong,
[data-testid="stMarkdownContainer"] p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
[data-testid="stCaptionContainer"] p,
[data-testid="stRadio"] label p,
[data-testid="stRadio"] div[role="radiogroup"] label p{color:#202124!important}
[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] p{color:#5f6368!important}

/* Selectbox — white background, dark text */
[data-testid="stSelectbox"] [data-baseweb="select"]{background:#fff!important}
[data-testid="stSelectbox"] [data-baseweb="select"] span{color:#202124!important}
[data-testid="stSelectbox"] [data-baseweb="select"] input{color:#202124!important}
[data-baseweb="popover"]{background:#fff!important}
[data-baseweb="popover"] li{color:#202124!important}
[data-baseweb="popover"] li:hover{background:#f1f3f4!important}

/* Multiselect dropdown */
[data-testid="stMultiSelect"] [data-baseweb="select"]{background:#fff!important}
[data-testid="stMultiSelect"] span{color:#202124!important}

/* Dataframe white background */
[data-testid="stDataFrame"]{background:#fff!important;border-radius:8px}
[data-testid="stDataFrame"] table{background:#fff!important}
</style>""", unsafe_allow_html=True)

# ━━━ SIDEBAR NAV ━━━
NAV=["Resume Parsing","AI Interviewer","Match Score Quality","Recommendation Quality","Bias Studies"]
with st.sidebar:
    st.markdown('<div class="sb"><div class="sb-t">AI COMPLIANCE</div><div class="sb-s">Quality Monitoring</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="ss">AI Quality Modules <span class="sc">5</span></div>',unsafe_allow_html=True)
    page=st.selectbox("Module",NAV,index=0,label_visibility="collapsed",key="page_nav")

# ████████████████████████████████████████████████████
# █  RESUME PARSING                                   █
# ████████████████████████████████████████████████████
if page=="Resume Parsing":
    FA={"Standard PDF":(0.85,0.98),"DOCX":(0.75,0.90),"Multi-column PDF":(0.65,0.80),"Image-based resume":(0.60,0.75)}
    LB={"English":0.05,"German":-0.03,"Spanish":-0.04,"French":-0.03}
    IR_={"Standard PDF":0.02,"DOCX":0.05,"Multi-column PDF":0.10,"Image-based resume":0.22}
    HB={"Standard PDF":(0.02,0.08),"DOCX":(0.05,0.15),"Multi-column PDF":(0.10,0.22),"Image-based resume":(0.15,0.30)}
    LL=list(LB.keys()); FF=list(FA.keys())
    def gc(v):
        if v>=0.90:return"Excellent","pe"
        if v>=0.85:return"Good","po"
        return"Fair","pf"
    def gp(v):
        if v>=0.85:return"Excellent","pe"
        if v>=0.70:return"Great","pg"
        if v>=0.65:return"Good","po"
        return"Fair","pf"
    def gpr(v):
        if v>=0.90:return"Excellent","pe"
        if v>=0.80:return"Great","pg"
        if v>=0.75:return"Good","po"
        return"Fair","pf"
    def gr(v):
        if v>=0.90:return"Excellent","pe"
        if v>=0.80:return"Great","pg"
        if v>=0.75:return"Good","po"
        return"Fair","pf"
    def uh(v,t):
        return(t=="c"and v<0.85)or(t=="p"and v<0.65)or(t=="pr"and v<0.75)or(t=="r"and v<0.80)
    def gen_rp(sd,ed,ls,fs,seed=42):
        rng=np.random.default_rng(seed);nd=max((ed-sd).days,1);n=max(int(nd*int(rng.integers(15,31))),10);recs=[]
        for i in range(n):
            l,f=rng.choice(ls),rng.choice(fs);lo,hi=FA[f]
            ca=float(np.clip(rng.uniform(lo,hi)+LB[l],0,1));pa=float(np.clip(rng.uniform(lo,hi)+LB[l],0,1))
            iv=bool(rng.random()>IR_[f]);hl,hh=HB[f];hs=float(np.clip(rng.uniform(hl,hh),0,1))
            ts=sd+timedelta(seconds=int(rng.integers(0,max(nd*86400,1))))
            recs.append({"rid":f"R{i+1:05}","ts":ts,"lang":l,"fmt":f,"ca":round(ca,4),"pa":round(pa,4),"vld":iv,"hs":round(hs,4)})
        return pd.DataFrame(recs).sort_values("ts").reset_index(drop=True)
    def rp_pdf():
        from reportlab.lib.pagesizes import A4;from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle;from reportlab.lib.colors import HexColor;from reportlab.lib.units import mm;from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,HRFlowable
        buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
        sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368")
        ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
        h1=ParagraphStyle("H",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=16,spaceAfter=8)
        bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
        s=[Spacer(1,20),Paragraph("Resume Parsing — Methodology",ti),HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=12)]
        s.append(Paragraph("Pipeline: Validation → Cover Letter Detection → Text Extraction → Standardisation → Hallucination Detection",bd))
        s.append(Paragraph("Metrics: Contact (≥90% Excellent), Professional (≥85% Excellent), Parse Rate (≥90%), Reliability (≥90%)",bd))
        doc.build(s);buf.seek(0);return buf.getvalue()

    st.markdown('<div class="pt">Resume Parsing</div>',unsafe_allow_html=True)
    st.markdown('<div class="st_">Filters</div>',unsafe_allow_html=True)
    today=datetime.today().date()
    rc1,rc2,rc3,rc4=st.columns([1.2,1.2,1,1])
    with rc1:st.markdown('<div class="fl">From</div>',unsafe_allow_html=True);rpf=st.date_input("x",value=today-timedelta(days=30),max_value=today,label_visibility="collapsed",key="rpf")
    with rc2:st.markdown('<div class="fl">To</div>',unsafe_allow_html=True);rpt=st.date_input("x",value=today,max_value=today,label_visibility="collapsed",key="rpt")
    with rc3:st.markdown('<div class="fl">Language</div>',unsafe_allow_html=True);rpl=st.multiselect("x",LL,default=None,placeholder="All",label_visibility="collapsed",key="rpl");rpl=rpl or LL
    with rc4:st.markdown('<div class="fl">Format</div>',unsafe_allow_html=True);rpfm=st.multiselect("x",FF,default=None,placeholder="All",label_visibility="collapsed",key="rpfm");rpfm=rpfm or FF
    if not(rpf and rpt and rpf<=rpt):st.warning("Select valid time range.");st.stop()
    st.markdown("")
    if st.button("Check Quality",type="primary",key="rp_go"):st.session_state["rp_ok"]=True
    if not st.session_state.get("rp_ok"):st.caption("Click Check Quality to run.");st.stop()
    df=gen_rp(datetime.combine(rpf,datetime.min.time()),datetime.combine(rpt,datetime.max.time()),rpl,rpfm)
    ns=len(df);st.markdown("---")
    if ns<50:st.markdown(f'<div class="cb">Limited data ({ns} resumes).</div>',unsafe_allow_html=True)
    ca_=float(df["ca"].mean());pa_=float(df["pa"].mean());pr_=float(df["vld"].mean());rl_=float(1-df["hs"].mean())
    ml=[("Contact Info Accuracy",ca_,"c",gc),("Professional Background",pa_,"p",gp),("Parse Rate",pr_,"pr",gpr),("Reliability",rl_,"r",gr)]
    st.markdown('<div class="st_">Key Metrics</div>',unsafe_allow_html=True)
    h='<div class="mt"><div class="mth"><span style="flex:2">Metric</span><span style="flex:1;text-align:center">Score</span><span style="flex:1;text-align:center">Status</span></div>'
    ah=""
    for nm,vl,mt,gf in ml:
        gl,gcc=gf(vl);h+=f'<div class="mr"><span class="mrn" style="flex:2">{nm}</span><span class="mrs" style="flex:1">{vl:.1%}</span><span style="flex:1;text-align:center"><span class="pill {gcc}"><span class="pd"></span>{gl}</span></span></div>'
        if uh(vl,mt):ah+=f'<div class="ab">🚨 <strong>{nm}</strong> at {vl:.1%} — below threshold.</div>'
    h+='</div>';st.markdown(h,unsafe_allow_html=True)
    st.markdown('<div class="gl"><div class="glr"><span class="gld" style="background:#0d904f"></span><b>Excellent</b></div><div class="glr"><span class="gld" style="background:#34a853"></span><b>Great</b></div><div class="glr"><span class="gld" style="background:#f9ab00"></span><b>Good</b></div><div class="glr"><span class="gld" style="background:#ea4335"></span><b>Fair</b></div></div>',unsafe_allow_html=True)
    if ah:st.markdown(ah,unsafe_allow_html=True)
    # Trend
    st.markdown('<div class="st_">Quality Trend</div>',unsafe_allow_html=True)
    nd_=(datetime.combine(rpt,datetime.max.time())-datetime.combine(rpf,datetime.min.time())).days
    if nd_<=7:df["per"]=df["ts"].dt.date
    elif nd_<=60:df["per"]=df["ts"].dt.to_period("W").apply(lambda r:r.start_time.date())
    else:df["per"]=df["ts"].dt.to_period("M").apply(lambda r:r.start_time.date())
    tr=df.groupby("per").agg(c=("ca","mean"),p=("pa","mean"),v=("vld","mean"),h_=("hs","mean"),vol=("rid","size")).reset_index().sort_values("per")
    tr["r"]=1-tr["h_"];tr["per"]=pd.to_datetime(tr["per"])
    tm=st.radio("Metric",["Contact","Professional","Parse Rate","Reliability"],horizontal=True,key="rptm")
    mp={"Contact":("c",0.85,0.90),"Professional":("p",0.65,0.85),"Parse Rate":("v",0.75,0.90),"Reliability":("r",0.80,0.90)}
    cn,at_,et_=mp[tm];cv_=tr[cn].iloc[-1]if len(tr)>0 else 0;lc="#0d904f"if cv_>=et_ else"#f9ab00"if cv_>=at_ else"#ea4335"
    fig=go.Figure();fig.add_trace(go.Scatter(x=tr["per"],y=tr[cn],mode="lines+markers",name=tm,line=dict(color=lc,width=2.5),marker=dict(size=6,color=lc)))
    fig.add_trace(go.Bar(x=tr["per"],y=tr["vol"],name="Vol",marker_color="rgba(26,115,232,0.08)",yaxis="y2"))
    fig.add_hline(y=at_,line_dash="dash",line_color="#ea4335",opacity=0.5);fig.add_hline(y=et_,line_dash="dash",line_color="#0d904f",opacity=0.35)
    fig.update_layout(xaxis=dict(gridcolor="#f1f3f4"),yaxis=dict(tickformat=".0%",range=[max(0,tr[cn].min()-0.1),1.02],gridcolor="#f1f3f4"),yaxis2=dict(overlaying="y",side="right",showgrid=False,showticklabels=False,range=[0,tr["vol"].max()*5]),height=300,margin=dict(l=10,r=10,t=20,b=40),plot_bgcolor="#fff",paper_bgcolor="#fff",font=dict(family="DM Sans",color="#202124",size=12),legend=dict(orientation="h",y=1.05,x=1,xanchor="right",font=dict(size=10)),hovermode="x unified")
    st.plotly_chart(fig,use_container_width=True)
    st.markdown('<div class="st_">Downloads</div>',unsafe_allow_html=True)
    d1,d2,_=st.columns([1,1,2])
    with d1:st.download_button("⬇ Results CSV",df.to_csv(index=False).encode(),file_name="rp.csv",mime="text/csv",use_container_width=True,key="rpd1")
    with d2:st.download_button("⬇ Methodology PDF",rp_pdf(),file_name="rp_method.pdf",mime="application/pdf",use_container_width=True,key="rpd2")
    with st.expander("How Resume Parsing Works"):
        st.markdown("**Contact** ≥90% Excellent. **Professional** ≥85% Excellent. **Parse Rate** ≥90%. **Reliability** ≥90%.")
    st.stop()  # ← CRITICAL: prevents any code below from running



# ████████████████████████████████████████████████████
# █  BIAS STUDIES                                      █
# ████████████████████████████████████████████████████
elif page=="Bias Studies":
    st.markdown('<div class="pt">Bias Studies</div>',unsafe_allow_html=True)
    bst=st.radio("Study Type",["Impact Ratio Study","Perturbation Study"],horizontal=True,label_visibility="collapsed",key="bst")
    if bst=="Perturbation Study":
        st.markdown("---")
        import time as _time

        # ═══════════════════════════════════════════
        # PERTURBATION STUDY
        # ═══════════════════════════════════════════
        PT_JOBS=["Engineering","Sales","Operations","Marketing","Finance"]
        PT_EXPS=["Entry (0-2 yrs)","Mid (3-5 yrs)","Senior (6+ yrs)"]
        PT_GEOS=["US","Europe","India"]
        PT_CATS=["Gender","Nationality","Disability","Religion & Sexuality","Family Status","Career Gap","College"]

        JOB_BASE={"Engineering":2.05,"Sales":1.97,"Operations":2.00,"Marketing":1.95,"Finance":2.02}
        EXP_ADJ={"Entry (0-2 yrs)":-0.06,"Mid (3-5 yrs)":0.0,"Senior (6+ yrs)":0.08}
        GEO_ADJ={"US":0.02,"Europe":0.0,"India":-0.03}
        JOB_DIST={"Engineering":0.30,"Sales":0.20,"Operations":0.15,"Marketing":0.20,"Finance":0.15}
        EXP_DIST={"Entry (0-2 yrs)":0.35,"Mid (3-5 yrs)":0.40,"Senior (6+ yrs)":0.25}
        GEO_DIST_={"US":0.45,"Europe":0.30,"India":0.25}

        CAT_SHIFT={
            "Gender":(0.001,0.005),"Nationality":(0.010,0.025),"Disability":(0.000,0.005),
            "Religion & Sexuality":(0.010,0.025),"Family Status":(0.008,0.020),
            "Career Gap":(0.015,0.030),"College":(0.001,0.008),
        }

        def shift_mult(cat,jobs,exps,geos):
            m=1.0
            narrow=len(jobs)<=2 and len(exps)<=2 and len(geos)<=2
            if cat=="Career Gap":
                if "Engineering" in jobs or "Finance" in jobs: m*=2.0
                if "Senior (6+ yrs)" in exps: m*=2.0
                if len(jobs)==1 and len(exps)==1: m*=1.5
                if narrow: m*=1.3
            if cat=="College":
                if "Entry (0-2 yrs)" in exps: m*=2.5
                if len(exps)==1 and "Entry (0-2 yrs)" in exps: m*=2.0
                if narrow: m*=1.3
            if cat=="Nationality":
                if "India" in geos: m*=1.8
                if len(geos)==1 and "India" in geos: m*=1.5
                if "Europe" in geos: m*=1.4
            if cat=="Religion & Sexuality":
                if "India" in geos or "Europe" in geos: m*=1.3
                if narrow: m*=1.2
            if cat=="Gender":
                if len(jobs)==1 and len(geos)==1: m*=1.2
            if cat=="Family Status":
                if narrow: m*=1.3
            return m

        # Direction bias per category: how consistently the perturbation hurts/helps
        # 0.5 = random, 0.85 = mostly one direction
        CAT_DIR_BIAS={
            "Gender":0.52,"Nationality":0.65,"Disability":0.52,
            "Religion & Sexuality":0.60,"Family Status":0.60,
            "Career Gap":0.85,"College":0.75,
        }

        @st.cache_data
        def build_pool(seed=99):
            rng=np.random.default_rng(seed)
            resumes=[]
            for i in range(6000):
                jc=rng.choice(list(JOB_DIST.keys()),p=list(JOB_DIST.values()))
                el=rng.choice(list(EXP_DIST.keys()),p=list(EXP_DIST.values()))
                geo=rng.choice(list(GEO_DIST_.keys()),p=list(GEO_DIST_.values()))
                sk=float(rng.uniform(0.3,1.0));ex=float(rng.uniform(0.2,1.0))
                ed=float(rng.uniform(0.3,1.0));ti=float(rng.uniform(0.3,1.0))
                if el=="Entry (0-2 yrs)": ex*=0.6;ed*=1.1
                elif el=="Senior (6+ yrs)": ex*=1.2;sk*=1.1
                resumes.append({"rid":f"R{i+1:05}","jc":jc,"el":el,"geo":geo,
                    "sk":min(sk,1.0),"ex":min(ex,1.0),"ed":min(ed,1.0),"ti":min(ti,1.0)})
            positions=[]
            for j in range(60):
                jc=rng.choice(PT_JOBS);geo=rng.choice(PT_GEOS)
                positions.append({"pid":f"P{j+1:03}","jc":jc,"geo":geo,
                    "rsk":float(rng.uniform(0.4,0.9)),"rex":float(rng.uniform(0.3,0.8)),"red":float(rng.uniform(0.3,0.8))})
            return pd.DataFrame(resumes),pd.DataFrame(positions)

        def match_score(res,pos,rng):
            base=JOB_BASE.get(res["jc"],2.0)+EXP_ADJ.get(res["el"],0.0)+GEO_ADJ.get(res["geo"],0.0)
            sf=1.0-abs(res["sk"]-pos["rsk"]);ef=1.0-abs(res["ex"]-pos["rex"])
            edf=1.0-abs(res["ed"]-pos["red"]);tf=res["ti"]
            return round(float(base+0.35*sf+0.25*ef+0.15*edf+0.10*tf+rng.normal(0,0.08)),5)

        def perturb_score(orig,cat,sm,rng):
            lo,hi=CAT_SHIFT[cat]
            magnitude=float(rng.uniform(lo,hi))*sm
            # Directional bias: some categories consistently shift scores down
            dir_bias=CAT_DIR_BIAS.get(cat,0.5)
            direction=rng.choice([-1,1],p=[dir_bias,1-dir_bias])
            shift=direction*magnitude
            noise=float(rng.normal(0,0.003))
            return round(float(orig+shift+noise),5)

        def ttest(a,b):
            from math import erfc,sqrt
            n1,n2=len(a),len(b);m1,m2=np.mean(a),np.mean(b)
            s1,s2=np.std(a,ddof=1),np.std(b,ddof=1)
            if s1==0 and s2==0: return 0.0,1.0,0.0
            sp2=((n1-1)*s1**2+(n2-1)*s2**2)/(n1+n2-2)
            if sp2==0: return 0.0,1.0,0.0
            t=(m1-m2)/sqrt(sp2*(1/n1+1/n2))
            p=float(erfc(abs(t)/sqrt(2)))
            return round(float(t),5),round(p,5),round(float(m1-m2),5)

        # ── Filters ──
        st.markdown('<div class="st_">Filters</div>',unsafe_allow_html=True)
        today=datetime.today().date()
        ptr1,ptr2,pc1,pc2=st.columns(4)
        with ptr1:
            st.markdown('<div class="fl">From</div>',unsafe_allow_html=True)
            ptfrom=st.date_input("x",value=today-timedelta(days=180),max_value=today,label_visibility="collapsed",key="ptfrom")
        with ptr2:
            st.markdown('<div class="fl">To</div>',unsafe_allow_html=True)
            ptto=st.date_input("x",value=today,max_value=today,label_visibility="collapsed",key="ptto")
        with pc1:
            st.markdown('<div class="fl">Job Category</div>',unsafe_allow_html=True)
            ptj=st.multiselect("x",PT_JOBS,default=None,placeholder="All",label_visibility="collapsed",key="ptj")
            ptj=ptj or PT_JOBS
        with pc2:
            st.markdown('<div class="fl">Experience Level</div>',unsafe_allow_html=True)
            pte=st.multiselect("x",PT_EXPS,default=None,placeholder="All",label_visibility="collapsed",key="pte")
            pte=pte or PT_EXPS
        pc3,pc4,_,_=st.columns(4)
        with pc3:
            st.markdown('<div class="fl">Geography</div>',unsafe_allow_html=True)
            ptg=st.multiselect("x",PT_GEOS,default=None,placeholder="All",label_visibility="collapsed",key="ptg")
            ptg=ptg or PT_GEOS
        with pc4:
            st.markdown('<div class="fl">Perturbation Category</div>',unsafe_allow_html=True)
            ptc=st.multiselect("x",PT_CATS,default=None,placeholder="All",label_visibility="collapsed",key="ptc")
            ptc=ptc or PT_CATS

        if not(ptfrom and ptto and ptfrom<=ptto):
            st.warning("Please select a valid time range.");st.stop()
        st.markdown("")
        email_col,btn_col=st.columns([2,1])
        with email_col:
            st.markdown('<div class="fl">Email for notification</div>',unsafe_allow_html=True)
            pt_email=st.text_input("x",placeholder="you@company.com",label_visibility="collapsed",key="pt_email")
        with btn_col:
            st.markdown('<div class="fl">&nbsp;</div>',unsafe_allow_html=True)
            run_clicked=st.button("Run & Notify Me",type="primary",key="pt_go")

        # ── State machine: idle → running → done ──
        if run_clicked and pt_email:
            st.session_state["pt_state"]="running"
            st.session_state["pt_start"]=_time.time()
            st.session_state["pt_email_addr"]=pt_email
            st.session_state["pt_filters"]={"jobs":ptj,"exps":pte,"geos":ptg,"cats":ptc}
            st.rerun()
        elif run_clicked and not pt_email:
            st.warning("Please enter your email address.")

        pt_state=st.session_state.get("pt_state","idle")

        if pt_state=="idle":
            st.caption("Configure filters, enter your email, and click Run & Notify Me.")
            st.stop()

        # ── Running state ──
        if pt_state=="running":
            elapsed=_time.time()-st.session_state.get("pt_start",_time.time())
            duration=20.0
            stages=[
                (0.00,"Collecting source resumes from pool…"),
                (0.15,"Filtering by job category, experience, geography…"),
                (0.25,"Selecting 150 resumes and 5 positions…"),
                (0.35,"Generating Gender perturbations…"),
                (0.42,"Generating Nationality perturbations…"),
                (0.49,"Generating Disability perturbations…"),
                (0.56,"Generating Religion & Sexuality perturbations…"),
                (0.63,"Generating Family Status perturbations…"),
                (0.70,"Generating Career Gap perturbations…"),
                (0.77,"Generating College perturbations…"),
                (0.84,"Running match scoring on all resume pairs…"),
                (0.92,"Computing statistical tests…"),
                (0.97,"Finalizing results…"),
            ]
            if elapsed>=duration:
                st.session_state["pt_state"]="done"
                st.rerun()
            else:
                pct=min(elapsed/duration,0.99)
                msg="Processing…"
                for threshold,label in reversed(stages):
                    if pct>=threshold: msg=label;break
                st.progress(pct,text=msg)
                st.info(f"Study in progress… {int(elapsed)}/{int(duration)} seconds. You can navigate away — the study will continue.")
                _time.sleep(1)
                st.rerun()

        # ── Done state ──
        if pt_state=="done":
            addr=st.session_state.get("pt_email_addr","")
            st.success(f"✅ Perturbation study complete. Notification sent to **{addr}**.")
            st.markdown("")

            if st.button("View Results",type="primary",key="pt_view"):
                st.session_state["pt_state"]="results"
                st.rerun()
            st.stop()

        # ── Results state ──
        if pt_state=="results":
            addr=st.session_state.get("pt_email_addr","")
            st.success(f"✅ Study complete. Notification was sent to **{addr}**.")
            flt=st.session_state.get("pt_filters",{"jobs":PT_JOBS,"exps":PT_EXPS,"geos":PT_GEOS,"cats":PT_CATS})

            # Generate data
            all_res,all_pos=build_pool()
            fr=all_res[(all_res["jc"].isin(flt["jobs"]))&(all_res["el"].isin(flt["exps"]))&(all_res["geo"].isin(flt["geos"]))]
            fp=all_pos[all_pos["jc"].isin(flt["jobs"])]
            n_avail_r=len(fr);n_avail_p=len(fp)
            n_samp_r=min(150,n_avail_r);n_samp_p=min(5,n_avail_p)

            rng=np.random.default_rng(42)
            samp_r=fr.sample(n=n_samp_r,random_state=42).reset_index(drop=True) if n_samp_r>0 else pd.DataFrame()
            samp_p=fp.sample(n=n_samp_p,random_state=42).reset_index(drop=True) if n_samp_p>0 else pd.DataFrame()

            # Match each resume to one position
            pairs=[]
            if n_samp_r>0 and n_samp_p>0:
                for i,(_,res) in enumerate(samp_r.iterrows()):
                    pos=samp_p.iloc[i%n_samp_p]
                    orig=match_score(res,pos,rng)
                    pairs.append({"rid":res["rid"],"pid":pos["pid"],"jc":res["jc"],"el":res["el"],"geo":res["geo"],"orig":orig})

            # Perturb and compute
            results=[]
            for cat in flt["cats"]:
                sm=shift_mult(cat,flt["jobs"],flt["exps"],flt["geos"])
                origs=[p["orig"] for p in pairs]
                perts=[perturb_score(p["orig"],cat,sm,rng) for p in pairs]
                if len(origs)>=2:
                    ts,pv,diff=ttest(origs,perts)
                else:
                    ts,pv,diff=0.0,1.0,0.0
                passing=pv>0.05
                results.append({"Category":cat,"Resume_Pairs":len(origs),"Score_Difference":diff,
                    "p_value":pv,"t_score":ts,"_pass":passing,
                    "Status":"🟢 Pass" if passing else "🔴 Fail"})
            res_df=pd.DataFrame(results)

            st.markdown("---")
            st.caption(f"{n_samp_r} resumes · {n_samp_p} positions · {len(flt['cats'])} categories · {', '.join(flt['jobs'])} | {', '.join(flt['exps'])} | {', '.join(flt['geos'])}")

            # ── Readiness ──
            conf="High" if n_samp_r>=100 else "Medium" if n_samp_r>=50 else "Low"
            conf_color="#0d904f" if conf=="High" else "#f9ab00" if conf=="Medium" else "#ea4335"
            ready_pct=round((min(n_samp_r,150)/150*0.4+min(n_samp_p,5)/5*0.3+(len(flt["cats"])/7)*0.2+(1.0 if n_samp_r>=100 else 0.5 if n_samp_r>=50 else 0.2)*0.1)*100)
            rc="#0d904f" if ready_pct>=80 else "#f9ab00" if ready_pct>=60 else "#ea4335"
            circ=314.16;off_=circ*(1-ready_pct/100)

            st.markdown('<div class="st_">Study Readiness</div>',unsafe_allow_html=True)
            with st.expander("ℹ️  What is Perturbation Study Readiness? (click to learn)"):
                st.markdown(f"""
Readiness checks whether enough data exists for a statistically meaningful study.

**Components:**
- **Source Resumes (40%)** — Target: 150. Available: **{n_samp_r}**. {'Sufficient.' if n_samp_r>=150 else 'Below target — consider broadening filters.'}
- **Positions (30%)** — Target: 5. Available: **{n_samp_p}**. {'Sufficient.' if n_samp_p>=5 else 'Below target.'}
- **Category Coverage (20%)** — Testing **{len(flt['cats'])}** of 7 categories.
- **Statistical Confidence (10%)** — Based on pair count. **{conf}** confidence ({n_samp_r} pairs).

**Confidence levels:** High (100+ pairs) = reliable results. Medium (50-99) = indicative. Low (<50) = interpret with caution.

**Overall ≥80%** = Ready. **60-79%** = Caution. **<60%** = Insufficient.
""")

            dc,ic=st.columns([1,3])
            with dc:
                st.markdown(f'<div style="position:relative;width:130px;height:130px;margin:auto"><svg viewBox="0 0 120 120" width="130" height="130"><circle cx="60" cy="60" r="50" fill="none" stroke="#e8eaed" stroke-width="10"/><circle cx="60" cy="60" r="50" fill="none" stroke="{rc}" stroke-width="10" stroke-dasharray="{circ}" stroke-dashoffset="{off_}" stroke-linecap="round" transform="rotate(-90 60 60)"/></svg><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:1.6rem;font-weight:700;color:{rc}">{ready_pct}%</div></div>',unsafe_allow_html=True)
            with ic:
                st.markdown(f"&nbsp;&nbsp;{'✅' if n_samp_r>=150 else '⚠️' if n_samp_r>=50 else '❌'}&nbsp;&nbsp; {n_samp_r}/150 source resumes")
                st.markdown(f"&nbsp;&nbsp;{'✅' if n_samp_p>=5 else '⚠️' if n_samp_p>=2 else '❌'}&nbsp;&nbsp; {n_samp_p}/5 positions")
                st.markdown(f"&nbsp;&nbsp;{'✅' if len(flt['cats'])==7 else '⚠️'}&nbsp;&nbsp; {len(flt['cats'])}/7 perturbation categories")
                st.markdown(f"&nbsp;&nbsp;Confidence: <span style='color:{conf_color};font-weight:600'>{conf}</span> ({n_samp_r} pairs)",unsafe_allow_html=True)

            if ready_pct<80:
                st.warning("⚠️ Study readiness below threshold. Consider broadening filters.")
            st.markdown("---")

            # ── Results table ──
            st.markdown('<div class="st_">Results</div>',unsafe_allow_html=True)
            if len(res_df)==0:
                st.error("No results — insufficient data.");st.stop()

            disp=res_df[["Category","Resume_Pairs","Score_Difference","Status"]].copy()
            disp["Score_Difference"]=disp["Score_Difference"].apply(lambda x:f"{x:.5f}")
            disp=disp.rename(columns={"Resume_Pairs":"Resume Pairs","Score_Difference":"Score Difference"})
            st.dataframe(disp,use_container_width=True,hide_index=True)
            st.caption("🟢 Pass = p-value > 0.05 (no significant difference)  ·  🔴 Fail = p-value ≤ 0.05 (bias detected)")

            # Alerts
            for _,r in res_df[~res_df["_pass"]].iterrows():
                st.error(f"🚨 **{r['Category']}** perturbation test has failed — statistically significant score difference detected (difference: {r['Score_Difference']:.5f}). Please contact the AI Engineering team immediately.")

            st.markdown("---")

            # ── Downloads ──
            st.markdown('<div class="st_">Downloads</div>',unsafe_allow_html=True)

            def build_pt_report():
                from reportlab.lib.pagesizes import A4
                from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
                from reportlab.lib.colors import HexColor
                from reportlab.lib.units import mm
                from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,HRFlowable
                buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
                sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368");lt=HexColor("#f8f9fa")
                ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
                sub=ParagraphStyle("Su",parent=sty["Normal"],fontSize=11,textColor=gr_,spaceAfter=18)
                h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
                bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
                bu=ParagraphStyle("Bu",parent=bd,leftIndent=18,bulletIndent=6,spaceAfter=4)
                s=[Spacer(1,20),Paragraph("Perturbation Study — Results Report",ti),
                   Paragraph(f"Filters: {', '.join(flt['jobs'])} | {', '.join(flt['exps'])} | {', '.join(flt['geos'])}",sub),
                   HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14)]
                s.append(Paragraph("1. Summary",h1))
                s.append(Paragraph(f"This report presents the results of a perturbation sensitivity study. <b>{n_samp_r}</b> resumes were tested against <b>{n_samp_p}</b> positions across <b>{len(flt['cats'])}</b> perturbation categories.",bd))
                s.append(Paragraph(f"Study readiness: <b>{ready_pct}%</b>. Confidence level: <b>{conf}</b>.",bd))
                s.append(Paragraph("2. What Was Tested",h1))
                s.append(Paragraph("Each resume was scored against a position. Then, for each perturbation category, one protected attribute was modified on the resume and it was scored again. An Independent Samples T-Test determined whether the score difference is statistically significant.",bd))
                s.append(Paragraph("3. Results",h1))
                td=[["Category","Pairs","Score Diff","p-value","Result"]]
                for _,r in res_df.iterrows():
                    td.append([r["Category"],str(r["Resume_Pairs"]),f"{r['Score_Difference']:.5f}",f"{r['p_value']:.5f}","Pass" if r["_pass"] else "FAIL"])
                t=Table(td,colWidths=[120,50,70,70,50])
                t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
                    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9),
                    ("ALIGN",(1,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
                    ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
                    ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
                s.append(t);s.append(Spacer(1,10))
                s.append(Paragraph("4. Interpretation",h1))
                fails=res_df[~res_df["_pass"]]
                passes=res_df[res_df["_pass"]]
                if len(passes)>0:
                    s.append(Paragraph(f"<b>{len(passes)} categories passed</b> — the AI system shows no statistically significant sensitivity to changes in these protected characteristics. Score differences are negligible and within expected variance.",bd))
                if len(fails)>0:
                    s.append(Paragraph(f"<b>{len(fails)} category(s) failed:</b>",bd))
                    for _,f in fails.iterrows():
                        s.append(Paragraph(f"&bull; <b>{f['Category']}</b>: score difference of {f['Score_Difference']:.5f} with p-value {f['p_value']:.5f}. This indicates the AI model is sensitive to changes in this attribute. The match score changes significantly when this characteristic is modified, suggesting potential bias.",bu,bulletText=""))
                    s.append(Paragraph("<b>Recommended action:</b> Contact the AI Engineering team for investigation. The model may need retraining or additional debiasing for the failing categories.",bd))
                else:
                    s.append(Paragraph("All categories pass. The AI system treats candidates fairly regardless of protected characteristics being tested.",bd))
                s.append(Paragraph("5. Disclaimer",h1))
                s.append(Paragraph("This study uses simulated data for demonstration. Production studies use the Eightfold perturbation infrastructure with real resumes and LLM-generated perturbations.",bd))
                doc.build(s);buf.seek(0);return buf.getvalue()

            def build_pt_method():
                from reportlab.lib.pagesizes import A4
                from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
                from reportlab.lib.colors import HexColor
                from reportlab.lib.units import mm
                from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,HRFlowable
                buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
                sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368");lt=HexColor("#f8f9fa")
                ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
                sub=ParagraphStyle("Su",parent=sty["Normal"],fontSize=11,textColor=gr_,spaceAfter=18)
                h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
                bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
                bu=ParagraphStyle("Bu",parent=bd,leftIndent=18,bulletIndent=6,spaceAfter=4)
                s=[Spacer(1,20),Paragraph("Perturbation Study — Methodology",ti),
                   Paragraph("AI Compliance — Sensitivity Testing Framework",sub),
                   HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14)]
                s.append(Paragraph("1. What is Perturbation Testing?",h1))
                s.append(Paragraph("Perturbation testing evaluates whether changing a protected characteristic on a resume affects the AI match score. It ensures attributes like gender, nationality, disability, religion, family status, career history, and college do not unfairly influence scoring.",bd))
                s.append(Paragraph("2. Process",h1))
                s.append(Paragraph("<b>Step 1</b> — Collect 150 source resumes from the candidate pool matching the selected filters.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Step 2</b> — Select 5 positions from the same job categories.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Step 3</b> — Score each resume against its matched position (original score).",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Step 4</b> — For each of 7 categories, modify one attribute on the resume and re-score (perturbed score).",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Step 5</b> — Compare original and perturbed scores using an Independent Samples T-Test.",bu,bulletText="\u2022"))
                s.append(Paragraph("3. Perturbation Categories",h1))
                for title,desc in [("Gender","Name changed to imply different gender. Everything else identical."),
                    ("Nationality","Nationality, ethnicity, or citizenship info added."),
                    ("Disability","Disability information or paralympic interests added."),
                    ("Religion &amp; Sexuality","Religion or sexual orientation info added."),
                    ("Family Status","Parental or marital status added."),
                    ("Career Gap","Work dates shifted to create employment gap."),
                    ("College","College name changed (e.g. prestigious to average).")]:
                    s.append(Paragraph(f"<b>{title}</b> — {desc}",bu,bulletText="\u2022"))
                s.append(Paragraph("4. Statistical Test",h1))
                s.append(Paragraph("The Independent Samples T-Test compares the mean match scores of original and perturbed resumes. The <b>t-score</b> quantifies the difference. The <b>p-value</b> is the probability of observing this difference by chance.",bd))
                td=[["p-value","Meaning","Result"],["> 0.05","No significant difference","Pass"],["\u2264 0.05","Significant difference — bias detected","Fail"]]
                t=Table(td,colWidths=[60,230,70])
                t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
                    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9.5),
                    ("ALIGN",(0,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
                    ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
                    ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
                s.append(t);s.append(Spacer(1,8))
                s.append(Paragraph("5. Data Requirements",h1))
                s.append(Paragraph("<b>150 source resumes</b> from the filtered pool.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>5 positions</b> from the selected job categories.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>All 7 categories</b> recommended for full coverage.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>100+ pairs</b> for high-confidence T-test results.",bu,bulletText="\u2022"))
                s.append(Paragraph("6. Confidence Levels",h1))
                s.append(Paragraph("<b>High</b> (100+ pairs) — Results are statistically reliable.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Medium</b> (50-99 pairs) — Results are indicative but not definitive.",bu,bulletText="\u2022"))
                s.append(Paragraph("<b>Low</b> (&lt;50 pairs) — Results should be interpreted with caution. Consider broadening filters.",bu,bulletText="\u2022"))
                s.append(Paragraph("7. Limitations",h1))
                s.append(Paragraph("With fewer than 100 pairs, the T-test has reduced power and may miss real bias. This prototype uses simulated data. Production studies use actual resume perturbation via the Eightfold infrastructure.",bd))
                doc.build(s);buf.seek(0);return buf.getvalue()

            d1,d2=st.columns(2)
            with d1:
                with st.spinner("Generating report…"):rpt=build_pt_report()
                st.download_button("⬇ Download Results (PDF)",rpt,file_name="perturbation_report.pdf",mime="application/pdf",use_container_width=True,key="ptd1")
            with d2:
                with st.spinner("Generating methodology…"):mth=build_pt_method()
                st.download_button("⬇ Download Methodology (PDF)",mth,file_name="perturbation_methodology.pdf",mime="application/pdf",use_container_width=True,key="ptd2")

            with st.expander("How Perturbation Testing Works"):
                st.markdown("""
**What it tests** — Whether changing a protected characteristic on a resume causes the AI match score to change significantly.

**How** — 150 resumes are scored against matched positions. Each resume is modified in one category at a time and re-scored. A T-Test compares original vs perturbed scores.

**Pass** = p-value > 0.05 (scores are statistically similar — system is fair).

**Fail** = p-value ≤ 0.05 (scores differ significantly — bias detected).

**7 Categories** — Gender, Nationality, Disability, Religion & Sexuality, Family Status, Career Gap, College.
""")
        st.stop()
    st.markdown("---")

    # Constants
    IR_JOBS=["Engineering","Sales","Operations","Marketing","Finance"]
    IR_EXPS=["Entry (0-2 yrs)","Mid (3-5 yrs)","Senior (6+ yrs)"]
    IR_GEOS=["US","Europe","India"]
    IR_STGS=["Applied","Screened","Shortlisted","Interviewed"]
    STAGE_P={"Applied":0.52,"Screened":0.62,"Shortlisted":0.73,"Interviewed":0.84}
    EXP_B={"Entry (0-2 yrs)":-0.06,"Mid (3-5 yrs)":0.0,"Senior (6+ yrs)":0.05}
    JOB_B={"Engineering":0.03,"Sales":-0.02,"Operations":0.0,"Marketing":-0.03,"Finance":0.02}
    GEN_B={"Female":0.015,"Male":-0.010}
    RACE_B={"White":-0.012,"Black or African American":0.025,"Asian":0.008,"Hispanic or Latino":-0.018,"Native American or Alaskan Native":-0.008,"Native Hawaiian or Pacific Islander":-0.008,"Two or more races":-0.010}
    GEO_DEMO={"US":0.88,"Europe":0.60,"India":0.42}
    GEO_FP={"US":0.44,"Europe":0.40,"India":0.32}

    def generate_ir_data(sd,ed,jobs,exps,geos,stages,seed=77):
        rng=np.random.default_rng(seed);nd=max((ed-sd).days,1)
        n=min(max(int(nd*550*(len(jobs)/5)*(len(geos)/3)*(len(exps)/3)),500),250000)
        # Interaction effects: gender bias stronger in certain job categories
        JOB_GEN_INT={"Engineering":{"Female":-0.01,"Male":0.008},"Finance":{"Female":-0.008,"Male":0.006},
                     "Sales":{"Female":0.005,"Male":-0.003},"Marketing":{"Female":0.003,"Male":-0.002},"Operations":{"Female":0.0,"Male":0.0}}
        # Race bias varies by experience level
        EXP_RACE_INT={"Entry (0-2 yrs)":{"Hispanic or Latino":-0.01,"Asian":0.005},"Mid (3-5 yrs)":{},"Senior (6+ yrs)":{"White":0.005,"Black or African American":-0.008}}
        recs=[]
        for i in range(n):
            jc,el,geo,stg=rng.choice(jobs),rng.choice(exps),rng.choice(geos),rng.choice(stages)
            fp=GEO_FP[geo];gen=rng.choice(["Female","Male"],p=[fp,1-fp])
            race=rng.choice(list(RACE_B.keys()),p=[0.33,0.14,0.23,0.16,0.02,0.02,0.10])
            sp=STAGE_P[stg]+EXP_B[el]+JOB_B[jc]+GEN_B[gen]+RACE_B[race]
            sp+=(-0.02 if geo=="India" else -0.01 if geo=="Europe" else 0)
            # Interaction: job × gender
            sp+=JOB_GEN_INT.get(jc,{}).get(gen,0.0)
            # Interaction: experience × race
            sp+=EXP_RACE_INT.get(el,{}).get(race,0.0)
            sp=float(np.clip(sp,0.05,0.97))
            sel=bool(rng.random()<sp);da=bool(rng.random()<GEO_DEMO[geo])
            rp=bool(rng.random()<0.91);ep=bool(rng.random()<0.86);edp=bool(rng.random()<0.82)
            ni,ns_,nt=int(rng.integers(1,8)),int(rng.integers(1,10)),int(rng.integers(1,6))
            recs.append({"job_category":jc,"experience_level":el,"geography":geo,"hiring_stage":stg,
                "gender":gen,"race":race,"selected":sel,"demo_available":da,
                "resume_ok":rp,"exp_ok":ep,"edu_ok":edp,"n_ideal":ni,"n_skills":ns_,"n_titles":nt})
        return pd.DataFrame(recs)

    def compute_readiness(df):
        n=len(df);vol_s=100 if n>=100000 else 70 if n>=50000 else 40
        dp=df["demo_available"].mean()*100;demo_s=100 if dp>=80 else 70 if dp>=50 else 40
        cp=(df["resume_ok"].mean()+df["exp_ok"].mean()+df["edu_ok"].mean())/3*100;comp_s=100 if cp>=80 else 70 if cp>=50 else 40
        clp=((df["n_ideal"]>=3).mean()*0.33+(df["n_skills"]>=3).mean()*0.34+(df["n_titles"]>=3).mean()*0.33)*100;cal_s=100 if clp>=80 else 70 if clp>=50 else 40
        sn=df["hiring_stage"].nunique();cov_s=100 if sn>=4 else 60 if sn>=2 else 30
        ov=round(0.3*vol_s+0.2*demo_s+0.2*comp_s+0.2*cal_s+0.1*cov_s)
        items=[(vol_s,f"{n:,} applications across closed positions",n>=100000),
               (demo_s,f"{dp:.0f}% self-declared race/gender data available",dp>=80),
               (comp_s,f"{cp:.0f}% of profiles are complete",cp>=80),
               (cal_s,f"{clp:.0f}% of closed positions are well calibrated",clp>=70),
               (cov_s,f"{sn} of 4 hiring stages present in data",sn>=4)]
        return ov,items

    def ir_table(df,gcol):
        g=df.groupby(gcol).agg(N_Applicants=("selected","size"),N_Selected=("selected","sum")).reset_index()
        g["Scoring_Rate"]=(g["N_Selected"]/g["N_Applicants"]).round(3)
        ref=g["Scoring_Rate"].max();g["Impact_Ratio"]=(g["Scoring_Rate"]/ref).round(3)
        g["_pass"]=g["Impact_Ratio"]>=0.80
        g["Status"]=g["_pass"].apply(lambda x:"🟢 Pass" if x else "🔴 Fail")
        return g.sort_values("Scoring_Rate",ascending=False).reset_index(drop=True).rename(columns={gcol:"Group"})[["Group","N_Applicants","Scoring_Rate","Impact_Ratio","Status","_pass"]]

    def ir_intersectional(df):
        g=df.groupby(["race","gender"]).agg(N_Applicants=("selected","size"),N_Selected=("selected","sum")).reset_index()
        g["Scoring_Rate"]=(g["N_Selected"]/g["N_Applicants"]).round(3)
        ref=g["Scoring_Rate"].max();g["Impact_Ratio"]=(g["Scoring_Rate"]/ref).round(3)
        g["_pass"]=g["Impact_Ratio"]>=0.80
        g["Status"]=g["_pass"].apply(lambda x:"🟢 Pass" if x else "🔴 Fail")
        return g.sort_values("Scoring_Rate",ascending=False).reset_index(drop=True).rename(columns={"race":"Race/Ethnicity","gender":"Gender"})[["Race/Ethnicity","Gender","N_Applicants","Scoring_Rate","Impact_Ratio","Status","_pass"]]

    def fmt_tbl(df):
        d=df.drop(columns=["_pass"]).copy()
        d["N_Applicants"]=d["N_Applicants"].apply(lambda x:f"{x:,}")
        d["Scoring_Rate"]=d["Scoring_Rate"].apply(lambda x:f"{x:.3f}")
        d["Impact_Ratio"]=d["Impact_Ratio"].apply(lambda x:f"{x:.3f}")
        return d

    def show_alerts(df):
        fails=df[~df["_pass"]]
        for _,r in fails.iterrows():
            grp=r.get("Group",f"{r.get('Race/Ethnicity','')} — {r.get('Gender','')}")
            st.error(f"🚨 **{grp}** has an Impact Ratio of {r['Impact_Ratio']:.3f}, below the 4/5ths rule threshold (0.80). Please review and contact the AI Engineering team immediately.")

    # ── Filters ──
    st.markdown('<div class="st_">Filters</div>',unsafe_allow_html=True)
    today=datetime.today().date()
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:st.markdown('<div class="fl">From</div>',unsafe_allow_html=True);irf=st.date_input("x",value=today-timedelta(days=365),max_value=today,label_visibility="collapsed",key="irf")
    with c2:st.markdown('<div class="fl">To</div>',unsafe_allow_html=True);irt=st.date_input("x",value=today,max_value=today,label_visibility="collapsed",key="irt")
    with c3:st.markdown('<div class="fl">Job Category</div>',unsafe_allow_html=True);irj=st.multiselect("x",IR_JOBS,default=None,placeholder="All",label_visibility="collapsed",key="irj");irj=irj or IR_JOBS
    with c4:st.markdown('<div class="fl">Experience</div>',unsafe_allow_html=True);ire=st.multiselect("x",IR_EXPS,default=None,placeholder="All",label_visibility="collapsed",key="ire");ire=ire or IR_EXPS
    with c5:st.markdown('<div class="fl">Geography</div>',unsafe_allow_html=True);irg=st.multiselect("x",IR_GEOS,default=None,placeholder="All",label_visibility="collapsed",key="irg");irg=irg or IR_GEOS
    c6,_,_,_=st.columns(4)
    with c6:st.markdown('<div class="fl">Hiring Stage</div>',unsafe_allow_html=True);irs=st.multiselect("x",IR_STGS,default=None,placeholder="All",label_visibility="collapsed",key="irs");irs=irs or IR_STGS

    if not(irf and irt and irf<=irt):st.warning("Please select a valid time range.");st.stop()
    st.markdown("")
    if st.button("Run Impact Ratio Study",type="primary",key="ir_go"):st.session_state["ir_ok"]=True
    if not st.session_state.get("ir_ok"):st.caption("Configure filters and click Run Impact Ratio Study.");st.stop()

    # Generate
    with st.spinner("Generating applicant data — this may take a few seconds…"):
        ir_df=generate_ir_data(datetime.combine(irf,datetime.min.time()),datetime.combine(irt,datetime.max.time()),irj,ire,irg,irs)
    n_total=len(ir_df)
    st.markdown("---")
    st.caption(f"{n_total:,} applicants  ·  {irf.strftime('%b %d, %Y')} – {irt.strftime('%b %d, %Y')}  ·  {', '.join(irj)} | {', '.join(irg)}")

    # ══ READINESS ══
    ov,items=compute_readiness(ir_df)
    rc="#0d904f" if ov>=80 else "#f9ab00" if ov>=60 else "#ea4335"
    circ=314.16;off_=circ*(1-ov/100)
    st.markdown('<div class="st_">Data Readiness</div>',unsafe_allow_html=True)
    with st.expander("ℹ️  What is Data Readiness? (click to learn)"):
        st.markdown("""
Data Readiness checks whether your dataset meets minimum requirements for a meaningful study.

**Components & thresholds:**
- **Data Volume (30%)** — ≥100,000 applications = full score. <50,000 = insufficient.
- **Demographic Data (20%)** — ≥80% self-declared gender/race = full score. <50% = insufficient.
- **Profile Completeness (20%)** — ≥80% with resume + experience + education = full score.
- **Position Calibration (20%)** — ≥70% positions with 3+ ideal candidates, skills, titles.
- **Pipeline Coverage (10%)** — All 4 hiring stages present = full score.

**Overall ≥80%** = Ready (green). **60-79%** = Caution (yellow). **<60%** = Not ready (red).
Below 80% does not block the study but results should be interpreted with caution.
""")
    dc,ic=st.columns([1,3])
    with dc:
        st.markdown(f'<div style="position:relative;width:130px;height:130px;margin:auto"><svg viewBox="0 0 120 120" width="130" height="130"><circle cx="60" cy="60" r="50" fill="none" stroke="#e8eaed" stroke-width="10"/><circle cx="60" cy="60" r="50" fill="none" stroke="{rc}" stroke-width="10" stroke-dasharray="{circ}" stroke-dashoffset="{off_}" stroke-linecap="round" transform="rotate(-90 60 60)"/></svg><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:1.6rem;font-weight:700;color:{rc}">{ov}%</div></div>',unsafe_allow_html=True)
    with ic:
        for sc,lb,passing in items:
            icon="✅" if passing else ("⚠️" if sc>=60 else "❌")
            st.markdown(f"&nbsp;&nbsp;{icon}&nbsp;&nbsp; {lb}")
    if ov<80:st.warning("⚠️ Data readiness is below acceptable threshold. Results may not be reliable.")
    st.markdown("---")

    # ══ RESULTS ══
    st.markdown('<div class="st_">Results</div>',unsafe_allow_html=True)
    dv=st.selectbox("Select Demographic View",["All","Gender","Race / Ethnicity","Intersectional"],index=0,key="ir_dv")
    gen_tbl=ir_table(ir_df,"gender");race_tbl=ir_table(ir_df,"race");inter_tbl=ir_intersectional(ir_df)

    if dv in ["All","Gender"]:
        st.markdown("**Non-intersectional — Gender**")
        st.dataframe(fmt_tbl(gen_tbl),use_container_width=True,hide_index=True)
        show_alerts(gen_tbl)
    if dv in ["All","Race / Ethnicity"]:
        st.markdown("**Non-intersectional — Race / Ethnicity**")
        st.dataframe(fmt_tbl(race_tbl),use_container_width=True,hide_index=True)
        show_alerts(race_tbl)
    if dv in ["All","Intersectional"]:
        st.markdown("**Intersectional — Gender × Race / Ethnicity**")
        itf=inter_tbl.drop(columns=["_pass"]).copy();itf["N_Applicants"]=itf["N_Applicants"].apply(lambda x:f"{x:,}");itf["Scoring_Rate"]=itf["Scoring_Rate"].apply(lambda x:f"{x:.3f}");itf["Impact_Ratio"]=itf["Impact_Ratio"].apply(lambda x:f"{x:.3f}")
        st.dataframe(itf,use_container_width=True,hide_index=True)
        for _,r in inter_tbl[~inter_tbl["_pass"]].iterrows():
            st.error(f"🚨 **{r['Race/Ethnicity']} — {r['Gender']}** IR={r['Impact_Ratio']:.3f}, below 4/5ths threshold. Contact AI Engineering immediately.")
    st.caption("✅ Pass = IR ≥ 0.80  ·  ❌ Fail = IR < 0.80  ·  Reference: 4/5ths rule (EEOC, NYC LL144)")
    st.markdown("---")

    # ══ CHARTS ══
    st.markdown('<div class="st_">Charts</div>',unsafe_allow_html=True)
    cv=st.radio("Chart view",["Gender","Race"],horizontal=True,key="ir_cv")
    cdf=gen_tbl if cv=="Gender" else race_tbl
    cols=["#0d904f" if p else "#ea4335" for p in cdf["_pass"]]
    fig1=go.Figure(go.Bar(x=cdf["Group"],y=cdf["Scoring_Rate"],marker_color=cols,text=[f"{v:.3f}" for v in cdf["Scoring_Rate"]],textposition="outside",textfont=dict(size=11,color="#202124")))
    fig1.update_layout(yaxis=dict(title="Scoring Rate",gridcolor="#f1f3f4",range=[0,cdf["Scoring_Rate"].max()*1.15]),height=320,margin=dict(l=50,r=20,t=15,b=80),plot_bgcolor="#fff",paper_bgcolor="#fff",font=dict(family="DM Sans",color="#202124",size=12))
    st.plotly_chart(fig1,use_container_width=True)

    ic2=["#0d904f" if p else "#ea4335" for p in cdf["_pass"]]
    fig2=go.Figure(go.Bar(x=cdf["Group"],y=cdf["Impact_Ratio"],marker_color=ic2,text=[f"{v:.3f}" for v in cdf["Impact_Ratio"]],textposition="outside",textfont=dict(size=11,color="#202124")))
    fig2.add_hline(y=0.80,line_dash="dash",line_color="#ea4335",opacity=0.6,annotation_text="4/5ths (0.80)",annotation_position="top left",annotation_font_size=10,annotation_font_color="#ea4335")
    fig2.update_layout(yaxis=dict(title="Impact Ratio",gridcolor="#f1f3f4",range=[0,1.12]),height=320,margin=dict(l=50,r=20,t=15,b=80),plot_bgcolor="#fff",paper_bgcolor="#fff",font=dict(family="DM Sans",color="#202124",size=12))
    st.plotly_chart(fig2,use_container_width=True)
    st.markdown("---")

    # ══ DOWNLOADS — proper PDFs ══
    st.markdown('<div class="st_">Downloads</div>',unsafe_allow_html=True)

    def build_ir_report_pdf():
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.colors import HexColor
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
        buf=BytesIO()
        doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
        sty=getSampleStyleSheet()
        bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368");lt=HexColor("#f8f9fa")
        red=HexColor("#ea4335");grn=HexColor("#0d904f")
        ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
        sub=ParagraphStyle("Su",parent=sty["Normal"],fontSize=11,textColor=gr_,spaceAfter=18)
        h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
        h2=ParagraphStyle("H2",parent=sty["Heading2"],fontSize=12,textColor=dk,spaceBefore=12,spaceAfter=6)
        bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
        s=[]
        s.append(Spacer(1,20))
        s.append(Paragraph("Impact Ratio Study — Report",ti))
        s.append(Paragraph(f"Period: {irf.strftime('%B %d, %Y')} to {irt.strftime('%B %d, %Y')}",sub))
        s.append(HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14))
        # Intro
        s.append(Paragraph("1. Introduction",h1))
        s.append(Paragraph(
            "This report presents the results of an Impact Ratio study conducted to assess fairness "
            "in the AI-powered candidate selection process. The study follows the 4/5ths rule as outlined "
            "in U.S. Equal Employment Opportunity Commission (EEOC) guidelines and NYC Local Law 144.",bd))
        s.append(Paragraph(f"Total applicants analyzed: <b>{n_total:,}</b>",bd))
        s.append(Paragraph(f"Data readiness score: <b>{ov}%</b>",bd))
        # Methodology
        s.append(Paragraph("2. Methodology",h1))
        s.append(Paragraph(
            "For each demographic group, the <b>Selection Rate</b> is computed as the proportion of "
            "applicants who were selected (i.e., scored above the match threshold). The <b>Impact Ratio</b> "
            "is then calculated as the ratio of each group's selection rate to the highest selection rate "
            "observed (the reference group).",bd))
        s.append(Paragraph(
            "Under the 4/5ths rule, an Impact Ratio of 0.80 or above is considered a <b>Pass</b>. "
            "An Impact Ratio below 0.80 indicates potential <b>adverse impact</b>, meaning the group is "
            "being selected at less than 80% of the rate of the most-selected group.",bd))
        # Gender results
        s.append(Paragraph("3. Results — Gender (Non-intersectional)",h1))
        gt=gen_tbl.drop(columns=["_pass"])
        gdata=[["Group","N Applicants","Scoring Rate","Impact Ratio","Status"]]
        for _,r in gt.iterrows():
            gdata.append([str(r["Group"]),f"{int(r['N_Applicants']):,}",f"{r['Scoring_Rate']:.3f}",f"{r['Impact_Ratio']:.3f}",r["Status"]])
        t1=Table(gdata,colWidths=[100,90,80,80,70])
        t1.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9),
            ("ALIGN",(1,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
        s.append(t1);s.append(Spacer(1,10))
        # Race results
        s.append(Paragraph("4. Results — Race/Ethnicity (Non-intersectional)",h1))
        rt=race_tbl.drop(columns=["_pass"])
        rdata=[["Group","N Applicants","Scoring Rate","Impact Ratio","Status"]]
        for _,r in rt.iterrows():
            rdata.append([str(r["Group"]),f"{int(r['N_Applicants']):,}",f"{r['Scoring_Rate']:.3f}",f"{r['Impact_Ratio']:.3f}",r["Status"]])
        t2=Table(rdata,colWidths=[150,80,80,80,70])
        t2.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9),
            ("ALIGN",(1,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
        s.append(t2);s.append(Spacer(1,10))
        # Intersectional
        s.append(Paragraph("5. Results — Intersectional (Gender x Race/Ethnicity)",h1))
        it=inter_tbl.drop(columns=["_pass"])
        idata=[["Race/Ethnicity","Gender","N Applicants","Scoring Rate","Impact Ratio","Status"]]
        for _,r in it.iterrows():
            idata.append([str(r["Race/Ethnicity"]),str(r["Gender"]),f"{int(r['N_Applicants']):,}",f"{r['Scoring_Rate']:.3f}",f"{r['Impact_Ratio']:.3f}",r["Status"]])
        t3=Table(idata,colWidths=[120,55,70,70,70,55])
        t3.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),8),
            ("ALIGN",(2,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
            ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
        s.append(t3);s.append(Spacer(1,10))
        # Conclusion
        s.append(Paragraph("6. Conclusion",h1))
        af=pd.concat([gen_tbl[~gen_tbl["_pass"]],race_tbl[~race_tbl["_pass"]]])
        if len(af)==0:
            s.append(Paragraph("All demographic groups pass the 4/5ths rule. <b>No adverse impact detected.</b>",bd))
        else:
            s.append(Paragraph(f"Adverse impact detected for <b>{len(af)} group(s)</b>. The following groups have an Impact Ratio below 0.80:",bd))
            for _,f in af.iterrows():
                s.append(Paragraph(f"&bull; <b>{f['Group']}</b>: IR = {f['Impact_Ratio']:.3f}",bd))
            s.append(Paragraph("Recommend immediate review and consultation with the AI Engineering team.",bd))
        doc.build(s);buf.seek(0);return buf.getvalue()

    def build_ir_methodology_pdf():
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.colors import HexColor
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
        buf=BytesIO()
        doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
        sty=getSampleStyleSheet()
        bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368");lt=HexColor("#f8f9fa")
        ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
        sub=ParagraphStyle("Su",parent=sty["Normal"],fontSize=11,textColor=gr_,spaceAfter=18)
        h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
        bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
        bu=ParagraphStyle("Bu",parent=bd,leftIndent=18,bulletIndent=6,spaceAfter=4)
        s=[]
        s.append(Spacer(1,20))
        s.append(Paragraph("Impact Ratio Study — Methodology",ti))
        s.append(Paragraph("AI Compliance — Fairness Testing Framework",sub))
        s.append(HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14))
        # What
        s.append(Paragraph("1. What is an Impact Ratio Study?",h1))
        s.append(Paragraph(
            "An Impact Ratio study evaluates whether an AI-powered selection system treats demographic "
            "groups fairly. It compares the rate at which different groups are selected (e.g., scored above "
            "a match threshold) and checks whether any group is disproportionately disadvantaged.",bd))
        s.append(Paragraph(
            "This methodology is based on the U.S. Equal Employment Opportunity Commission (EEOC) Uniform "
            "Guidelines on Employee Selection Procedures and is aligned with NYC Local Law 144 requirements "
            "for automated employment decision tools (AEDTs).",bd))
        # How
        s.append(Paragraph("2. How is the Impact Ratio Calculated?",h1))
        s.append(Paragraph("<b>Step 1 — Selection Rate:</b> For each demographic group, compute the proportion of applicants who were selected.",bd))
        s.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Selection Rate = Number Selected / Total Applicants in Group",bd))
        s.append(Paragraph("<b>Step 2 — Reference Group:</b> Identify the group with the highest selection rate. This becomes the reference (comparator) group.",bd))
        s.append(Paragraph("<b>Step 3 — Impact Ratio:</b> Divide each group's selection rate by the reference group's selection rate.",bd))
        s.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Impact Ratio = SR(group) / SR(reference)",bd))
        # Rule
        s.append(Paragraph("3. The 4/5ths Rule",h1))
        s.append(Paragraph(
            "The 4/5ths rule (also called the 80% rule) states that if the selection rate for any group is "
            "less than 80% (four-fifths) of the selection rate of the group with the highest rate, there is "
            "evidence of potential adverse impact.",bd))
        tdata=[["Impact Ratio","Interpretation","Action"],
               ["\u2265 0.80","Pass — No adverse impact","No action required"],
               ["< 0.80","Fail — Potential adverse impact","Investigate and contact AI Engineering"]]
        t=Table(tdata,colWidths=[80,180,180])
        t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9.5),
            ("ALIGN",(0,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
        s.append(t);s.append(Spacer(1,8))
        # Demographics
        s.append(Paragraph("4. Demographic Breakdowns",h1))
        s.append(Paragraph("<b>Non-intersectional Gender:</b> Compares selection rates between Female and Male applicants.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Non-intersectional Race/Ethnicity:</b> Compares selection rates across racial/ethnic groups (White, Black or African American, Asian, Hispanic or Latino, Native American or Alaskan Native, Native Hawaiian or Pacific Islander, Two or more races).",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Intersectional (Gender x Race):</b> Examines every combination of gender and race. This can reveal bias hidden in non-intersectional views — e.g., Hispanic females may face adverse impact even if Hispanic applicants overall pass.",bu,bulletText="\u2022"))
        # Data
        s.append(Paragraph("5. Data Requirements",h1))
        s.append(Paragraph("A minimum of <b>100,000 applications</b> across closed positions for a meaningful period (e.g. 1 year).",bu,bulletText="\u2022"))
        s.append(Paragraph("Applicants across <b>all stages</b> of the interview pipeline (Applied, Screened, Shortlisted, Interviewed).",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Self-declared PII data</b> — gender and race/ethnicity.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Complete profiles</b> — resume, work experience, education, and title.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Well-calibrated positions</b> — minimum 3 ideal candidates, 3 preferred skills, 3 preferred titles.",bu,bulletText="\u2022"))
        # Readiness
        s.append(Paragraph("6. Data Readiness Score",h1))
        s.append(Paragraph("Before the study runs, a readiness score is computed from 5 components:",bd))
        s.append(Paragraph("<b>Data Volume (30%)</b> — \u2265100K = full score; <50K = insufficient.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Demographic Data (20%)</b> — \u226580% self-declared = full score; <50% = insufficient.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Profile Completeness (20%)</b> — \u226580% complete profiles = full score.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Position Calibration (20%)</b> — \u226570% well-calibrated positions = full score.",bu,bulletText="\u2022"))
        s.append(Paragraph("<b>Pipeline Coverage (10%)</b> — all 4 stages present = full score.",bu,bulletText="\u2022"))
        s.append(Paragraph("A readiness score \u226580% is recommended. Below 80%, results should be interpreted with caution.",bd))
        # Limitations
        s.append(Paragraph("7. Limitations",h1))
        s.append(Paragraph("The 4/5ths rule is a practical guideline, not a definitive legal test. At small sample sizes, impact ratios can be unreliable — a single additional selection can flip the result.",bd))
        s.append(Paragraph("This study uses simulated data for demonstration purposes. Real studies require actual self-declared demographic data from applicants.",bd))
        s.append(Paragraph("Reference: EEOC Uniform Guidelines, NYC Local Law 144, BABL Eightfold Bias Audit.",bd))
        doc.build(s);buf.seek(0);return buf.getvalue()

    d1,d2=st.columns(2)
    with d1:
        with st.spinner("Generating report PDF…"):
            rpt_pdf=build_ir_report_pdf()
        st.download_button("⬇ Download Study Report (PDF)",rpt_pdf,file_name="impact_ratio_report.pdf",mime="application/pdf",use_container_width=True,key="ird1")
    with d2:
        with st.spinner("Generating methodology PDF…"):
            meth_pdf=build_ir_methodology_pdf()
        st.download_button("⬇ Download Methodology (PDF)",meth_pdf,file_name="impact_ratio_methodology.pdf",mime="application/pdf",use_container_width=True,key="ird2")

    with st.expander("How Impact Ratio Study Works"):
        st.markdown("**Selection Rate** = selected / total per group (e.g. 0.624 = 62.4%).\n\n**Impact Ratio** = group SR / highest SR. IR=1.000 = parity.\n\n**4/5ths Rule** — IR<0.80 = potential adverse impact.\n\n**Intersectional** — Gender × Race combinations to detect hidden bias.")
    st.stop()



# ████████████████████████████████████████████████████
# █  AI INTERVIEWER                                    █
# ████████████████████████████████████████████████████
elif page=="AI Interviewer":
    st.markdown('<div class="pt">AI Interviewer</div>',unsafe_allow_html=True)

    AI_ROLES=["Engineering","Sales","Operations","Marketing","Finance"]
    AI_ITYPES=["Screening","Technical","Behavioral"]
    AI_EXPS=["Entry","Mid","Senior"]
    AI_GEOS=["US","India","Europe"]
    AI_LANGS=["English","Hindi","Spanish","French","German"]
    AI_GENDERS=["Female","Male"]
    AI_RACES=["White","Black","Asian","Hispanic","Other"]
    AI_ACCENTS=["Native","Non-native"]
    AI_OUTCOMES=["Selected","Rejected","Pending"]

    # Score generation parameters (realistic, causal)
    ROLE_BASE={"Engineering":0.88,"Finance":0.85,"Operations":0.83,"Marketing":0.80,"Sales":0.77}
    EXP_ADJ__={"Entry":-0.04,"Mid":0.03,"Senior":-0.01}
    GEO_ADJ__={"US":0.02,"India":-0.01,"Europe":0.0}
    ITYPE_ADJ={"Screening":0.02,"Technical":-0.01,"Behavioral":0.01}
    # Slight bias for perturbation/IR realism
    GENDER_ADJ__={"Female":0.005,"Male":-0.003}
    RACE_ADJ__={"White":0.0,"Black":-0.008,"Asian":0.003,"Hispanic":-0.006,"Other":-0.004}
    ACCENT_ADJ={"Native":0.005,"Non-native":-0.008}

    @st.cache_data
    def gen_ai_data(seed=88):
        rng=np.random.default_rng(seed);n=60000;recs=[]
        for i in range(n):
            role=rng.choice(AI_ROLES);itype=rng.choice(AI_ITYPES);exp=rng.choice(AI_EXPS)
            geo=rng.choice(AI_GEOS);lang=rng.choice(AI_LANGS)
            gen=rng.choice(AI_GENDERS,p=[0.43,0.57]);race=rng.choice(AI_RACES,p=[0.35,0.15,0.22,0.16,0.12])
            accent=rng.choice(AI_ACCENTS,p=[0.6,0.4])
            base=ROLE_BASE[role]+EXP_ADJ__[exp]+GEO_ADJ__[geo]+ITYPE_ADJ[itype]
            # Interview metrics
            coverage=float(np.clip(base+rng.normal(0,0.06),0.5,1.0))
            clarity=float(np.clip(base+0.02+rng.normal(0,0.05),0.5,1.0))
            resume_rel=float(np.clip(base-0.01+rng.normal(0,0.06),0.5,1.0))
            compliance=float(np.clip(0.95+rng.normal(0,0.03),0.7,1.0))
            # Feedback metrics
            accuracy=float(np.clip(base+0.01+rng.normal(0,0.05),0.5,1.0))
            completeness=float(np.clip(base-0.02+rng.normal(0,0.06),0.5,1.0))
            evidence=float(np.clip(base+rng.normal(0,0.05),0.5,1.0))
            # AI score (for IR/perturbation)
            ai_score=float(np.clip(base+GENDER_ADJ__[gen]+RACE_ADJ__[race]+ACCENT_ADJ[accent]+rng.normal(0,0.08),0.3,1.0))
            sel_prob=float(np.clip(ai_score-0.15+rng.normal(0,0.1),0.1,0.9))
            outcome=rng.choice(["Selected","Rejected","Pending"],p=[sel_prob*0.5,0.9-sel_prob*0.5,0.1])
            # Perturbation: small noise, mostly <1% diff
            pert_score=float(ai_score+rng.normal(0,0.005)*rng.choice([1,1,1,1,2]))  # rare larger shifts
            pert_score=float(np.clip(pert_score,0.3,1.0))
            ts=datetime(2024,1,1)+timedelta(days=int(rng.integers(0,730)))
            recs.append({"role":role,"itype":itype,"exp":exp,"geo":geo,"lang":lang,
                "gender":gen,"race":race,"accent":accent,"outcome":outcome,
                "coverage":round(coverage,4),"clarity":round(clarity,4),"resume_rel":round(resume_rel,4),
                "compliance":round(compliance,4),"accuracy":round(accuracy,4),
                "completeness":round(completeness,4),"evidence":round(evidence,4),
                "ai_score":round(ai_score,4),"pert_score":round(pert_score,4),"ts":ts})
        return pd.DataFrame(recs)

    def color_val(v):
        if v>=0.90:return "🟢"
        if v>=0.75:return "🟡"
        return "🔴"

    # ── Filters ──
    st.markdown('<div class="st_">Filters</div>',unsafe_allow_html=True)
    today=datetime.today().date()
    a1,a2,a3,a4=st.columns(4)
    with a1:st.markdown('<div class="fl">From</div>',unsafe_allow_html=True);aif=st.date_input("x",value=today-timedelta(days=365),max_value=today,label_visibility="collapsed",key="aif")
    with a2:st.markdown('<div class="fl">To</div>',unsafe_allow_html=True);ait=st.date_input("x",value=today,max_value=today,label_visibility="collapsed",key="ait")
    with a3:st.markdown('<div class="fl">Role / Job Category</div>',unsafe_allow_html=True);air=st.multiselect("x",AI_ROLES,default=None,placeholder="All",label_visibility="collapsed",key="air");air=air or AI_ROLES
    with a4:st.markdown('<div class="fl">Interview Type</div>',unsafe_allow_html=True);aiit=st.multiselect("x",AI_ITYPES,default=None,placeholder="All",label_visibility="collapsed",key="aiit");aiit=aiit or AI_ITYPES
    a5,a6,a7,a8=st.columns(4)
    with a5:st.markdown('<div class="fl">Experience Level</div>',unsafe_allow_html=True);aie=st.multiselect("x",AI_EXPS,default=None,placeholder="All",label_visibility="collapsed",key="aie");aie=aie or AI_EXPS
    with a6:st.markdown('<div class="fl">Geography</div>',unsafe_allow_html=True);aig=st.multiselect("x",AI_GEOS,default=None,placeholder="All",label_visibility="collapsed",key="aig");aig=aig or AI_GEOS
    with a7:st.markdown('<div class="fl">Language</div>',unsafe_allow_html=True);ail=st.multiselect("x",AI_LANGS,default=None,placeholder="All",label_visibility="collapsed",key="ail");ail=ail or AI_LANGS
    with a8:st.markdown('<div class="fl">Outcome</div>',unsafe_allow_html=True);aio=st.multiselect("x",AI_OUTCOMES,default=None,placeholder="All",label_visibility="collapsed",key="aio");aio=aio or AI_OUTCOMES

    if not(aif and ait and aif<=ait):st.warning("Please select a valid time range.");st.stop()
    st.markdown("")
    if st.button("Check AI Interview Quality",type="primary",key="ai_go"):st.session_state["ai_ok"]=True
    if not st.session_state.get("ai_ok"):st.caption("Configure filters and click Check AI Interview Quality.");st.stop()

    # Filter data
    with st.spinner("Analyzing AI interviewer data…"):
        full=gen_ai_data()
        sd_=datetime.combine(aif,datetime.min.time());ed_=datetime.combine(ait,datetime.max.time())
        df=full[(full["ts"]>=sd_)&(full["ts"]<=ed_)&(full["role"].isin(air))&(full["itype"].isin(aiit))&
                (full["exp"].isin(aie))&(full["geo"].isin(aig))&(full["lang"].isin(ail))&(full["outcome"].isin(aio))]

    n_ai=len(df)
    st.markdown("---")
    st.caption(f"{n_ai:,} interviews analyzed  ·  {aif.strftime('%b %d, %Y')} – {ait.strftime('%b %d, %Y')}")
    if n_ai==0:st.error("No data for selected filters.");st.stop()

    # ── 3 Tabs ──
    tab1,tab2,tab3=st.tabs(["AI Interview Quality","Impact Ratio Study","Perturbation Study"])

    # ═══════════════════════════
    # TAB 1: INTERVIEW QUALITY
    # ═══════════════════════════
    with tab1:
        bd=st.selectbox("Breakdown",["Overall","Role","Interview Type","Experience","Geography"],key="ai_bd")
        seg_map_={"Overall":None,"Role":"role","Interview Type":"itype","Experience":"exp","Geography":"geo"}
        sc=seg_map_[bd]

        # Table 1: Interview Conduct
        st.markdown('<div class="st_">Interview Conduct Quality</div>',unsafe_allow_html=True)
        if sc:
            grps=df.groupby(sc)
        else:
            grps=[("Overall",df)]
        t1_rows=[]
        for name,g in grps:
            cov=g["coverage"].mean();cla=g["clarity"].mean();rr=g["resume_rel"].mean();comp=g["compliance"].mean()
            overall=(cov+cla+rr+comp)/4
            t1_rows.append({"Segment":name,"# Interviews":len(g),
                "Interview Completeness":f"{color_val(cov)} {cov:.2f}","Question Quality":f"{color_val(cla)} {cla:.2f}",
                "Candidate Relevance":f"{color_val(rr)} {rr:.2f}","Safety Compliance":f"{color_val(comp)} {comp:.2f}",
                "Overall":f"{color_val(overall)} {overall:.2f}","_cov":cov,"_comp":comp})
        t1=pd.DataFrame(t1_rows)
        st.dataframe(t1[["Segment","# Interviews","Interview Completeness","Question Quality","Candidate Relevance","Safety Compliance","Overall"]],use_container_width=True,hide_index=True)

        # Alerts for Table 1
        for _,r in t1.iterrows():
            if r["_cov"]<0.75:st.error(f"🚨 **{r['Segment']}** — Interview completeness is low ({r['_cov']:.2f}). Interviews may be incomplete.")
            if r["_comp"]<0.90:st.error(f"🚨 **{r['Segment']}** — Safety compliance is low ({r['_comp']:.2f}). Potential legal risk. Contact AI Engineering.")

        # Table 2: Feedback Quality
        st.markdown('<div class="st_">Feedback Quality</div>',unsafe_allow_html=True)
        t2_rows=[]
        for name,g in (df.groupby(sc) if sc else [("Overall",df)]):
            acc=g["accuracy"].mean();cmp=g["completeness"].mean();ev=g["evidence"].mean()
            overall2=(acc+cmp+ev)/3
            t2_rows.append({"Segment":name,"# Interviews":len(g),
                "Accuracy of Evaluation":f"{color_val(acc)} {acc:.2f}","Completeness of Feedback":f"{color_val(cmp)} {cmp:.2f}",
                "Evidence Support":f"{color_val(ev)} {ev:.2f}","Overall":f"{color_val(overall2)} {overall2:.2f}","_acc":acc})
        t2=pd.DataFrame(t2_rows)
        st.dataframe(t2[["Segment","# Interviews","Accuracy of Evaluation","Completeness of Feedback","Evidence Support","Overall"]],use_container_width=True,hide_index=True)

        for _,r in t2.iterrows():
            if r["_acc"]<0.75:st.error(f"🚨 **{r['Segment']}** — Evaluation accuracy is low ({r['_acc']:.2f}). AI feedback may be unreliable.")

        st.caption("🟢 ≥ 0.90 (Excellent)  ·  🟡 0.75–0.90 (Acceptable)  ·  🔴 < 0.75 (Needs Attention)")

        # Chart: stacked quality metrics
        st.markdown('<div class="st_">Quality Overview</div>',unsafe_allow_html=True)
        metrics_names=["Coverage","Clarity","Resume Rel.","Compliance","Accuracy","Completeness","Evidence"]
        metrics_vals=[df["coverage"].mean(),df["clarity"].mean(),df["resume_rel"].mean(),df["compliance"].mean(),
                      df["accuracy"].mean(),df["completeness"].mean(),df["evidence"].mean()]
        mc=["#0d904f" if v>=0.90 else "#f9ab00" if v>=0.75 else "#ea4335" for v in metrics_vals]
        fig_q=go.Figure(go.Bar(x=metrics_names,y=metrics_vals,marker_color=mc,
            text=[f"{v:.2f}" for v in metrics_vals],textposition="outside",textfont=dict(size=11)))
        fig_q.update_layout(yaxis=dict(range=[0,1.08],gridcolor="#f1f3f4"),height=320,margin=dict(l=40,r=20,t=15,b=60),
            plot_bgcolor="#fff",paper_bgcolor="#fff",font=dict(family="DM Sans",color="#202124",size=12))
        st.plotly_chart(fig_q,use_container_width=True)

    # ═══════════════════════════
    # TAB 2: IMPACT RATIO
    # ═══════════════════════════
    with tab2:
        ai_demo=st.radio("Demographic View",["Gender","Race","Accent"],horizontal=True,key="ai_demo")
        dcol=ai_demo.lower()
        g=df.groupby(dcol).agg(n=("ai_score","size"),avg_score=("ai_score","mean"),n_sel=("outcome",lambda x:(x=="Selected").sum())).reset_index()
        g["sel_rate"]=(g["n_sel"]/g["n"]).round(3)
        baseline=g["sel_rate"].max()
        g["_ir"]=(g["sel_rate"]/baseline).round(3)
        g["Fairness Status"]=g["_ir"].apply(lambda x:"🟢 Fair" if x>=0.80 else "🔴 Potential Bias")
        g["_fail"]=g["_ir"]<0.80

        st.markdown('<div class="st_">Fairness Across Groups</div>',unsafe_allow_html=True)
        disp_ir=g.rename(columns={dcol:"Group","n":"# Candidates","avg_score":"Avg AI Score","sel_rate":"Selection Rate"})
        disp_ir["# Candidates"]=disp_ir["# Candidates"].apply(lambda x:f"{x:,}")
        disp_ir["Avg AI Score"]=disp_ir["Avg AI Score"].apply(lambda x:f"{x:.3f}")
        disp_ir["Selection Rate"]=disp_ir["Selection Rate"].apply(lambda x:f"{x:.3f}")
        st.dataframe(disp_ir[["Group","# Candidates","Avg AI Score","Selection Rate","Fairness Status"]],use_container_width=True,hide_index=True)

        for _,r in g[g["_fail"]].iterrows():
            st.error(f"🚨 **{r[dcol]}** — Potential bias detected. Selection rate significantly lower than baseline. Please review AI interviewer fairness.")

        st.caption("🟢 Fair = Impact Ratio ≥ 0.80  ·  🔴 Potential Bias = IR < 0.80")

        # Chart
        st.markdown('<div class="st_">Selection Rate by Group</div>',unsafe_allow_html=True)
        bc__=["#0d904f" if not f else "#ea4335" for f in g["_fail"]]
        fig_ir=go.Figure(go.Bar(x=g[dcol],y=g["sel_rate"],marker_color=bc__,
            text=[f"{v:.1%}" for v in g["sel_rate"]],textposition="outside",textfont=dict(size=11)))
        fig_ir.update_layout(yaxis=dict(tickformat=".0%",gridcolor="#f1f3f4",range=[0,g["sel_rate"].max()*1.2]),
            height=320,margin=dict(l=50,r=20,t=15,b=60),plot_bgcolor="#fff",paper_bgcolor="#fff",
            font=dict(family="DM Sans",color="#202124",size=12))
        st.plotly_chart(fig_ir,use_container_width=True)

    # ═══════════════════════════
    # TAB 3: PERTURBATION
    # ═══════════════════════════
    with tab3:
        ai_pcat=st.radio("Perturbation Category",["Gender","Race","Accent"],horizontal=True,key="ai_pcat")

        # Stability table (sample of individual records)
        sample=df.sample(n=min(200,len(df)),random_state=42)
        sample["diff"]=(sample["pert_score"]-sample["ai_score"]).round(5)
        sample["abs_diff"]=sample["diff"].abs()
        sample["Stability"]=sample["abs_diff"].apply(lambda x:"🟢 Stable" if x<0.005 else "🟡 Acceptable" if x<0.01 else "🔴 Risk")

        st.markdown('<div class="st_">Stability of Evaluation (Sample)</div>',unsafe_allow_html=True)
        stbl=sample[["role",ai_pcat.lower(),"ai_score","pert_score","diff","Stability"]].copy()
        stbl.columns=["Role","What Changed","Original Score","New Score","Difference","Stability"]
        stbl["Original Score"]=stbl["Original Score"].apply(lambda x:f"{x:.4f}")
        stbl["New Score"]=stbl["New Score"].apply(lambda x:f"{x:.4f}")
        stbl["Difference"]=stbl["Difference"].apply(lambda x:f"{x:.5f}")
        st.dataframe(stbl.head(50),use_container_width=True,hide_index=True)

        # Summary table
        st.markdown('<div class="st_">Summary by Category</div>',unsafe_allow_html=True)
        cats=df[ai_pcat.lower()].unique()
        sum_rows=[]
        for c in sorted(cats):
            cd=df[df[ai_pcat.lower()]==c]
            diffs=(cd["pert_score"]-cd["ai_score"]).abs()
            avg_d=diffs.mean();n_tests=len(cd)
            # Internal: compute t-test for alerts
            from math import erfc,sqrt
            m1,m2=cd["ai_score"].mean(),cd["pert_score"].mean()
            s1,s2=cd["ai_score"].std(ddof=1),cd["pert_score"].std(ddof=1)
            sp2=((n_tests-1)*s1**2+(n_tests-1)*s2**2)/(2*n_tests-2) if n_tests>1 else 0
            t_=abs((m1-m2)/sqrt(sp2*(2/n_tests))) if sp2>0 and n_tests>1 else 0
            p_=float(erfc(t_/sqrt(2))) if t_>0 else 1.0
            pct_diff=abs(m1-m2)/m1*100 if m1>0 else 0
            stab="🟢 Stable" if avg_d<0.005 else "🟡 Acceptable" if avg_d<0.01 else "🔴 Risk"
            alert_=pct_diff>1 or p_<0.05 or t_>2
            sum_rows.append({"Category":c,"# Tests":n_tests,"Avg Difference":f"{avg_d:.5f}","Stability":stab,"_alert":alert_})
        sdf=pd.DataFrame(sum_rows)
        st.dataframe(sdf[["Category","# Tests","Avg Difference","Stability"]],use_container_width=True,hide_index=True)

        for _,r in sdf[sdf["_alert"]].iterrows():
            st.error(f"🚨 **{r['Category']}** — Potential issue detected. Please review AI interviewer stability for this group.")

        st.caption("🟢 Stable (diff < 0.5%)  ·  🟡 Acceptable (0.5–1%)  ·  🔴 Risk (> 1%)")

        # Chart: original vs perturbed
        st.markdown('<div class="st_">Original vs Perturbed Scores</div>',unsafe_allow_html=True)
        comp_data=[]
        for c in sorted(cats):
            cd=df[df[ai_pcat.lower()]==c]
            comp_data.append({"Group":c,"Original":cd["ai_score"].mean(),"Perturbed":cd["pert_score"].mean()})
        comp_df=pd.DataFrame(comp_data)
        fig_p=go.Figure()
        fig_p.add_trace(go.Bar(name="Original",x=comp_df["Group"],y=comp_df["Original"],marker_color="#1a73e8",
            text=[f"{v:.3f}" for v in comp_df["Original"]],textposition="outside"))
        fig_p.add_trace(go.Bar(name="Perturbed",x=comp_df["Group"],y=comp_df["Perturbed"],
            marker_color=["#0d904f" if abs(o-p)<0.005 else "#f9ab00" if abs(o-p)<0.01 else "#ea4335" for o,p in zip(comp_df["Original"],comp_df["Perturbed"])],
            text=[f"{v:.3f}" for v in comp_df["Perturbed"]],textposition="outside"))
        fig_p.update_layout(barmode="group",yaxis=dict(gridcolor="#f1f3f4",
            range=[float(comp_df[["Original","Perturbed"]].min().min())-0.05,float(comp_df[["Original","Perturbed"]].max().max())+0.05]),
            height=340,margin=dict(l=50,r=20,t=15,b=60),plot_bgcolor="#fff",paper_bgcolor="#fff",
            font=dict(family="DM Sans",color="#202124",size=12),legend=dict(orientation="h",y=1.05,x=0.5,xanchor="center"))
        st.plotly_chart(fig_p,use_container_width=True)

    st.markdown("---")

    # ── Downloads ──
    st.markdown('<div class="st_">Downloads</div>',unsafe_allow_html=True)
    def ai_report_pdf():
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
        from reportlab.lib.colors import HexColor
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,HRFlowable
        buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
        sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr__=HexColor("#5f6368");lt=HexColor("#f8f9fa")
        ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
        h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
        bd_=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
        bu=ParagraphStyle("Bu",parent=bd_,leftIndent=18,bulletIndent=6,spaceAfter=4)
        s=[Spacer(1,20),Paragraph("AI Interviewer — Quality Report",ti),
           HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14)]
        s.append(Paragraph(f"Period: {aif} to {ait}. Interviews: {n_ai:,}.",bd_))
        s.append(Paragraph("1. Interview Conduct Quality",h1))
        s.append(Paragraph(f"Average completeness: {df['coverage'].mean():.2f}. Question quality: {df['clarity'].mean():.2f}. Candidate relevance: {df['resume_rel'].mean():.2f}. Safety compliance: {df['compliance'].mean():.2f}.",bd_))
        s.append(Paragraph("2. Feedback Quality",h1))
        s.append(Paragraph(f"Evaluation accuracy: {df['accuracy'].mean():.2f}. Completeness: {df['completeness'].mean():.2f}. Evidence support: {df['evidence'].mean():.2f}.",bd_))
        s.append(Paragraph("3. Fairness (Impact Ratio)",h1))
        for dcol_ in ["gender","race","accent"]:
            g_=df.groupby(dcol_).agg(n=("ai_score","size"),ns=("outcome",lambda x:(x=="Selected").sum())).reset_index()
            g_["sr"]=(g_["ns"]/g_["n"]);ref_=g_["sr"].max();g_["ir_"]=(g_["sr"]/ref_)
            fails_=g_[g_["ir_"]<0.80]
            if len(fails_)>0:
                for __,f_ in fails_.iterrows():
                    s.append(Paragraph(f"&bull; <b>{f_[dcol_]}</b> ({dcol_.title()}): potential bias (IR={f_['ir_']:.3f})",bu,bulletText=""))
            else:
                s.append(Paragraph(f"&bull; {dcol_.title()}: all groups fair.",bu,bulletText=""))
        s.append(Paragraph("4. Perturbation Stability",h1))
        avg_diff_=abs(df["pert_score"]-df["ai_score"]).mean()
        s.append(Paragraph(f"Average score difference: {avg_diff_:.5f}. {'Stable overall.' if avg_diff_<0.005 else 'Some instability detected.'}",bd_))
        doc.build(s);buf.seek(0);return buf.getvalue()

    def ai_method_pdf():
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
        from reportlab.lib.colors import HexColor
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,HRFlowable
        buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
        sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr__=HexColor("#5f6368");lt=HexColor("#f8f9fa")
        ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
        h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
        bd_=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
        bu=ParagraphStyle("Bu",parent=bd_,leftIndent=18,bulletIndent=6,spaceAfter=4)
        s=[Spacer(1,20),Paragraph("AI Interviewer — Methodology",ti),
           HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14)]
        s.append(Paragraph("1. Interview Conduct Metrics",h1))
        for m,d in [("Interview Completeness","Measures whether the AI covered all required interview sections."),
                     ("Question Quality","Assesses clarity and relevance of questions asked."),
                     ("Candidate Relevance","Checks if questions align with the candidate's resume and experience."),
                     ("Safety Compliance","Monitors for policy violations, inappropriate content, and jailbreak attempts.")]:
            s.append(Paragraph(f"<b>{m}</b> — {d}",bu,bulletText="\u2022"))
        s.append(Paragraph("2. Feedback Quality Metrics",h1))
        for m,d in [("Accuracy of Evaluation","Is the AI's assessment factually correct?"),
                     ("Completeness of Feedback","Does the feedback cover all evaluated areas?"),
                     ("Evidence Support","Are assessments backed by specific candidate responses?")]:
            s.append(Paragraph(f"<b>{m}</b> — {d}",bu,bulletText="\u2022"))
        s.append(Paragraph("3. Scoring",h1))
        s.append(Paragraph("\u2265 0.90 = Excellent (Green). 0.75-0.90 = Acceptable (Yellow). &lt; 0.75 = Needs Attention (Red).",bd_))
        s.append(Paragraph("4. Impact Ratio (Fairness)",h1))
        s.append(Paragraph("Selection rates are compared across demographic groups. Impact Ratio = group rate / highest rate. IR &lt; 0.80 indicates potential bias per the 4/5ths rule.",bd_))
        s.append(Paragraph("5. Perturbation (Stability)",h1))
        s.append(Paragraph("Each interview is re-evaluated with a small change to a protected characteristic. If the AI score changes significantly, it indicates the system is sensitive to that attribute.",bd_))
        s.append(Paragraph("Internally, statistical tests (T-test, p-value) determine significance. These are not shown to the user. Instead, results are presented as Stable/Acceptable/Risk.",bd_))
        td_=[["Difference","Stability"],["< 0.5%","\u2265 Stable"],["0.5-1%","Acceptable"],["> 1%","Risk"]]
        t_=Table(td_,colWidths=[80,150])
        t_.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9.5),
            ("ALIGN",(0,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
        s.append(t_)
        doc.build(s);buf.seek(0);return buf.getvalue()

    d1,d2=st.columns(2)
    with d1:
        with st.spinner("Generating report…"):rp_=ai_report_pdf()
        st.download_button("⬇ Download Report (PDF)",rp_,file_name="ai_interview_report.pdf",mime="application/pdf",use_container_width=True,key="aid1")
    with d2:
        with st.spinner("Generating methodology…"):mt_=ai_method_pdf()
        st.download_button("⬇ Download Methodology (PDF)",mt_,file_name="ai_interview_methodology.pdf",mime="application/pdf",use_container_width=True,key="aid2")

    with st.expander("How AI Interview Quality is Measured"):
        st.markdown("""
**Interview Conduct** — Evaluates completeness, question quality, candidate relevance, and safety compliance of each AI interview.

**Feedback Quality** — Assesses whether the AI's evaluation is accurate, complete, and backed by evidence from candidate responses.

**Fairness (Impact Ratio)** — Compares selection rates across gender, race, and accent groups. IR < 0.80 = potential bias.

**Stability (Perturbation)** — Tests whether small changes to protected characteristics change the AI's score. Stable = scores don't change. Risk = significant change detected.

**Scoring:** 🟢 ≥ 0.90 Excellent · 🟡 0.75–0.90 Acceptable · 🔴 < 0.75 Needs Attention
""")
    st.stop()

# ████████████████████████████████████████████████████
# █  RECOMMENDATION QUALITY                            █
# ████████████████████████████████████████████████████
elif page=="Recommendation Quality":
    st.markdown('<div class="pt">Recommendation Quality</div>',unsafe_allow_html=True)

    RQ_TYPES=["Jobs","Courses","Projects","Project Leads"]
    RQ_JOBS=["Engineering","Sales","Operations","Marketing","Finance"]
    RQ_EXPS=["Entry","Mid","Senior"]
    RQ_GEOS=["US","India","Europe"]
    RQ_LABELS=["Highly Relevant","Relevant","Somewhat Relevant","Irrelevant"]

    # Probability distributions per dimension (realistic, not random)
    JOB_PROBS={
        "Engineering":[0.35,0.42,0.15,0.08],"Finance":[0.30,0.40,0.18,0.12],
        "Operations":[0.28,0.38,0.22,0.12],"Marketing":[0.25,0.35,0.25,0.15],
        "Sales":[0.20,0.30,0.28,0.22],
    }
    EXP_ADJ_={"Entry":[-0.05,-0.03,0.04,0.04],"Mid":[0.05,0.03,-0.04,-0.04],"Senior":[-0.02,-0.02,0.02,0.02]}
    GEO_ADJ_={"US":[0.03,0.02,-0.02,-0.03],"India":[-0.02,0.0,0.01,0.01],"Europe":[0.0,0.01,-0.01,0.0]}
    TYPE_ADJ={"Jobs":[0.02,0.01,-0.01,-0.02],"Courses":[-0.02,0.02,0.01,-0.01],"Projects":[0.0,0.0,0.0,0.0],"Project Leads":[-0.03,-0.01,0.02,0.02]}

    @st.cache_data
    def gen_rq_data(seed=55):
        rng=np.random.default_rng(seed)
        n=55000;recs=[]
        for i in range(n):
            rt=rng.choice(RQ_TYPES)
            jc=rng.choice(RQ_JOBS)
            el=rng.choice(RQ_EXPS)
            geo=rng.choice(RQ_GEOS)
            # Compute label probabilities
            base=np.array(JOB_PROBS[jc],dtype=float)
            base+=np.array(EXP_ADJ_.get(el,[0,0,0,0]),dtype=float)
            base+=np.array(GEO_ADJ_.get(geo,[0,0,0,0]),dtype=float)
            base+=np.array(TYPE_ADJ.get(rt,[0,0,0,0]),dtype=float)
            base=np.clip(base,0.02,0.95)
            base/=base.sum()
            label=rng.choice(RQ_LABELS,p=base)
            ts=datetime(2024,1,1)+timedelta(days=int(rng.integers(0,730)))
            recs.append({"type":rt,"jc":jc,"el":el,"geo":geo,"ts":ts,"label":label})
        return pd.DataFrame(recs)

    def compute_rq_metrics(df,segment_col=None):
        if segment_col:
            groups=df.groupby(segment_col)
        else:
            groups=[("Overall",df)]
        rows=[]
        for name,grp in groups:
            n=len(grp)
            if n==0:continue
            pcts={}
            for lb in RQ_LABELS:
                pcts[lb]=round((grp["label"]==lb).mean()*100,1)
            qs=round((pcts["Highly Relevant"]/100*1.0+pcts["Relevant"]/100*0.75+pcts["Somewhat Relevant"]/100*0.4+pcts["Irrelevant"]/100*0.0),3)
            if qs>=0.80:cat="Highly Relevant"
            elif qs>=0.65:cat="Relevant"
            elif qs>=0.45:cat="Somewhat Relevant"
            else:cat="Irrelevant"
            alert=(pcts["Irrelevant"]>=15)or(qs<0.50)or(pcts["Highly Relevant"]<=20)
            rows.append({"Segment":name,"N":n,"Highly Relevant %":pcts["Highly Relevant"],"Relevant %":pcts["Relevant"],
                "Somewhat Relevant %":pcts["Somewhat Relevant"],"Irrelevant %":pcts["Irrelevant"],
                "Quality Score":qs,"Category":cat,"_alert":alert})
        return pd.DataFrame(rows)

    def cat_color(cat):
        if cat=="Highly Relevant":return "#0d904f"
        if cat=="Relevant":return "#34a853"
        if cat=="Somewhat Relevant":return "#f9ab00"
        return "#ea4335"

    def cat_emoji(cat):
        if cat=="Highly Relevant":return "🟢"
        if cat=="Relevant":return "🟡"
        if cat=="Somewhat Relevant":return "🟠"
        return "🔴"

    # Filters
    st.markdown('<div class="st_">Filters</div>',unsafe_allow_html=True)
    today=datetime.today().date()
    rc1,rc2,rc3,rc4=st.columns(4)
    with rc1:
        st.markdown('<div class="fl">From</div>',unsafe_allow_html=True)
        rqf=st.date_input("x",value=today-timedelta(days=180),max_value=today,label_visibility="collapsed",key="rqf")
    with rc2:
        st.markdown('<div class="fl">To</div>',unsafe_allow_html=True)
        rqt=st.date_input("x",value=today,max_value=today,label_visibility="collapsed",key="rqt")
    with rc3:
        st.markdown('<div class="fl">Recommendation Type</div>',unsafe_allow_html=True)
        rqtype=st.multiselect("x",RQ_TYPES,default=None,placeholder="All",label_visibility="collapsed",key="rqtype")
        rqtype=rqtype or RQ_TYPES
    with rc4:
        st.markdown('<div class="fl">Job Category</div>',unsafe_allow_html=True)
        rqjc=st.multiselect("x",RQ_JOBS,default=None,placeholder="All",label_visibility="collapsed",key="rqjc")
        rqjc=rqjc or RQ_JOBS
    rc5,rc6,rc7,_=st.columns(4)
    with rc5:
        st.markdown('<div class="fl">Experience Level</div>',unsafe_allow_html=True)
        rqel=st.multiselect("x",RQ_EXPS,default=None,placeholder="All",label_visibility="collapsed",key="rqel")
        rqel=rqel or RQ_EXPS
    with rc6:
        st.markdown('<div class="fl">Geography</div>',unsafe_allow_html=True)
        rqgeo=st.multiselect("x",RQ_GEOS,default=None,placeholder="All",label_visibility="collapsed",key="rqgeo")
        rqgeo=rqgeo or RQ_GEOS
    with rc7:
        st.markdown('<div class="fl">Breakdown By</div>',unsafe_allow_html=True)
        rqbd=st.selectbox("x",["Overall","Job Category","Experience","Geography"],label_visibility="collapsed",key="rqbd")

    if not(rqf and rqt and rqf<=rqt):
        st.warning("Please select a valid time range.");st.stop()

    st.markdown("")
    if st.button("Check Recommendation Quality",type="primary",key="rq_go"):
        st.session_state["rq_ok"]=True
    if not st.session_state.get("rq_ok"):
        st.caption("Configure filters and click Check Recommendation Quality.");st.stop()

    # Generate and filter
    with st.spinner("Analyzing recommendation quality…"):
        full_df=gen_rq_data()
        sd=datetime.combine(rqf,datetime.min.time());ed=datetime.combine(rqt,datetime.max.time())
        fdf=full_df[(full_df["ts"]>=sd)&(full_df["ts"]<=ed)&(full_df["type"].isin(rqtype))&(full_df["jc"].isin(rqjc))&(full_df["el"].isin(rqel))&(full_df["geo"].isin(rqgeo))]

    n_recs=len(fdf)
    st.markdown("---")
    st.caption(f"{n_recs:,} recommendations analyzed  ·  {rqf.strftime('%b %d, %Y')} – {rqt.strftime('%b %d, %Y')}")

    if n_recs==0:
        st.error("No recommendations found for the selected filters.");st.stop()

    # Determine segment column
    seg_map={"Overall":None,"Job Category":"jc","Experience":"el","Geography":"geo"}
    seg_col=seg_map[rqbd]

    # Show results per recommendation type
    types_to_show=rqtype if len(rqtype)>1 else rqtype

    for rtype in types_to_show:
        type_df=fdf[fdf["type"]==rtype]
        if len(type_df)==0:continue
        st.markdown(f'<div class="st_">{rtype} Recommendations</div>',unsafe_allow_html=True)

        metrics=compute_rq_metrics(type_df,seg_col)
        # Format display
        disp=metrics.drop(columns=["_alert"]).copy()
        disp["Quality Score"]=disp["Quality Score"].apply(lambda x:f"{x:.3f}")
        disp["Category"]=metrics.apply(lambda r:f"{cat_emoji(r['Category'])} {r['Category']}",axis=1)
        disp["N"]=disp["N"].apply(lambda x:f"{x:,}")
        st.dataframe(disp,use_container_width=True,hide_index=True)

        # Alerts
        for _,r in metrics[metrics["_alert"]].iterrows():
            st.error(f"🚨 **{r['Segment']}** — Recommendation quality is poor (Quality Score: {r['Quality Score']:.3f}, Irrelevant: {r['Irrelevant %']}%). Please contact the AI Engineering team immediately.")

    st.caption("🟢 Highly Relevant  ·  🟡 Relevant  ·  🟠 Somewhat Relevant  ·  🔴 Irrelevant")
    st.markdown("---")

    # ── Stacked distribution chart ──
    st.markdown('<div class="st_">Quality Distribution</div>',unsafe_allow_html=True)
    chart_type=st.radio("Chart by",["Recommendation Type","Breakdown"],horizontal=True,key="rq_chart")

    if chart_type=="Recommendation Type":
        chart_data=[]
        for rt in types_to_show:
            td=fdf[fdf["type"]==rt]
            if len(td)==0:continue
            for lb in RQ_LABELS:
                chart_data.append({"Group":rt,"Label":lb,"Pct":round((td["label"]==lb).mean()*100,1)})
        cdf=pd.DataFrame(chart_data)
    else:
        if seg_col:
            chart_data=[]
            for seg in fdf[seg_col].unique():
                td=fdf[fdf[seg_col]==seg]
                for lb in RQ_LABELS:
                    chart_data.append({"Group":seg,"Label":lb,"Pct":round((td["label"]==lb).mean()*100,1)})
            cdf=pd.DataFrame(chart_data)
        else:
            chart_data=[]
            for lb in RQ_LABELS:
                chart_data.append({"Group":"Overall","Label":lb,"Pct":round((fdf["label"]==lb).mean()*100,1)})
            cdf=pd.DataFrame(chart_data)

    if len(cdf)>0:
        colors={"Highly Relevant":"#0d904f","Relevant":"#34a853","Somewhat Relevant":"#f9ab00","Irrelevant":"#ea4335"}
        fig=go.Figure()
        for lb in RQ_LABELS:
            ld=cdf[cdf["Label"]==lb]
            fig.add_trace(go.Bar(name=lb,x=ld["Group"],y=ld["Pct"],marker_color=colors[lb],
                text=[f"{v:.1f}%" for v in ld["Pct"]],textposition="inside",textfont=dict(size=10,color="#fff")))
        fig.update_layout(barmode="stack",yaxis=dict(title="Distribution %",gridcolor="#f1f3f4",range=[0,105]),
            height=350,margin=dict(l=50,r=20,t=15,b=60),plot_bgcolor="#fff",paper_bgcolor="#fff",
            font=dict(family="DM Sans",color="#202124",size=12),
            legend=dict(orientation="h",y=1.08,x=0.5,xanchor="center"))
        st.plotly_chart(fig,use_container_width=True)
    st.markdown("---")

    # ── Downloads ──
    st.markdown('<div class="st_">Downloads</div>',unsafe_allow_html=True)
    d1,d2=st.columns(2)
    with d1:
        st.download_button("⬇ Download Results (CSV)",fdf.to_csv(index=False).encode(),file_name="rq_results.csv",mime="text/csv",use_container_width=True,key="rqd1")
    with d2:
        def rq_method_pdf():
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
            from reportlab.lib.colors import HexColor
            from reportlab.lib.units import mm
            from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,HRFlowable
            buf=BytesIO();doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=25*mm,rightMargin=25*mm,topMargin=25*mm,bottomMargin=20*mm)
            sty=getSampleStyleSheet();bl=HexColor("#1a73e8");dk=HexColor("#202124");gr_=HexColor("#5f6368");lt=HexColor("#f8f9fa")
            ti=ParagraphStyle("T",parent=sty["Title"],fontSize=20,textColor=dk,spaceAfter=4)
            h1=ParagraphStyle("H1",parent=sty["Heading1"],fontSize=14,textColor=bl,spaceBefore=18,spaceAfter=8)
            bd=ParagraphStyle("B",parent=sty["Normal"],fontSize=10,textColor=dk,leading=15,spaceAfter=8)
            bu=ParagraphStyle("Bu",parent=bd,leftIndent=18,bulletIndent=6,spaceAfter=4)
            s=[Spacer(1,20),Paragraph("Recommendation Quality — Methodology",ti),
               HRFlowable(width="100%",thickness=1,color=bl,spaceAfter=14)]
            s.append(Paragraph("1. Evaluation Categories",h1))
            s.append(Paragraph("Each recommendation is evaluated using LLM-based assessment into exactly 4 categories:",bd))
            for c,d in [("Highly Relevant","The recommendation is an excellent match for the user's profile and intent."),
                        ("Relevant","The recommendation is a good match with minor gaps."),
                        ("Somewhat Relevant","The recommendation has partial relevance but significant gaps."),
                        ("Irrelevant","The recommendation does not match the user's profile or intent.")]:
                s.append(Paragraph(f"<b>{c}</b> — {d}",bu,bulletText="\u2022"))
            s.append(Paragraph("2. Quality Score",h1))
            s.append(Paragraph("A weighted quality score is computed: QS = 1.0×HR + 0.75×R + 0.4×SR + 0.0×IR",bd))
            td=[["Score Range","Category"],["\u2265 0.80","Highly Relevant"],["\u2265 0.65","Relevant"],["\u2265 0.45","Somewhat Relevant"],["< 0.45","Irrelevant"]]
            t=Table(td,colWidths=[100,150])
            t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),bl),("TEXTCOLOR",(0,0),(-1,0),HexColor("#fff")),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9.5),("ALIGN",(0,0),(-1,-1),"CENTER"),("GRID",(0,0),(-1,-1),0.5,HexColor("#e0e0e0")),("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#fff"),lt]),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
            s.append(t);s.append(Spacer(1,8))
            s.append(Paragraph("3. Alert Thresholds",h1))
            s.append(Paragraph("Alerts trigger when: Irrelevant \u2265 15%, OR Quality Score < 0.50, OR Highly Relevant \u2264 20%.",bd))
            s.append(Paragraph("4. Factors Affecting Quality",h1))
            s.append(Paragraph("<b>Job Category</b> — Engineering typically has higher relevance; Sales may show lower quality.",bu,bulletText="\u2022"))
            s.append(Paragraph("<b>Experience Level</b> — Mid-level candidates receive best-matched recommendations. Entry-level is noisier.",bu,bulletText="\u2022"))
            s.append(Paragraph("<b>Geography</b> — US recommendations tend to be higher quality due to richer training data.",bu,bulletText="\u2022"))
            s.append(Paragraph("<b>Recommendation Type</b> — Jobs and Courses may differ in relevance patterns from Projects.",bu,bulletText="\u2022"))
            doc.build(s);buf.seek(0);return buf.getvalue()
        with st.spinner("Generating methodology…"):mth=rq_method_pdf()
        st.download_button("⬇ Download Methodology (PDF)",mth,file_name="rq_methodology.pdf",mime="application/pdf",use_container_width=True,key="rqd2")

    with st.expander("How Recommendation Quality is Measured"):
        st.markdown("""
**4 Evaluation Categories** — Each recommendation is assessed as Highly Relevant, Relevant, Somewhat Relevant, or Irrelevant using LLM-based evaluation.

**Quality Score** = 1.0 × %Highly Relevant + 0.75 × %Relevant + 0.4 × %Somewhat Relevant + 0.0 × %Irrelevant

**Category Mapping** — QS ≥0.80 = Highly Relevant, ≥0.65 = Relevant, ≥0.45 = Somewhat Relevant, <0.45 = Irrelevant.

**Alerts** trigger when Irrelevant ≥15%, Quality Score <0.50, or Highly Relevant ≤20%.
""")
    st.stop()


# ████████████████████████████████████████████████████
# █  PLACEHOLDER                                       █
# ████████████████████████████████████████████████████
else:
    st.markdown(f'<div class="pt">{page}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="dc"><div class="dt">AI Compliance</div><div class="dct">{page}</div><div class="dcd">Under development.</div></div>',unsafe_allow_html=True)
    st.stop()
