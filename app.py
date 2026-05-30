import streamlit as st
import streamlit.components.v1 as components

# 1. Set up the page configuration
st.set_page_config(
    page_title="Live HTML Renderer", 
    page_icon="🌐", 
    layout="wide"
)

st.title("🌐 Live HTML Renderer")
st.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<title>Kisan Ka Pakistan — Smart Farming</title>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"/>
<style>
:root{
  --gp:#1a7a3e;--gl:#2ecc71;--gpal:#e8f8ee;--gm:#27ae60;
  --sky:#0ea5e9;--skyl:#e0f2fe;
  --gold:#f59e0b;--goldl:#fef3c7;
  --red:#ef4444;--redl:#fee2e2;
  --pur:#7c3aed;--purl:#ede9fe;
  --surf:#f0f7f3;--surf2:#fff;
  --glass:rgba(255,255,255,.92);
  --bdr:rgba(26,122,62,.13);
  --sh:0 8px 32px rgba(26,122,62,.14);
  --sh2:0 20px 60px rgba(26,122,62,.18);
  --tp:#0d2e1a;--ts:#4a7c59;--tm:#8db09a;
  --r:16px;--rs:10px;--rl:24px;
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
html,body{font-family:'Sora',sans-serif;background:var(--surf);color:var(--tp);overflow-x:hidden;min-height:100vh;}
.mono{font-family:'JetBrains Mono',monospace;}

/* SPLASH */
#splash{position:fixed;inset:0;z-index:9999;background:linear-gradient(135deg,#0d2e1a,#1a7a3e 50%,#0ea5e9);display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .8s;}
#splash.gone{opacity:0;pointer-events:none;}
.spl-icon{width:96px;height:96px;background:rgba(255,255,255,.12);border-radius:26px;display:flex;align-items:center;justify-content:center;font-size:52px;margin-bottom:20px;animation:splPulse 1.8s ease-in-out infinite;box-shadow:0 0 60px rgba(46,204,113,.4);}
@keyframes splPulse{0%,100%{transform:scale(1);box-shadow:0 0 40px rgba(46,204,113,.3);}50%{transform:scale(1.07);box-shadow:0 0 80px rgba(46,204,113,.6);}}
.spl-title{color:#fff;font-size:28px;font-weight:800;letter-spacing:-.5px;}
.spl-sub{color:rgba(255,255,255,.7);font-size:14px;margin-top:6px;}
.spl-bar{width:220px;height:4px;background:rgba(255,255,255,.2);border-radius:99px;margin-top:40px;overflow:hidden;}
.spl-fill{height:100%;background:linear-gradient(90deg,#2ecc71,#0ea5e9);border-radius:99px;animation:sLoad 2.4s ease forwards;}
@keyframes sLoad{from{width:0}to{width:100%}}

/* AUTH */
#authScreen{display:none;min-height:100vh;background:linear-gradient(160deg,#e8f8ee,#e0f2fe 50%,#fdf3eb);}
.auth-wrap{max-width:480px;margin:0 auto;padding:36px 20px 60px;}
.auth-brand{display:flex;align-items:center;gap:12px;margin-bottom:28px;}
.auth-brand-icon{width:52px;height:52px;background:linear-gradient(135deg,#1a7a3e,#27ae60);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:28px;box-shadow:var(--sh);}
.auth-card{background:var(--glass);backdrop-filter:blur(20px);border-radius:var(--rl);padding:28px;border:1px solid var(--bdr);box-shadow:var(--sh2);}
.tabs{display:flex;gap:4px;background:var(--surf);border-radius:12px;padding:4px;margin-bottom:24px;}
.tab{flex:1;padding:10px;text-align:center;border-radius:9px;font-size:14px;font-weight:600;cursor:pointer;transition:.2s;color:var(--ts);}
.tab.on{background:#fff;color:var(--gp);box-shadow:0 2px 8px rgba(26,122,62,.08);}
.lang-row{display:flex;gap:8px;margin-bottom:16px;}
.lang-btn{flex:1;padding:10px;border-radius:10px;border:1.5px solid var(--bdr);background:#fff;font-size:13px;font-weight:600;cursor:pointer;transition:.2s;color:var(--ts);}
.lang-btn.on{border-color:var(--gp);background:var(--gpal);color:var(--gp);}
.fg{margin-bottom:14px;}
.fg2{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.fg2 .fg{margin-bottom:0;}
label{display:block;font-size:11px;font-weight:700;color:var(--ts);margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px;}
input,select,textarea{width:100%;padding:12px 14px;border:1.5px solid var(--bdr);border-radius:11px;font-family:'Sora',sans-serif;font-size:14px;background:#fff;color:var(--tp);outline:none;transition:.2s;appearance:none;}
input:focus,select:focus,textarea:focus{border-color:var(--gp);box-shadow:0 0 0 3px rgba(26,122,62,.1);}
input.err{border-color:var(--red)!important;background:#fff8f8;}
.err-msg{color:var(--red);font-size:11px;font-weight:600;margin-top:4px;display:none;}
.err-msg.show{display:block;}
.btn{width:100%;padding:14px;border-radius:12px;font-family:'Sora',sans-serif;font-size:15px;font-weight:700;cursor:pointer;border:none;transition:.25s;display:flex;align-items:center;justify-content:center;gap:8px;}
.btn-g{background:linear-gradient(135deg,#1a7a3e,#27ae60);color:#fff;box-shadow:0 4px 20px rgba(26,122,62,.35);}
.btn-g:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(26,122,62,.45);}
.btn-sm{width:auto;padding:9px 16px;font-size:13px;border-radius:9px;}
.btn-out{background:transparent;border:1.5px solid var(--bdr);color:var(--ts);}
.otp-row{display:flex;gap:8px;margin-bottom:16px;}
.otp-i{flex:1;padding:14px 0;text-align:center;font-size:22px;font-weight:800;border:1.5px solid var(--bdr);border-radius:11px;background:#fff;color:var(--gp);font-family:'JetBrains Mono',monospace;outline:none;transition:.2s;}
.otp-i:focus{border-color:var(--gp);box-shadow:0 0 0 3px rgba(26,122,62,.1);}
.link{color:var(--gp);font-weight:600;cursor:pointer;}

/* APP */
#app{display:none;min-height:100vh;padding-bottom:76px;}
.topbar{position:sticky;top:0;z-index:100;background:var(--glass);backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);padding:12px 16px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 2px 8px rgba(26,122,62,.06);}
.menu-btn,.notif-btn{width:40px;height:40px;border-radius:10px;background:var(--gpal);border:none;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;position:relative;}
.ndot{position:absolute;top:8px;right:8px;width:7px;height:7px;background:var(--red);border-radius:50%;border:2px solid #fff;}
.av{width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,#1a7a3e,#27ae60);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:800;cursor:pointer;}
.sov{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:200;opacity:0;pointer-events:none;transition:opacity .3s;backdrop-filter:blur(4px);}
.sov.on{opacity:1;pointer-events:all;}
.sidebar{position:fixed;left:0;top:0;bottom:0;width:276px;background:#fff;z-index:201;transform:translateX(-100%);transition:transform .35s cubic-bezier(.4,0,.2,1);overflow-y:auto;}
.sidebar.on{transform:translateX(0);}
.sb-hd{background:linear-gradient(135deg,#0d2e1a,#1a7a3e);padding:28px 20px 22px;color:#fff;}
.sb-farm{background:rgba(255,255,255,.12);border-radius:9px;padding:9px 12px;margin-top:14px;font-size:12px;}
.nsec{padding:8px 16px 4px;font-size:10px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:.7px;}
.ni{display:flex;align-items:center;gap:13px;padding:12px 18px;cursor:pointer;font-size:14px;font-weight:500;color:var(--ts);transition:.15s;position:relative;}
.ni:hover,.ni.on{background:var(--gpal);color:var(--gp);}
.ni.on::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:3px;height:60%;background:var(--gp);border-radius:0 3px 3px 0;}
.ni-ico{font-size:20px;width:24px;text-align:center;}
.nbadge{margin-left:auto;background:var(--red);color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:99px;}
.bnav{position:fixed;bottom:0;left:0;right:0;background:var(--glass);backdrop-filter:blur(20px);border-top:1px solid var(--bdr);display:flex;z-index:100;padding:5px 0 calc(5px + env(safe-area-inset-bottom));}
.bni{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;padding:7px 4px;cursor:pointer;color:var(--tm);font-size:10px;font-weight:600;transition:.15s;}
.bni.on{color:var(--gp);}
.bni-ico{font-size:22px;transition:transform .15s;}
.bni.on .bni-ico{transform:scale(1.12);}
.page{display:none;padding:18px 16px;animation:fadeIn .3s ease;}
.page.on{display:block;}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}

/* Cards / UI */
.card{background:#fff;border-radius:var(--r);border:1px solid var(--bdr);box-shadow:0 2px 8px rgba(26,122,62,.06);}
.sec-hd{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;}
.sec-t{font-size:16px;font-weight:700;}
.see-all{font-size:13px;font-weight:600;color:var(--gp);cursor:pointer;}
.chip{display:inline-flex;align-items:center;gap:4px;padding:4px 11px;border-radius:99px;font-size:12px;font-weight:600;}
.chip-g{background:var(--gpal);color:var(--gp);}
.chip-s{background:var(--skyl);color:#0369a1;}
.chip-r{background:var(--redl);color:var(--red);}
.chip-gold{background:var(--goldl);color:#92400e;}
.pb{width:100%;height:8px;background:var(--surf);border-radius:99px;overflow:hidden;}
.pf{height:100%;border-radius:99px;transition:width .5s ease;}
.alert{border-radius:var(--rs);padding:11px 14px;display:flex;align-items:center;gap:11px;font-size:13px;font-weight:500;margin-bottom:11px;}
.alert-warn{background:var(--goldl);color:#92400e;border:1px solid rgba(245,158,11,.25);}
.alert-ok{background:var(--gpal);color:var(--gp);border:1px solid rgba(26,122,62,.2);}
.alert-bad{background:var(--redl);color:#991b1b;border:1px solid rgba(239,68,68,.25);}
.live-badge{display:inline-flex;align-items:center;gap:5px;background:var(--redl);color:var(--red);font-size:11px;font-weight:800;padding:4px 11px;border-radius:99px;}
.ldot{width:6px;height:6px;background:var(--red);border-radius:50%;animation:blink 1s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}
.prog-label{display:flex;justify-content:space-between;margin-bottom:6px;font-size:13px;}

/* Dashboard */
.greet-card{background:linear-gradient(135deg,#0d2e1a,#1a7a3e 60%,#2ecc71);border-radius:var(--rl);padding:22px;margin-bottom:18px;position:relative;overflow:hidden;}
.greet-card::before{content:'🌾';position:absolute;right:-8px;bottom:-12px;font-size:90px;opacity:.1;transform:rotate(-12deg);}
.gs-grid{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:18px;}
.gs-card{background:#fff;border-radius:var(--r);padding:15px;border:1px solid var(--bdr);transition:transform .2s;}
.gs-card:hover{transform:translateY(-2px);}
.wcard{background:linear-gradient(135deg,#0ea5e9,#0369a1);border-radius:var(--r);padding:18px;color:#fff;margin-bottom:18px;position:relative;overflow:hidden;}
.wcard::after{content:'⛅';position:absolute;right:16px;top:50%;transform:translateY(-50%);font-size:58px;opacity:.25;}

/* ===== DRONE PAGE ===== */
.drone-page{padding:0;}
.drone-header{background:linear-gradient(135deg,#050e05,#0d2e1a);padding:16px;border-bottom:1px solid rgba(46,204,113,.15);}
.drone-canvas-container{position:relative;background:#050e05;width:100%;}
#droneCanvas{display:block;width:100%;height:320px;cursor:crosshair;}
.drone-hud-overlay{position:absolute;top:10px;left:10px;right:10px;pointer-events:none;}
.hud-row{display:flex;justify-content:space-between;align-items:flex-start;}
.hud-box{background:rgba(0,0,0,.6);backdrop-filter:blur(8px);border:1px solid rgba(46,204,113,.3);border-radius:8px;padding:6px 10px;min-width:70px;}
.hud-val{font-size:16px;font-weight:800;color:#2ecc71;font-family:'JetBrains Mono',monospace;}
.hud-lbl{font-size:9px;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.5px;margin-top:1px;}
.hud-center{text-align:center;}
.hud-status{background:rgba(0,0,0,.6);border:1px solid rgba(46,204,113,.3);border-radius:99px;padding:5px 14px;color:#2ecc71;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;}
.spray-indicator{position:absolute;bottom:10px;left:10px;right:10px;pointer-events:none;}
.spray-bar-bg{background:rgba(0,0,0,.5);border:1px solid rgba(14,165,233,.4);border-radius:99px;height:6px;overflow:hidden;}
.spray-bar-fill{height:100%;background:linear-gradient(90deg,#0ea5e9,#38bdf8);border-radius:99px;transition:width .3s;}

/* JOYSTICK SECTION */
.joy-section{background:#0d1a0d;padding:16px;}
.joy-grid{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:center;}
.joy-wrap{display:flex;flex-direction:column;align-items:center;gap:8px;}
.joy-lbl{font-size:11px;font-weight:700;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.5px;}
.joystick{width:130px;height:130px;border-radius:50%;background:radial-gradient(circle,#1a2a1a,#0d1a0d);border:2px solid rgba(46,204,113,.25);position:relative;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 0 20px rgba(0,0,0,.5),inset 0 0 20px rgba(0,0,0,.4);}
.joystick::before{content:'';position:absolute;inset:10px;border-radius:50%;border:1px solid rgba(46,204,113,.1);}
.joystick::after{content:'';position:absolute;inset:20px;border-radius:50%;border:1px solid rgba(46,204,113,.06);}
.jknob{width:46px;height:46px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#2ecc71,#1a7a3e);box-shadow:0 4px 14px rgba(46,204,113,.5),0 0 0 2px rgba(46,204,113,.2);position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);transition:box-shadow .1s;user-select:none;touch-action:none;}
.jknob:active{box-shadow:0 2px 8px rgba(46,204,113,.4);}
.joy-center-panel{display:flex;flex-direction:column;gap:8px;align-items:center;}

/* SPRAY CONTROLS */
.spray-ctrl{background:#0d1a0d;padding:14px 16px;border-top:1px solid rgba(46,204,113,.1);}
.spray-ctrl-title{color:rgba(255,255,255,.6);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;margin-bottom:12px;}
.spray-btns{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px;}
.sbn{padding:12px 8px;border-radius:10px;border:none;font-family:'Sora',sans-serif;font-size:12px;font-weight:700;cursor:pointer;transition:.2s;display:flex;flex-direction:column;align-items:center;gap:5px;}
.sbn-ico{font-size:20px;}
.sbn.spray-on{background:rgba(14,165,233,.15);border:1.5px solid rgba(14,165,233,.4);color:#38bdf8;}
.sbn.spray-on.active{background:rgba(14,165,233,.3);border-color:#0ea5e9;box-shadow:0 0 14px rgba(14,165,233,.3);}
.sbn.nav{background:rgba(46,204,113,.1);border:1.5px solid rgba(46,204,113,.25);color:#2ecc71;}
.sbn.danger{background:rgba(239,68,68,.1);border:1.5px solid rgba(239,68,68,.25);color:#f87171;}
.sbn.active-nav{background:rgba(46,204,113,.25);border-color:#2ecc71;box-shadow:0 0 12px rgba(46,204,113,.25);}
.spray-rate-row{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.spray-rate-lbl{color:rgba(255,255,255,.6);font-size:12px;font-weight:600;white-space:nowrap;}
.spray-rate-val{color:#38bdf8;font-size:14px;font-weight:800;font-family:'JetBrains Mono',monospace;min-width:40px;text-align:right;}
input[type=range]{-webkit-appearance:none;flex:1;height:5px;border-radius:99px;background:rgba(255,255,255,.1);outline:none;cursor:pointer;}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg,#2ecc71,#1a7a3e);cursor:pointer;box-shadow:0 2px 8px rgba(46,204,113,.4);}
.alt-ctrl-row{display:flex;align-items:center;gap:8px;margin-bottom:10px;}
.alt-btn{padding:8px 16px;border-radius:9px;background:rgba(46,204,113,.1);border:1.5px solid rgba(46,204,113,.25);color:#2ecc71;font-size:14px;font-weight:700;cursor:pointer;transition:.2s;}
.alt-btn:hover{background:rgba(46,204,113,.2);}
.alt-val{flex:1;text-align:center;color:#fff;font-size:16px;font-weight:800;font-family:'JetBrains Mono',monospace;}

/* TELEMETRY BAR */
.tele-bar{background:#000;padding:10px 14px;display:flex;gap:0;overflow-x:auto;border-top:1px solid rgba(46,204,113,.1);}
.tele-item{flex:0 0 auto;padding:0 14px;text-align:center;border-right:1px solid rgba(46,204,113,.1);}
.tele-item:last-child{border-right:none;}
.tv{font-size:15px;font-weight:800;color:#2ecc71;font-family:'JetBrains Mono',monospace;}
.tu{font-size:9px;color:rgba(255,255,255,.4);text-transform:uppercase;}

/* EMRG STOP */
.emrg{width:100%;padding:16px;background:linear-gradient(135deg,#ef4444,#b91c1c);color:#fff;border:none;font-family:'Sora',sans-serif;font-size:15px;font-weight:800;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:10px;transition:.2s;animation:emrgPulse 2s infinite;}
@keyframes emrgPulse{0%,100%{box-shadow:0 0 20px rgba(239,68,68,.4)}50%{box-shadow:0 0 50px rgba(239,68,68,.7)}}
.emrg:active{transform:scale(.98);}

/* SIGNAL BARS */
.sigbars{display:flex;gap:2px;align-items:flex-end;height:14px;}
.sb{width:4px;border-radius:2px;background:#2ecc71;}

/* Other pages */
.map-cont{background:#1a2744;border-radius:var(--rl);overflow:hidden;height:260px;position:relative;margin-bottom:18px;}
.map-inner{width:100%;height:100%;background:linear-gradient(160deg,#1a3a1a,#0d4a2a 40%,#1a4a2a);position:relative;overflow:hidden;}
.mgrid{position:absolute;inset:0;background-image:linear-gradient(rgba(46,204,113,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(46,204,113,.05) 1px,transparent 1px);background-size:36px 36px;}
.field-a{position:absolute;top:50px;left:30px;width:210px;height:130px;border:2.5px solid rgba(46,204,113,.7);border-radius:8px;background:rgba(46,204,113,.1);animation:fpulse 3s infinite;}
@keyframes fpulse{0%,100%{background:rgba(46,204,113,.1)}50%{background:rgba(46,204,113,.18)}}
.mdrn{position:absolute;top:90px;left:130px;animation:mdf 2s ease-in-out infinite;}
@keyframes mdf{0%,100%{transform:translate(0,0)}50%{transform:translate(5px,-4px)}}
.rring{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(46,204,113,.35);animation:rexp 2.5s linear infinite;}
.rring:nth-child(2){animation-delay:.8s}
.rring:nth-child(3){animation-delay:1.6s}
@keyframes rexp{0%{width:16px;height:16px;opacity:1}100%{width:180px;height:180px;opacity:0}}
.price-spark{width:100%;height:50px;}
.exp-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--bdr);}
.exp-item:last-child{border-bottom:none;}
.exp-ico{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;}
.mach-item{background:#fff;border-radius:var(--r);padding:15px;border:1px solid var(--bdr);margin-bottom:11px;transition:transform .2s;}
.mach-item:hover{transform:translateY(-2px);}
.exp-card{background:#fff;border-radius:var(--r);border:1px solid var(--bdr);overflow:hidden;margin-bottom:16px;}
.rec-card{background:#fff;border-radius:var(--r);padding:16px;border:1px solid var(--bdr);margin-bottom:11px;transition:transform .2s;}
.rec-card:hover{transform:translateY(-2px);}
.expert-card{background:#fff;border-radius:var(--r);padding:15px;border:1px solid var(--bdr);margin-bottom:11px;}
.xav{width:50px;height:50px;border-radius:13px;background:linear-gradient(135deg,#1a7a3e,#2ecc71);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;}
.xbtn{flex:1;padding:9px;border-radius:9px;border:none;font-family:'Sora',sans-serif;font-size:12px;font-weight:600;cursor:pointer;transition:.2s;display:flex;align-items:center;justify-content:center;gap:5px;}
.xbtn-c{background:var(--gpal);color:var(--gp);}
.xbtn-v{background:var(--skyl);color:#0369a1;}
.xbtn-m{background:var(--goldl);color:#92400e;}
.profile-hero{background:linear-gradient(135deg,#0d2e1a,#1a7a3e);border-radius:var(--rl);padding:26px;text-align:center;margin-bottom:18px;color:#fff;}
.pav{width:76px;height:76px;border-radius:20px;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;font-size:38px;margin:0 auto 14px;border:3px solid rgba(255,255,255,.25);}
.pro-sec{background:#fff;border-radius:var(--r);border:1px solid var(--bdr);overflow:hidden;margin-bottom:14px;}
.pro-row{display:flex;align-items:center;gap:13px;padding:14px;border-bottom:1px solid var(--bdr);cursor:pointer;}
.pro-row:last-child{border-bottom:none;}
.ai-chat{background:#fff;border-radius:var(--r);border:1px solid var(--bdr);overflow:hidden;margin-bottom:14px;}
.ai-msgs{padding:14px;max-height:320px;overflow-y:auto;display:flex;flex-direction:column;gap:12px;}
.amsg{max-width:85%;padding:11px 14px;border-radius:13px;font-size:14px;line-height:1.5;}
.amsg-b{background:var(--gpal);color:var(--tp);border-radius:4px 13px 13px 13px;align-self:flex-start;}
.amsg-u{background:linear-gradient(135deg,#1a7a3e,#27ae60);color:#fff;border-radius:13px 4px 13px 13px;align-self:flex-end;}
.ai-inp-row{display:flex;gap:9px;padding:11px 14px;border-top:1px solid var(--bdr);}
.ai-inp{flex:1;padding:11px 14px;border:1.5px solid var(--bdr);border-radius:10px;font-family:'Sora',sans-serif;font-size:14px;background:var(--surf);outline:none;width:auto;}
.ai-inp:focus{border-color:var(--gp);}
.asend{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,#1a7a3e,#27ae60);border:none;color:#fff;font-size:17px;cursor:pointer;transition:transform .15s;flex-shrink:0;}
.asend:hover{transform:scale(1.08);}
.weather-hero{background:linear-gradient(135deg,#0369a1,#0ea5e9,#38bdf8);border-radius:var(--rl);padding:26px;text-align:center;color:#fff;margin-bottom:18px;}
.wm-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px;}
.wmet{background:rgba(255,255,255,.15);border-radius:10px;padding:12px 8px;text-align:center;}
.fcast-row{display:flex;gap:9px;overflow-x:auto;padding-bottom:4px;margin-bottom:18px;}
.fday{background:#fff;border-radius:11px;padding:11px 13px;min-width:76px;text-align:center;border:1px solid var(--bdr);}

/* MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:500;display:flex;align-items:center;justify-content:center;padding:16px;opacity:0;pointer-events:none;transition:opacity .3s;backdrop-filter:blur(6px);}
.modal-overlay.on{opacity:1;pointer-events:all;}
.modal{background:#fff;border-radius:var(--rl);padding:24px;width:100%;max-width:480px;max-height:90vh;overflow-y:auto;transform:translateY(20px);transition:transform .3s;}
.modal-overlay.on .modal{transform:translateY(0);}
.modal-hd{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;}
.modal-close{width:36px;height:36px;border-radius:10px;background:var(--surf);border:none;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;}

/* MAP IFRAME */
.map-frame{width:100%;height:280px;border:none;border-radius:var(--rl);overflow:hidden;margin-bottom:18px;}
#googleMap{width:100%;height:280px;border-radius:var(--rl);overflow:hidden;margin-bottom:18px;background:#ddd;position:relative;}
.map-placeholder{width:100%;height:100%;background:linear-gradient(160deg,#1a3a1a,#0d4a2a 40%,#1a4a2a);border-radius:var(--rl);position:relative;overflow:hidden;cursor:pointer;}

/* TOAST */
.toast{position:fixed;bottom:86px;left:50%;transform:translateX(-50%) translateY(20px);background:#0d2e1a;color:#fff;padding:11px 20px;border-radius:11px;font-size:14px;font-weight:600;opacity:0;transition:.3s;z-index:9999;pointer-events:none;white-space:nowrap;max-width:90vw;text-align:center;}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0);}
.loader{position:fixed;inset:0;background:rgba(255,255,255,.88);backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;z-index:9998;opacity:0;pointer-events:none;transition:opacity .3s;}
.loader.on{opacity:1;pointer-events:all;}
.lspin{width:44px;height:44px;border:4px solid var(--gpal);border-top-color:var(--gp);border-radius:50%;animation:spin 1s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}

/* Drone selector */
.drone-list{display:flex;flex-direction:column;gap:10px;margin-bottom:14px;}
.drone-item{background:#0d1a0d;border:1.5px solid rgba(46,204,113,.2);border-radius:12px;padding:12px;display:flex;align-items:center;gap:12px;cursor:pointer;transition:.2s;}
.drone-item.selected{border-color:#2ecc71;background:rgba(46,204,113,.1);}
.drone-ico{font-size:28px;}

/* Settings page */
.setting-row{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--bdr);}
.setting-row:last-child{border-bottom:none;}
.toggle{width:44px;height:24px;background:#ddd;border-radius:99px;position:relative;cursor:pointer;transition:.2s;flex-shrink:0;margin-left:auto;}
.toggle.on{background:var(--gp);}
.toggle::after{content:'';position:absolute;top:3px;left:3px;width:18px;height:18px;border-radius:50%;background:#fff;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.2);}
.toggle.on::after{left:23px;}

/* AI typing indicator */
.typing-dots span{display:inline-block;width:6px;height:6px;background:var(--gp);border-radius:50%;margin:0 2px;animation:dotBounce .8s ease infinite;}
.typing-dots span:nth-child(2){animation-delay:.15s;}
.typing-dots span:nth-child(3){animation-delay:.3s;}
@keyframes dotBounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}

@media(min-width:640px){.gs-grid{grid-template-columns:repeat(4,1fr)}.fg2{grid-template-columns:repeat(2,1fr)}}
</style>
</head>
<body>

<!-- SPLASH -->
<div id="splash">
  <div class="spl-icon">🌾</div>
  <div class="spl-title">Kisan Ka Pakistan</div>
  <div class="spl-sub">Smart Agriculture 🇵🇰</div>
  <div class="spl-bar"><div class="spl-fill"></div></div>
</div>

<!-- AUTH -->
<div id="authScreen">
  <div class="auth-wrap">
    <div class="auth-brand">
      <div class="auth-brand-icon">🌾</div>
      <div>
        <div style="font-size:20px;font-weight:800;color:var(--gp)">Kisan Ka Pakistan</div>
        <div style="font-size:11px;color:var(--ts)">ICT for Smart Agriculture</div>
      </div>
    </div>
    <div class="lang-row">
      <button class="lang-btn on" onclick="setLang('en',this)">🇬🇧 English</button>
      <button class="lang-btn" onclick="setLang('ur',this)">🇵🇰 اردو</button>
    </div>
    <div class="auth-card">
      <div class="tabs">
        <div class="tab on" id="lt" onclick="atab('login')">Login</div>
        <div class="tab" id="rt" onclick="atab('reg')">Sign Up</div>
      </div>

      <!-- LOGIN -->
      <div id="loginF">
        <div class="fg">
          <label>📱 Mobile Number</label>
          <input id="lmob" type="tel" placeholder="03001234567" maxlength="11"/>
          <div class="err-msg" id="lmobErr">Enter valid 11-digit mobile number</div>
        </div>
        <div class="fg">
          <label>🔒 Password</label>
          <input id="lpass" type="password" placeholder="Enter password"/>
          <div class="err-msg" id="lpassErr">Password is required (min 6 characters)</div>
        </div>
        <div style="background:var(--gpal);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:var(--gp);">
          💡 <strong>Demo:</strong> Mobile: <strong>03001234567</strong> | Password: <strong>farmer123</strong>
        </div>
        <button class="btn btn-g" onclick="doLogin()">Login to Farm →</button>
        <p style="text-align:center;margin-top:14px;font-size:13px;color:var(--tm);">No account? <span class="link" onclick="atab('reg')">Register Free</span></p>
      </div>

      <!-- REGISTER -->
      <div id="regF" style="display:none">
        <div class="fg2">
          <div class="fg"><label>Full Name *</label><input id="rname" type="text" placeholder="Ali Hassan"/><div class="err-msg" id="rnameErr">Name required</div></div>
          <div class="fg"><label>Father's Name *</label><input id="rfname" type="text" placeholder="Muhammad Hassan"/><div class="err-msg" id="rfnameErr">Required</div></div>
          <div class="fg"><label>📱 Mobile *</label><input id="rmob" type="tel" placeholder="03001234567" maxlength="11"/><div class="err-msg" id="rmobErr">11-digit mobile required</div></div>
          <div class="fg"><label>🪪 CNIC *</label><input id="rcnic" type="text" placeholder="36302-1234567-1" maxlength="15"/><div class="err-msg" id="rcnicErr">Valid CNIC required</div></div>
          <div class="fg"><label>Province *</label>
            <select id="rprov"><option value="">Select Province</option><option>Punjab</option><option>Sindh</option><option>KPK</option><option>Balochistan</option><option>AJK</option></select>
            <div class="err-msg" id="rprovErr">Select a province</div>
          </div>
          <div class="fg"><label>District *</label><input id="rdist" type="text" placeholder="Multan"/><div class="err-msg" id="rdistErr">District required</div></div>
          <div class="fg"><label>🌾 Farm Acres *</label><input id="racres" type="number" placeholder="12" min="0.5"/><div class="err-msg" id="racresErr">Enter farm area</div></div>
          <div class="fg"><label>Main Crop *</label>
            <select id="rcrop"><option value="">Select Crop</option><option>Wheat</option><option>Cotton</option><option>Rice</option><option>Sugarcane</option><option>Maize</option><option>Vegetables</option></select>
            <div class="err-msg" id="rcropErr">Select main crop</div>
          </div>
          <div class="fg" style="grid-column:1/-1"><label>💧 Irrigation Source *</label>
            <select id="rirr"><option value="">Select Source</option><option>Canal Water</option><option>Tube Well</option><option>Rain-fed</option><option>Drip Irrigation</option></select>
            <div class="err-msg" id="rirrErr">Select irrigation source</div>
          </div>
          <div class="fg"><label>🔒 Password *</label><input id="rpass" type="password" placeholder="Min 6 chars"/><div class="err-msg" id="rpassErr">Min 6 characters</div></div>
          <div class="fg"><label>Confirm Password *</label><input id="rcpass" type="password" placeholder="Repeat password"/><div class="err-msg" id="rcpassErr">Passwords don't match</div></div>
        </div>
        <button class="btn btn-g" onclick="doRegister()">Create Account →</button>
        <p style="text-align:center;margin-top:14px;font-size:13px;color:var(--tm);">Have account? <span class="link" onclick="atab('login')">Login</span></p>
      </div>

      <!-- OTP -->
      <div id="otpF" style="display:none">
        <div style="text-align:center;margin-bottom:22px">
          <div style="font-size:40px;margin-bottom:8px">📲</div>
          <div style="font-size:17px;font-weight:700">Verify Mobile Number</div>
          <div style="font-size:13px;color:var(--tm);margin-top:4px">OTP sent to your mobile</div>
        </div>
        <div class="otp-row">
          <input class="otp-i" id="o1" maxlength="1" oninput="onext(this,2)" onkeydown="oback(event,this,0)"/>
          <input class="otp-i" id="o2" maxlength="1" oninput="onext(this,3)" onkeydown="oback(event,this,1)"/>
          <input class="otp-i" id="o3" maxlength="1" oninput="onext(this,4)" onkeydown="oback(event,this,2)"/>
          <input class="otp-i" id="o4" maxlength="1" oninput="onext(this,5)" onkeydown="oback(event,this,3)"/>
          <input class="otp-i" id="o5" maxlength="1" oninput="onext(this,6)" onkeydown="oback(event,this,4)"/>
          <input class="otp-i" id="o6" maxlength="1" oninput="checkOTP()" onkeydown="oback(event,this,5)"/>
        </div>
        <div style="background:var(--gpal);border-radius:9px;padding:9px 13px;margin-bottom:14px;font-size:12px;color:var(--gp);text-align:center">
          Demo OTP: <strong>1 2 3 4 5 6</strong>
        </div>
        <button class="btn btn-g" id="otpBtn" onclick="enterApp()">Verify & Enter →</button>
      </div>
    </div>
  </div>
</div>

<!-- APP -->
<div id="app">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:11px">
      <button class="menu-btn" onclick="toggleSB()">☰</button>
      <div id="ptitle" style="font-size:16px;font-weight:700">🏡 Dashboard</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="notif-btn" id="notifBtn" onclick="toast('🔔 3 new farm alerts!')">🔔<span class="ndot"></span></button>
      <div class="av" id="userAvatar" onclick="nav('profile')">KP</div>
    </div>
  </div>

  <div class="sov" id="sov" onclick="toggleSB()"></div>
  <div class="sidebar" id="sb">
    <div class="sb-hd">
      <div style="font-size:34px;margin-bottom:8px">🌾</div>
      <div style="font-size:18px;font-weight:700" id="sbName">Kisan</div>
      <div style="font-size:12px;opacity:.75;margin-top:2px" id="sbCnic">CNIC • Province</div>
      <div class="sb-farm" id="sbFarm">📍 Location • Farm Info</div>
    </div>
    <div>
      <div class="nsec">Main</div>
      <div class="ni on" onclick="nav('dashboard');toggleSB()"><span class="ni-ico">🏡</span>Dashboard</div>
      <div class="ni" onclick="nav('drone');toggleSB()"><span class="ni-ico">🚁</span>Drone Control</div>
      <div class="ni" onclick="nav('fields');toggleSB()"><span class="ni-ico">🗺️</span>GPS Field Map</div>
      <div class="ni" onclick="nav('weather');toggleSB()"><span class="ni-ico">🌤️</span>Weather</div>
      <div class="nsec">Farm</div>
      <div class="ni" onclick="nav('ai');toggleSB()"><span class="ni-ico">🤖</span>AI Advisor<span class="nbadge">3</span></div>
      <div class="ni" onclick="nav('resources');toggleSB()"><span class="ni-ico">💰</span>Resources</div>
      <div class="ni" onclick="nav('prices');toggleSB()"><span class="ni-ico">📈</span>Crop Prices</div>
      <div class="nsec">Support</div>
      <div class="ni" onclick="nav('machinery');toggleSB()"><span class="ni-ico">🚜</span>Machinery</div>
      <div class="ni" onclick="nav('experts');toggleSB()"><span class="ni-ico">👨‍🌾</span>Experts</div>
      <div class="ni" onclick="nav('profile');toggleSB()"><span class="ni-ico">👤</span>Profile</div>
      <div class="ni" onclick="nav('settings');toggleSB()"><span class="ni-ico">⚙️</span>Settings</div>
      <div class="ni" onclick="doLogout()"><span class="ni-ico">🚪</span>Logout</div>
    </div>
  </div>

  <!-- DASHBOARD -->
  <div class="page on" id="pg-dashboard" style="padding:16px">
    <div class="greet-card">
      <div style="font-size:12px;color:rgba(255,255,255,.7)" id="gtime">Good Morning ☀️</div>
      <div style="font-size:22px;font-weight:800;color:#fff;margin:4px 0 10px" id="greetName">Assalam-o-Alaikum! 👋</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <div class="chip" style="background:rgba(255,255,255,.15);color:#fff" id="dashAcresChip">🌾 -- Acres</div>
        <div class="chip" style="background:rgba(255,255,255,.15);color:#fff" id="dashLocChip">📍 --</div>
        <div class="chip" style="background:rgba(239,68,68,.3);color:#fff" id="droneStatusChip">🚁 Drone Idle</div>
      </div>
    </div>
    <div class="alert alert-warn" id="windAlert">⚠️ Wind 18 km/h — Delay spraying by 2 hours</div>
    <div class="alert alert-ok" id="missionAlert">✅ Mission ready — Connect your drone to begin</div>
    <div class="gs-grid">
      <div class="gs-card"><div style="font-size:26px">🌾</div><div style="font-size:22px;font-weight:800" id="dashTotalAcres">--</div><div style="font-size:12px;color:var(--ts)">Total Acres</div></div>
      <div class="gs-card"><div style="font-size:26px">🚁</div><div style="font-size:22px;font-weight:800" id="dashBat">87%</div><div style="font-size:12px;color:var(--ts)">Drone Bat</div></div>
      <div class="gs-card"><div style="font-size:26px">💧</div><div style="font-size:22px;font-weight:800" id="dashTank">64%</div><div style="font-size:12px;color:var(--ts)">Spray Tank</div></div>
      <div class="gs-card"><div style="font-size:26px">💰</div><div style="font-size:22px;font-weight:800" id="dashProfit">₨0</div><div style="font-size:12px;color:var(--ts)">This Month</div></div>
    </div>
    <div class="wcard" id="dashWeatherCard">
      <div style="font-size:12px;opacity:.8" id="dashWeatherLoc">📍 Loading...</div>
      <div style="font-size:44px;font-weight:800;color:#fff;line-height:1" id="dashTemp">--°</div>
      <div style="font-size:13px;opacity:.9;color:#fff;margin:4px 0 12px" id="dashWeatherDesc">🌤️ Loading weather...</div>
      <div style="display:flex;gap:14px;flex-wrap:wrap" id="dashWeatherMeta"></div>
    </div>
    <div class="card" style="padding:16px;margin-bottom:14px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <div style="font-size:15px;font-weight:700">🚁 Spray Coverage</div>
        <div class="live-badge" id="coverageBadge"><div class="ldot"></div><span id="coverageBadgeTxt">IDLE</span></div>
      </div>
      <div class="prog-label"><span style="color:var(--ts)">Sprayed Area</span><span style="font-weight:800;color:var(--gp)" id="dpct">0%</span></div>
      <div class="pb"><div class="pf" id="dbar" style="width:0%;background:linear-gradient(90deg,#1a7a3e,#2ecc71)"></div></div>
      <div style="display:flex;justify-content:space-between;font-size:11px;color:var(--tm);margin-top:6px"><span>0</span><span id="coveredAcresText">0/-- acres</span><span id="totalAcresText">-- acres</span></div>
    </div>
    <div class="sec-hd"><div class="sec-t">Recent Activity</div><button class="btn btn-g btn-sm" onclick="openAddActivity()">+ Add</button></div>
    <div class="card" style="padding:0 14px" id="activityList">
      <!-- Activities rendered by JS -->
    </div>
  </div>

  <!-- DRONE PAGE -->
  <div class="page drone-page" id="pg-drone">
    <div class="drone-header">
      <div style="display:flex;justify-content:space-between;align-items:center">
        <div>
          <div style="color:#fff;font-size:17px;font-weight:800">🚁 Drone Control</div>
          <div style="color:rgba(255,255,255,.6);font-size:12px;margin-top:2px" id="droneModelLabel">No drone selected</div>
        </div>
        <div style="display:flex;align-items:center;gap:8px">
          <button onclick="openDroneSelector()" style="background:rgba(46,204,113,.15);border:1px solid rgba(46,204,113,.4);color:#2ecc71;padding:7px 12px;border-radius:9px;font-size:12px;font-weight:700;cursor:pointer">🔄 Change Drone</button>
          <div class="live-badge" id="droneLiveBadge"><div class="ldot"></div>LIVE</div>
        </div>
      </div>
    </div>

    <div class="drone-canvas-container">
      <canvas id="droneCanvas"></canvas>
      <div class="drone-hud-overlay">
        <div class="hud-row">
          <div class="hud-box">
            <div class="hud-val" id="hudBat">87%</div>
            <div class="hud-lbl">🔋 Battery</div>
          </div>
          <div class="hud-box hud-center">
            <div class="hud-val" id="hudAlt">25m</div>
            <div class="hud-lbl">📏 Altitude</div>
          </div>
          <div class="hud-box" style="text-align:right">
            <div class="hud-val" id="hudSpd">0.0</div>
            <div class="hud-lbl">⚡ km/h</div>
          </div>
        </div>
        <div style="text-align:center;margin-top:8px">
          <div class="hud-status" id="hudStatus">
            <div class="ldot" style="background:#2ecc71"></div>
            <span id="hudStatusTxt">IDLE — Ready</span>
          </div>
        </div>
      </div>
      <div class="spray-indicator">
        <div style="display:flex;justify-content:space-between;margin-bottom:4px">
          <span style="color:rgba(255,255,255,.6);font-size:10px;font-weight:700">SPRAY TANK</span>
          <span style="color:#38bdf8;font-size:10px;font-weight:800" id="tankPct">64%</span>
        </div>
        <div class="spray-bar-bg"><div class="spray-bar-fill" id="tankBar" style="width:64%"></div></div>
      </div>
    </div>

    <div class="tele-bar">
      <div class="tele-item"><div class="tv" id="tGPS">--N</div><div class="tu">GPS Lat</div></div>
      <div class="tele-item"><div class="tv" id="tLng">--E</div><div class="tu">GPS Lng</div></div>
      <div class="tele-item"><div class="tv" id="tWind">18km/h</div><div class="tu">Wind</div></div>
      <div class="tele-item"><div class="tv" id="tCov">0%</div><div class="tu">Coverage</div></div>
      <div class="tele-item"><div class="tv" id="tTime">32min</div><div class="tu">Flight Left</div></div>
    </div>

    <div class="joy-section">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
        <span style="color:rgba(255,255,255,.5);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">🕹️ Flight Joysticks</span>
        <div class="chip" style="background:rgba(46,204,113,.15);color:#2ecc71;font-size:11px" id="modeChip">Manual Mode</div>
      </div>
      <div class="joy-grid">
        <div class="joy-wrap">
          <div class="joy-lbl">Throttle / Yaw</div>
          <div class="joystick" id="joy-left"><div class="jknob" id="jkL"></div></div>
          <div style="color:rgba(255,255,255,.35);font-size:10px;text-align:center">↑↓ Altitude • ←→ Rotate</div>
        </div>
        <div class="joy-center-panel">
          <button onclick="setFlightMode('hover')" id="btnHover" style="padding:8px 10px;border-radius:9px;background:rgba(46,204,113,.1);border:1.5px solid rgba(46,204,113,.25);color:#2ecc71;font-size:11px;font-weight:700;cursor:pointer;width:70px;transition:.2s">⏸️ Hover</button>
          <button onclick="takeOffLand()" id="btnTOL" style="padding:8px 10px;border-radius:9px;background:rgba(46,204,113,.15);border:1.5px solid rgba(46,204,113,.4);color:#2ecc71;font-size:11px;font-weight:700;cursor:pointer;width:70px;transition:.2s">🛫 Takeoff</button>
          <button onclick="setFlightMode('rtl')" id="btnRTL" style="padding:8px 10px;border-radius:9px;background:rgba(245,158,11,.1);border:1.5px solid rgba(245,158,11,.3);color:#f59e0b;font-size:11px;font-weight:700;cursor:pointer;width:70px;transition:.2s">🏠 RTL</button>
          <button onclick="setFlightMode('auto')" id="btnAuto" style="padding:8px 10px;border-radius:9px;background:rgba(14,165,233,.1);border:1.5px solid rgba(14,165,233,.3);color:#38bdf8;font-size:11px;font-weight:700;cursor:pointer;width:70px;transition:.2s">🤖 Auto</button>
        </div>
        <div class="joy-wrap">
          <div class="joy-lbl">Pitch / Roll</div>
          <div class="joystick" id="joy-right"><div class="jknob" id="jkR"></div></div>
          <div style="color:rgba(255,255,255,.35);font-size:10px;text-align:center">↑↓ Fwd/Back • ←→ Left/Right</div>
        </div>
      </div>
    </div>

    <div class="spray-ctrl">
      <div class="spray-ctrl-title">💧 Spray Control Panel</div>
      <div class="spray-btns">
        <button class="sbn spray-on" id="sprayToggleBtn" onclick="toggleSpray()">
          <span class="sbn-ico">💧</span>
          <span id="sprayBtnTxt">Spray OFF</span>
        </button>
        <button class="sbn spray-on" onclick="setSprayPattern('full')" id="spFull" style="background:rgba(14,165,233,.08);border:1.5px solid rgba(14,165,233,.25);color:rgba(14,165,233,.7)">
          <span class="sbn-ico">🌊</span><span>Full Width</span>
        </button>
        <button class="sbn spray-on" onclick="setSprayPattern('strip')" id="spStrip" style="background:rgba(14,165,233,.08);border:1.5px solid rgba(14,165,233,.25);color:rgba(14,165,233,.7)">
          <span class="sbn-ico">〰️</span><span>Strip Mode</span>
        </button>
        <button class="sbn spray-on" onclick="setSprayPattern('spot')" id="spSpot" style="background:rgba(14,165,233,.08);border:1.5px solid rgba(14,165,233,.25);color:rgba(14,165,233,.7)">
          <span class="sbn-ico">🎯</span><span>Spot Spray</span>
        </button>
        <button class="sbn nav" onclick="setFlightMode('auto')">
          <span class="sbn-ico">🤖</span><span>Auto Path</span>
        </button>
        <button class="sbn danger" onclick="emergStop()">
          <span class="sbn-ico">🛑</span><span>E-Stop</span>
        </button>
      </div>
      <div class="spray-rate-row">
        <span class="spray-rate-lbl">💧 Spray Rate:</span>
        <input type="range" id="sprayRateSlider" min="1" max="10" value="5" oninput="updateSprayRate(this.value)"/>
        <span class="spray-rate-val" id="sprayRateVal">5 L/ha</span>
      </div>
      <div class="spray-ctrl-title" style="margin-top:6px">📏 Altitude Control</div>
      <div class="alt-ctrl-row">
        <button class="alt-btn" onclick="changeAlt(-1)">▼</button>
        <div class="alt-val" id="altDisplay">25 m</div>
        <button class="alt-btn" onclick="changeAlt(1)">▲</button>
        <span style="color:rgba(255,255,255,.4);font-size:11px;margin-left:4px">AGL</span>
      </div>
      <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.25);border-radius:9px;padding:10px 12px;font-size:12px;color:#f59e0b">
        ⚠️ Wind: 18 km/h — Spray drift risk. Auto-spray paused above 25 km/h.
      </div>
    </div>
    <button class="emrg" onclick="emergStop()">🛑 EMERGENCY STOP — Press to Halt All Systems</button>
  </div>

  <!-- FIELDS PAGE -->
  <div class="page" id="pg-fields" style="padding:16px">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
      <div><div style="font-size:17px;font-weight:800">🗺️ GPS Field Map</div><div style="font-size:12px;color:var(--tm)">Manage your farmland</div></div>
      <button class="btn btn-g btn-sm" onclick="toast('📍 Draw mode active!')">+ Field</button>
    </div>
    <!-- Google Maps embed for Multan farmlands -->
    <div id="googleMap">
      <div class="map-placeholder" onclick="openFullMap()">
        <div class="mgrid"></div>
        <div class="rring"></div><div class="rring"></div><div class="rring"></div>
        <div class="field-a"></div>
        <div style="position:absolute;top:58px;left:40px;color:rgba(46,204,113,.85);font-size:11px;font-weight:700" id="fieldALabel">FIELD A — Loading...</div>
        <div class="mdrn" style="top:100px;left:140px;font-size:28px">🚁</div>
        <div style="position:absolute;top:185px;left:160px;width:110px;height:60px;border:2px dashed rgba(14,165,233,.6);border-radius:6px;background:rgba(14,165,233,.08)"></div>
        <div style="position:absolute;top:193px;left:167px;color:rgba(14,165,233,.8);font-size:11px;font-weight:700" id="fieldBLabel">FIELD B — Loading...</div>
        <div style="position:absolute;top:10px;right:10px;background:rgba(0,0,0,.6);color:#2ecc71;font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700">📍 Tap to open Maps</div>
        <div style="position:absolute;bottom:10px;left:10px;background:rgba(255,255,255,.9);border-radius:9px;padding:8px 12px">
          <div style="display:flex;gap:14px;font-size:12px">
            <div><span style="font-weight:800;color:var(--gp)" id="mapTotalAcres">--</span> Acres</div>
            <div><span style="font-weight:800;color:var(--gp)">2</span> Fields</div>
            <div><span style="font-weight:800;color:var(--gp)" id="mapSprayPct">0%</span> Sprayed</div>
          </div>
        </div>
      </div>
    </div>
    <div class="alert alert-ok" style="cursor:pointer" onclick="openFullMap()">🗺️ Tap map above or click here to open satellite view in Google Maps</div>
    <div class="sec-hd"><div class="sec-t">My Fields</div></div>
    <div style="display:flex;flex-direction:column;gap:11px">
      <div class="card" style="padding:15px">
        <div style="display:flex;justify-content:space-between">
          <div><div style="font-size:15px;font-weight:700">🌾 Field A — <span id="fieldACrop">Wheat</span></div><div style="font-size:12px;color:var(--tm);margin-top:3px" id="fieldAAddr">Plot #34-B, Multan</div>
          <div style="display:flex;gap:6px;margin-top:8px"><span class="chip chip-g" id="fieldASize">-- Acres</span><span class="chip chip-s">Loamy</span></div></div>
          <button class="btn btn-out btn-sm" onclick="openFullMap()">View</button>
        </div>
        <div style="margin-top:11px"><div class="prog-label"><span style="color:var(--tm);font-size:12px">Spray Progress</span><span style="font-weight:800;color:var(--gp)" id="fieldACov">0%</span></div>
        <div class="pb"><div class="pf" id="fieldABar" style="width:0%;background:linear-gradient(90deg,#1a7a3e,#2ecc71)"></div></div></div>
      </div>
      <div class="card" style="padding:15px">
        <div style="display:flex;justify-content:space-between">
          <div><div style="font-size:15px;font-weight:700">🌿 Field B — <span id="fieldBCrop">Cotton</span></div><div style="font-size:12px;color:var(--tm);margin-top:3px" id="fieldBAddr">Plot #67-A, Multan</div>
          <div style="display:flex;gap:6px;margin-top:8px"><span class="chip chip-g" id="fieldBSize">-- Acres</span><span class="chip chip-s">Clay Soil</span></div></div>
          <button class="btn btn-out btn-sm" onclick="openFullMap()">View</button>
        </div>
        <div style="margin-top:11px"><div class="prog-label"><span style="color:var(--tm);font-size:12px">Spray Progress</span><span style="font-weight:800;color:var(--sky)" id="fieldBCov">0%</span></div>
        <div class="pb"><div class="pf" id="fieldBBar" style="width:0%;background:linear-gradient(90deg,#0ea5e9,#38bdf8)"></div></div></div>
      </div>
    </div>
  </div>

  <!-- WEATHER PAGE -->
  <div class="page" id="pg-weather" style="padding:16px">
    <div class="weather-hero" id="weatherHero">
      <div style="font-size:14px;opacity:.85" id="weatherCity">📍 Loading...</div>
      <div style="font-size:68px;font-weight:800;line-height:1" id="weatherTemp">--°</div>
      <div style="font-size:14px;opacity:.9;margin:4px 0 8px" id="weatherDesc">Loading weather...</div>
      <div class="wm-grid">
        <div class="wmet"><div style="font-size:18px;font-weight:800" id="wHumidity">--%</div><div style="font-size:11px;opacity:.8">💧 Humidity</div></div>
        <div class="wmet"><div style="font-size:18px;font-weight:800" id="wWind">--</div><div style="font-size:11px;opacity:.8">💨 Wind km/h</div></div>
        <div class="wmet"><div style="font-size:18px;font-weight:800" id="wUV">UV--</div><div style="font-size:11px;opacity:.8">☀️ UV Index</div></div>
      </div>
    </div>
    <div id="weatherSprayAlert" class="alert alert-warn">⚠️ Loading spray safety info...</div>
    <div class="sec-hd"><div class="sec-t">7-Day Forecast</div><button class="btn btn-g btn-sm" onclick="loadWeather()">🔄 Refresh</button></div>
    <div class="fcast-row" id="forecastRow">
      <!-- Rendered by JS -->
    </div>
    <div class="card" style="padding:15px">
      <div style="font-size:15px;font-weight:700;margin-bottom:13px">🚁 Spray Safety Checker</div>
      <div style="display:flex;flex-direction:column;gap:10px" id="sprayCheckerList">
        <!-- Rendered by JS -->
      </div>
    </div>
    <div class="card" style="padding:15px;margin-top:12px">
      <div style="font-size:15px;font-weight:700;margin-bottom:13px">🌡️ Today's Hourly Trend</div>
      <div id="hourlyChart" style="display:flex;align-items:flex-end;gap:4px;height:80px;padding:0 4px"></div>
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--tm);margin-top:6px;padding:0 4px">
        <span>6AM</span><span>9AM</span><span>12PM</span><span>3PM</span><span>6PM</span><span>9PM</span>
      </div>
    </div>
  </div>

  <!-- AI PAGE -->
  <div class="page" id="pg-ai" style="padding:16px">
    <div style="background:linear-gradient(135deg,#7c3aed,#4c1d95);border-radius:var(--rl);padding:18px;margin-bottom:16px;position:relative;overflow:hidden">
      <div style="position:absolute;right:14px;top:50%;transform:translateY(-50%);font-size:54px;opacity:.18">🤖</div>
      <div style="color:#fff;font-size:16px;font-weight:700">🤖 AI Farming Advisor</div>
      <div style="color:rgba(255,255,255,.75);font-size:13px;margin-top:4px">Powered by Claude AI — Smart farming for Pakistan</div>
    </div>
    <div class="alert alert-bad">🐛 HIGH RISK: Aphid outbreak likely in 3 days — Act now!</div>
    <div class="sec-hd"><div class="sec-t">Today's Recommendations</div></div>
    <div class="rec-card"><div style="display:flex;gap:11px;align-items:flex-start"><div style="width:42px;height:42px;border-radius:11px;background:var(--redl);display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0">🐛</div><div><div style="font-size:15px;font-weight:700">Pest Alert: Aphid Risk</div><div style="font-size:12px;color:var(--ts)">Field B — Cotton</div></div></div><div style="font-size:13px;color:var(--ts);line-height:1.6;margin-top:9px">High humidity + warm temp: ideal aphid conditions. Spray Imidacloprid 200ml/acre within 48 hours.</div><span class="chip chip-r" style="margin-top:8px;display:inline-flex">🔴 High Priority</span><br/><button class="btn btn-g btn-sm" style="margin-top:10px" onclick="scheduleDroneSpray()">Schedule Drone Spray</button></div>
    <div class="rec-card"><div style="display:flex;gap:11px;align-items:flex-start"><div style="width:42px;height:42px;border-radius:11px;background:var(--gpal);display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0">🌱</div><div><div style="font-size:15px;font-weight:700">Fertilizer Needed</div><div style="font-size:12px;color:var(--ts)" id="aiFieldA">Field A</div></div></div><div style="font-size:13px;color:var(--ts);line-height:1.6;margin-top:9px">Nitrogen deficiency detected. Apply Urea 50 kg/acre via drone for 40% better absorption.</div><span class="chip chip-gold" style="margin-top:8px;display:inline-flex">🟡 Medium</span></div>
    <div class="sec-hd" style="margin-top:6px"><div class="sec-t">💬 Ask AI Advisor</div><span style="font-size:11px;color:var(--gp);font-weight:600">Internet-powered</span></div>
    <div class="ai-chat">
      <div class="ai-msgs" id="aiMsgs">
        <div class="amsg amsg-b">Assalam-o-Alaikum! 🌾 I'm your AI Farming Advisor for Pakistan. Ask me about pests, fertilizers, irrigation, crop prices, drone missions, or anything about your farm!<span style="display:block;font-size:10px;opacity:.5;margin-top:4px">Now</span></div>
      </div>
      <div class="ai-inp-row">
        <input class="ai-inp" id="aiInp" placeholder="Koi bhi sawaal poochein..." onkeypress="if(event.key==='Enter')aiSend()"/>
        <button class="asend" id="aiSendBtn" onclick="aiSend()">➤</button>
      </div>
    </div>
  </div>

  <!-- RESOURCES PAGE -->
  <div class="page" id="pg-resources" style="padding:16px">
    <div style="font-size:17px;font-weight:800;margin-bottom:16px">💰 Resources & Finance</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:16px">
      <div style="background:linear-gradient(135deg,#1a7a3e,#27ae60);border-radius:var(--r);padding:15px;color:#fff"><div style="font-size:11px;opacity:.8">Income</div><div style="font-size:24px;font-weight:800" id="totalIncome">₨0</div><div style="font-size:11px;opacity:.7;margin-top:3px" id="incomeChange">--</div></div>
      <div style="background:linear-gradient(135deg,#ef4444,#dc2626);border-radius:var(--r);padding:15px;color:#fff"><div style="font-size:11px;opacity:.8">Expenses</div><div style="font-size:24px;font-weight:800" id="totalExpenses">₨0</div><div style="font-size:11px;opacity:.7;margin-top:3px" id="expensesChange">--</div></div>
    </div>
    <div style="background:linear-gradient(135deg,#0ea5e9,#0369a1);border-radius:var(--r);padding:15px;color:#fff;margin-bottom:16px"><div style="font-size:11px;opacity:.8">Net Profit</div><div style="font-size:28px;font-weight:800" id="netProfit">₨0</div><div style="font-size:12px;opacity:.75;margin-top:3px" id="profitNote">Add transactions to see your profit margin</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:16px">
      <div class="card" style="padding:14px"><div style="font-size:28px">⛽</div><div style="font-size:13px;font-weight:700;margin-top:6px">Fuel</div><div style="font-size:20px;font-weight:800" id="resFuel">142L</div><div class="pb" style="margin-top:8px"><div class="pf" style="width:65%;background:var(--gold)"></div></div></div>
      <div class="card" style="padding:14px"><div style="font-size:28px">💧</div><div style="font-size:13px;font-weight:700;margin-top:6px">Water</div><div style="font-size:20px;font-weight:800" id="resWater">48KG</div><div class="pb" style="margin-top:8px"><div class="pf" style="width:45%;background:var(--sky)"></div></div></div>
      <div class="card" style="padding:14px"><div style="font-size:28px">🧪</div><div style="font-size:13px;font-weight:700;margin-top:6px">Fertilizer</div><div style="font-size:20px;font-weight:800" id="resFert">18 Bags</div><div class="pb" style="margin-top:8px"><div class="pf" style="width:72%;background:var(--gp)"></div></div></div>
      <div class="card" style="padding:14px"><div style="font-size:28px">👷</div><div style="font-size:13px;font-weight:700;margin-top:6px">Labor</div><div style="font-size:20px;font-weight:800" id="resLabor">₨0</div><div class="pb" style="margin-top:8px"><div class="pf" id="laborBar" style="width:0%;background:var(--pur)"></div></div></div>
    </div>
    <div class="sec-hd"><div class="sec-t">Transactions</div><button class="btn btn-g btn-sm" onclick="openAddTransaction()">+ Add</button></div>
    <div class="exp-card" id="transactionList">
      <!-- Rendered by JS -->
    </div>
  </div>

  <!-- PRICES PAGE -->
  <div class="page" id="pg-prices" style="padding:16px">
    <div style="font-size:17px;font-weight:800;margin-bottom:4px">📈 Crop Prices</div>
    <div style="font-size:12px;color:var(--tm);margin-bottom:12px" id="priceUpdateTime">Live Mandi Prices • Loading...</div>
    <div class="alert alert-ok" id="priceAITip">💡 Loading AI price tip...</div>
    <div style="display:flex;flex-direction:column;gap:11px" id="priceList">
      <!-- Rendered dynamically -->
    </div>
    <div style="background:linear-gradient(135deg,#7c3aed,#4c1d95);border-radius:var(--r);padding:15px;margin-top:12px;color:#fff"><div style="font-size:14px;font-weight:700;margin-bottom:5px">🤖 AI Price Forecast</div><div style="font-size:13px;opacity:.9;line-height:1.6" id="aiForecastTxt">Wheat +8–12% in 3 weeks due to export demand. Best sell: June 15–25. Cotton may fall further. Monitor daily prices.</div></div>
  </div>

  <!-- MACHINERY PAGE -->
  <div class="page" id="pg-machinery" style="padding:16px">
    <div style="font-size:17px;font-weight:800;margin-bottom:14px">🚜 Machinery Locator</div>
    <div class="map-cont" style="height:190px;margin-bottom:14px;cursor:pointer" onclick="openFullMap()"><div class="map-inner"><div class="mgrid"></div><div style="position:absolute;top:35px;left:55px;font-size:26px;animation:mdf 3s ease-in-out infinite">🚜</div><div style="position:absolute;top:65px;left:50px;background:var(--gold);color:#000;font-size:9px;font-weight:800;padding:2px 7px;border-radius:99px">1.2 km</div><div style="position:absolute;top:80px;right:55px;font-size:26px;animation:mdf 2s ease-in-out infinite .5s">🌾</div><div style="position:absolute;top:110px;right:50px;background:var(--gl);color:#000;font-size:9px;font-weight:800;padding:2px 7px;border-radius:99px">2.8 km</div><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:18px">📍</div><div style="position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.7);color:#2ecc71;font-size:10px;padding:4px 8px;border-radius:6px">📍 Tap for Google Maps</div></div></div>
    <div class="mach-item"><div style="display:flex;align-items:center;gap:12px"><div style="font-size:40px">🚜</div><div style="flex:1"><div style="font-size:15px;font-weight:700">Massey Ferguson 240</div><div style="font-size:12px;color:var(--tm)">Muhammad Aslam • Chak 44-A</div></div><div style="text-align:right"><div style="color:var(--sky);font-size:13px;font-weight:700">📍 1.2 km</div><div style="color:var(--gp);font-size:13px;font-weight:700">₨2,500/hr</div></div></div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px"><span class="chip chip-g" style="font-size:11px">🟢 Available</span><div style="display:flex;gap:8px"><button onclick="toast('📞 Calling 0300-1234567...')" class="btn btn-g btn-sm">📞 Call</button><button onclick="toast('📅 Booking confirmed!')" class="btn btn-out btn-sm">Book</button></div></div></div>
    <div class="mach-item"><div style="display:flex;align-items:center;gap:12px"><div style="font-size:40px">🌾</div><div style="flex:1"><div style="font-size:15px;font-weight:700">Combine Harvester</div><div style="font-size:12px;color:var(--tm)">Fateh Agricultural Services</div></div><div style="text-align:right"><div style="color:var(--sky);font-size:13px;font-weight:700">📍 2.8 km</div><div style="color:var(--gp);font-size:13px;font-weight:700">₨8,000/day</div></div></div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px"><span class="chip chip-g" style="font-size:11px">🟢 Jun 12</span><div style="display:flex;gap:8px"><button onclick="toast('📞 Calling...')" class="btn btn-g btn-sm">📞 Call</button><button onclick="toast('📅 Booking...')" class="btn btn-out btn-sm">Book</button></div></div></div>
    <div class="mach-item"><div style="display:flex;align-items:center;gap:12px"><div style="font-size:40px">🚛</div><div style="flex:1"><div style="font-size:15px;font-weight:700">Seed Drill Machine</div><div style="font-size:12px;color:var(--tm)">Khalid Brothers Equipment</div></div><div style="text-align:right"><div style="color:var(--sky);font-size:13px;font-weight:700">📍 3.4 km</div><div style="color:var(--gp);font-size:13px;font-weight:700">₨3,500/day</div></div></div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px"><span class="chip chip-r" style="font-size:11px">🔴 Busy</span><div style="display:flex;gap:8px"><button onclick="toast('📞 Calling...')" class="btn btn-g btn-sm">📞 Call</button><button onclick="toast('📋 Waitlisted!')" class="btn btn-out btn-sm">Waitlist</button></div></div></div>
  </div>

  <!-- EXPERTS PAGE -->
  <div class="page" id="pg-experts" style="padding:16px">
    <div style="font-size:17px;font-weight:800;margin-bottom:4px">👨‍🌾 Expert Contact</div>
    <div style="font-size:12px;color:var(--tm);margin-bottom:12px">Get professional farming advice</div>
    <div class="alert alert-ok">📞 Free Helpline: <strong>0800-AGRI (2474)</strong></div>
    <div class="expert-card"><div style="display:flex;gap:12px;align-items:flex-start"><div class="xav">👨‍🔬</div><div><div style="font-size:15px;font-weight:700">Dr. Imran Ashraf</div><div style="font-size:12px;color:var(--ts)">Crop Disease Specialist • PARB</div><div style="color:var(--gold);font-size:12px;font-weight:600;margin-top:4px">⭐⭐⭐⭐⭐ 4.9</div></div></div><div style="display:flex;gap:7px;margin-top:12px"><button class="xbtn xbtn-c" onclick="toast('📞 Calling Dr. Imran...')">📞 Call</button><button class="xbtn xbtn-v" onclick="toast('📹 Video call starting...')">📹 Video</button><button class="xbtn xbtn-m" onclick="toast('💬 Chat opened!')">💬 Chat</button></div></div>
    <div class="expert-card"><div style="display:flex;gap:12px;align-items:flex-start"><div class="xav">👩‍🌾</div><div><div style="font-size:15px;font-weight:700">Ms. Sana Butt</div><div style="font-size:12px;color:var(--ts)">Soil & Fertilizer Expert • NARC</div><div style="color:var(--gold);font-size:12px;font-weight:600;margin-top:4px">⭐⭐⭐⭐⭐ 4.8</div></div></div><div style="display:flex;gap:7px;margin-top:12px"><button class="xbtn xbtn-c" onclick="toast('📞 Calling Ms. Sana...')">📞 Call</button><button class="xbtn xbtn-v" onclick="toast('📹 Video call...')">📹 Video</button><button class="xbtn xbtn-m" onclick="toast('💬 Chat opened!')">💬 Chat</button></div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:6px">
      <div style="background:var(--gpal);border-radius:var(--rs);padding:13px;cursor:pointer" onclick="toast('📞 0800-2474')"><div style="font-size:22px">🏛️</div><div style="font-size:13px;font-weight:700;color:var(--gp);margin-top:5px">Punjab Agri</div><div style="font-size:12px;color:var(--tm)">0800-2474</div></div>
      <div style="background:var(--skyl);border-radius:var(--rs);padding:13px;cursor:pointer" onclick="toast('📞 051-9290160')"><div style="font-size:22px">🇵🇰</div><div style="font-size:13px;font-weight:700;color:#0369a1;margin-top:5px">NARC</div><div style="font-size:12px;color:var(--tm)">051-9290160</div></div>
      <div style="background:var(--goldl);border-radius:var(--rs);padding:13px;cursor:pointer" onclick="toast('🌍 fao.org/pakistan')"><div style="font-size:22px">🌍</div><div style="font-size:13px;font-weight:700;color:#92400e;margin-top:5px">FAO Pakistan</div><div style="font-size:12px;color:var(--tm)">fao.org</div></div>
      <div style="background:var(--redl);border-radius:var(--rs);padding:13px;cursor:pointer" onclick="toast('🆘 0800-6666')"><div style="font-size:22px">🆘</div><div style="font-size:13px;font-weight:700;color:var(--red);margin-top:5px">Emergency</div><div style="font-size:12px;color:var(--tm)">0800-6666</div></div>
    </div>
  </div>

  <!-- PROFILE PAGE -->
  <div class="page" id="pg-profile" style="padding:16px">
    <div class="profile-hero">
      <div class="pav">👨‍🌾</div>
      <div style="font-size:22px;font-weight:800" id="profileName">Kisan</div>
      <div style="opacity:.75;font-size:13px;margin-top:3px" id="profileCnic">CNIC: --</div>
      <div style="display:flex;gap:8px;justify-content:center;margin-top:12px">
        <div class="chip" style="background:rgba(255,255,255,.15);color:#fff" id="profileAcresChip">🌾 -- Acres</div>
        <div class="chip" style="background:rgba(255,255,255,.15);color:#fff">⭐ Verified</div>
      </div>
    </div>
    <div class="pro-sec">
      <div class="pro-row"><div style="font-size:20px">📱</div><div><div style="font-size:11px;color:var(--tm)">Mobile</div><div style="font-size:14px;font-weight:600" id="profileMob">--</div></div></div>
      <div class="pro-row"><div style="font-size:20px">📍</div><div><div style="font-size:11px;color:var(--tm)">District & Province</div><div style="font-size:14px;font-weight:600" id="profileLoc">--</div></div></div>
      <div class="pro-row"><div style="font-size:20px">🌾</div><div><div style="font-size:11px;color:var(--tm)">Farm</div><div style="font-size:14px;font-weight:600" id="profileFarm">--</div></div></div>
      <div class="pro-row"><div style="font-size:20px">💧</div><div><div style="font-size:11px;color:var(--tm)">Irrigation</div><div style="font-size:14px;font-weight:600" id="profileIrr">--</div></div></div>
    </div>
    <div class="pro-sec">
      <div class="pro-row" onclick="openEditProfile()"><div style="font-size:20px">✏️</div><div style="font-size:14px;font-weight:600">Edit Profile Info</div><div style="margin-left:auto;color:var(--gp);font-weight:700">Edit ›</div></div>
      <div class="pro-row" onclick="nav('settings')"><div style="font-size:20px">⚙️</div><div style="font-size:14px;font-weight:600">Settings</div><div style="margin-left:auto;color:var(--tm)">›</div></div>
      <div class="pro-row" onclick="exportReport()"><div style="font-size:20px">📋</div><div style="font-size:14px;font-weight:600">Export Reports</div><div style="margin-left:auto;color:var(--tm)">›</div></div>
      <div class="pro-row" onclick="doLogout()"><div style="font-size:20px">🚪</div><div style="font-size:14px;font-weight:600;color:var(--red)">Logout</div></div>
    </div>
  </div>

  <!-- SETTINGS PAGE -->
  <div class="page" id="pg-settings" style="padding:16px">
    <div style="font-size:17px;font-weight:800;margin-bottom:16px">⚙️ Settings</div>
    <div class="pro-sec" style="margin-bottom:14px">
      <div style="padding:12px 14px;font-size:12px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--bdr)">Notifications</div>
      <div class="setting-row"><div style="font-size:20px">🔔</div><div><div style="font-size:14px;font-weight:600">Pest Alerts</div><div style="font-size:12px;color:var(--tm)">Get notified of pest risks</div></div><div class="toggle on" id="tog-pest" onclick="toggleSetting(this,'pest')"></div></div>
      <div class="setting-row"><div style="font-size:20px">🌧️</div><div><div style="font-size:14px;font-weight:600">Weather Alerts</div><div style="font-size:12px;color:var(--tm)">Rain & wind warnings</div></div><div class="toggle on" id="tog-weather" onclick="toggleSetting(this,'weather')"></div></div>
      <div class="setting-row"><div style="font-size:20px">💰</div><div><div style="font-size:14px;font-weight:600">Price Alerts</div><div style="font-size:12px;color:var(--tm)">Mandi price changes</div></div><div class="toggle on" id="tog-price" onclick="toggleSetting(this,'price')"></div></div>
      <div class="setting-row"><div style="font-size:20px">🚁</div><div><div style="font-size:14px;font-weight:600">Drone Alerts</div><div style="font-size:12px;color:var(--tm)">Battery & mission status</div></div><div class="toggle on" id="tog-drone" onclick="toggleSetting(this,'drone')"></div></div>
    </div>
    <div class="pro-sec" style="margin-bottom:14px">
      <div style="padding:12px 14px;font-size:12px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--bdr)">App Preferences</div>
      <div class="setting-row"><div style="font-size:20px">🌙</div><div><div style="font-size:14px;font-weight:600">Dark Mode (Drone View)</div><div style="font-size:12px;color:var(--tm)">Already dark on drone page</div></div><div class="toggle on" id="tog-dark" onclick="toggleSetting(this,'dark')"></div></div>
      <div class="setting-row"><div style="font-size:20px">🇵🇰</div><div><div style="font-size:14px;font-weight:600">Urdu Language</div><div style="font-size:12px;color:var(--tm)">Show Urdu labels</div></div><div class="toggle" id="tog-urdu" onclick="toggleSetting(this,'urdu')"></div></div>
      <div class="setting-row"><div style="font-size:20px">📍</div><div><div style="font-size:14px;font-weight:600">GPS Location</div><div style="font-size:12px;color:var(--tm)">Auto-detect your location</div></div><div class="toggle on" id="tog-gps" onclick="toggleSetting(this,'gps')"></div></div>
    </div>
    <div class="pro-sec" style="margin-bottom:14px">
      <div style="padding:12px 14px;font-size:12px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--bdr)">Data & Privacy</div>
      <div class="setting-row" onclick="toast('🔄 Data synced!')"><div style="font-size:20px">☁️</div><div style="font-size:14px;font-weight:600">Sync Farm Data</div><div style="margin-left:auto;color:var(--gp);font-size:13px;font-weight:600">Sync</div></div>
      <div class="setting-row" onclick="clearAllData()"><div style="font-size:20px;color:var(--red)">🗑️</div><div style="font-size:14px;font-weight:600;color:var(--red)">Clear All Data</div><div style="margin-left:auto;color:var(--red);font-size:13px;font-weight:600">Clear</div></div>
    </div>
    <div style="background:var(--gpal);border-radius:var(--r);padding:14px;text-align:center">
      <div style="font-size:22px;margin-bottom:6px">🌾</div>
      <div style="font-size:14px;font-weight:700;color:var(--gp)">Kisan Ka Pakistan v2.0</div>
      <div style="font-size:12px;color:var(--tm);margin-top:3px">Developed for Pakistani Farmers</div>
    </div>
  </div>

  <!-- BOTTOM NAV -->
  <div class="bnav">
    <div class="bni on" id="bn-dashboard" onclick="nav('dashboard')"><div class="bni-ico">🏡</div><span>Home</span></div>
    <div class="bni" id="bn-drone" onclick="nav('drone')"><div class="bni-ico">🚁</div><span>Drone</span></div>
    <div class="bni" id="bn-ai" onclick="nav('ai')"><div class="bni-ico">🤖</div><span>AI</span></div>
    <div class="bni" id="bn-resources" onclick="nav('resources')"><div class="bni-ico">💰</div><span>Finance</span></div>
    <div class="bni" id="bn-profile" onclick="nav('profile')"><div class="bni-ico">👤</div><span>Profile</span></div>
  </div>
</div>

<!-- MODALS -->
<!-- Add Activity Modal -->
<div class="modal-overlay" id="modal-activity">
  <div class="modal">
    <div class="modal-hd"><div style="font-size:17px;font-weight:800">+ Add Activity</div><button class="modal-close" onclick="closeModal('modal-activity')">✕</button></div>
    <div class="fg"><label>Activity Type</label>
      <select id="actType">
        <option value="🚁">🚁 Drone Spray</option>
        <option value="💧">💧 Irrigation</option>
        <option value="🌱">🌱 Fertilizer Applied</option>
        <option value="🧪">🧪 Pesticide Spray</option>
        <option value="🌾">🌾 Harvest</option>
        <option value="🚜">🚜 Ploughing</option>
        <option value="🌧️">🌧️ Rainfall</option>
        <option value="📊">📊 Soil Test</option>
      </select>
    </div>
    <div class="fg"><label>Description</label><input id="actDesc" type="text" placeholder="e.g. Mission 4 Completed — 5 acres"/></div>
    <div class="fg"><label>Field</label>
      <select id="actField"><option>Field A</option><option>Field B</option><option>Both Fields</option></select>
    </div>
    <div class="fg"><label>Date & Time</label><input id="actDate" type="datetime-local"/></div>
    <button class="btn btn-g" onclick="saveActivity()">✓ Save Activity</button>
  </div>
</div>

<!-- Add Transaction Modal -->
<div class="modal-overlay" id="modal-transaction">
  <div class="modal">
    <div class="modal-hd"><div style="font-size:17px;font-weight:800">+ Add Transaction</div><button class="modal-close" onclick="closeModal('modal-transaction')">✕</button></div>
    <div class="fg"><label>Type</label>
      <select id="txType" onchange="updateTxIcon()">
        <option value="income">💰 Income (Sale)</option>
        <option value="expense">📤 Expense</option>
      </select>
    </div>
    <div class="fg"><label>Category</label>
      <select id="txCat">
        <option>Crop Sale</option>
        <option>Chemicals</option>
        <option>Fertilizer</option>
        <option>Fuel</option>
        <option>Labor</option>
        <option>Equipment Rental</option>
        <option>Drone Service</option>
        <option>Seeds</option>
        <option>Other</option>
      </select>
    </div>
    <div class="fg"><label>Description</label><input id="txDesc" type="text" placeholder="e.g. Wheat sale 200 maunds"/></div>
    <div class="fg"><label>Amount (₨)</label><input id="txAmount" type="number" placeholder="0" min="0"/><div class="err-msg" id="txAmtErr">Enter valid amount</div></div>
    <div class="fg"><label>Date</label><input id="txDate" type="date"/></div>
    <button class="btn btn-g" onclick="saveTransaction()">✓ Save Transaction</button>
  </div>
</div>

<!-- Edit Profile Modal -->
<div class="modal-overlay" id="modal-editprofile">
  <div class="modal">
    <div class="modal-hd"><div style="font-size:17px;font-weight:800">✏️ Edit Profile</div><button class="modal-close" onclick="closeModal('modal-editprofile')">✕</button></div>
    <div class="fg"><label>Full Name</label><input id="epName" type="text"/></div>
    <div class="fg"><label>Father's Name</label><input id="epFname" type="text"/></div>
    <div class="fg"><label>District</label><input id="epDist" type="text"/></div>
    <div class="fg"><label>Province</label>
      <select id="epProv"><option>Punjab</option><option>Sindh</option><option>KPK</option><option>Balochistan</option><option>AJK</option></select>
    </div>
    <div class="fg"><label>Farm Acres</label><input id="epAcres" type="number" min="0.5"/></div>
    <div class="fg"><label>Main Crop</label>
      <select id="epCrop"><option>Wheat</option><option>Cotton</option><option>Rice</option><option>Sugarcane</option><option>Maize</option><option>Vegetables</option></select>
    </div>
    <div class="fg"><label>Irrigation Source</label>
      <select id="epIrr"><option>Canal Water</option><option>Tube Well</option><option>Rain-fed</option><option>Drip Irrigation</option></select>
    </div>
    <button class="btn btn-g" onclick="saveProfile()">✓ Save Changes</button>
  </div>
</div>

<!-- Drone Selector Modal -->
<div class="modal-overlay" id="modal-drone">
  <div class="modal" style="background:#0d1a0d">
    <div class="modal-hd">
      <div style="font-size:17px;font-weight:800;color:#fff">🚁 Select Drone</div>
      <button class="modal-close" onclick="closeModal('modal-drone')" style="background:rgba(255,255,255,.1);color:#fff">✕</button>
    </div>
    <div class="drone-list" id="droneList">
      <!-- Rendered by JS -->
    </div>
    <button class="btn btn-g" onclick="confirmDrone()">✓ Connect Drone</button>
  </div>
</div>

<div class="toast" id="toast"></div>
<div class="loader" id="loader"><div class="lspin"></div></div>

<script>
// ============================================================
// USER DATA STORE (localStorage-based multi-user)
// ============================================================
let APP_STATE = {
  currentUser: null,
  users: {},
  activities: [],
  transactions: [],
  settings: {pest:true,weather:true,price:true,drone:true,dark:true,urdu:false,gps:true},
  selectedDrone: null,
};

const DRONES = [
  {id:'dji-agri',name:'DJI Agras T40',tank:40,range:'7ha/flight',icon:'🚁',bat:87},
  {id:'dji-t20',name:'DJI Agras T20P',tank:20,range:'5ha/flight',icon:'🚁',bat:92},
  {id:'xag-p100',name:'XAG P100 Pro',tank:30,range:'6ha/flight',icon:'🛸',bat:78},
  {id:'local-kit',name:'Local DIY Kit',tank:10,range:'2ha/flight',icon:'🔧',bat:65},
];

function loadState(){
  try{
    const s=localStorage.getItem('kisan_state');
    if(s){const p=JSON.parse(s);Object.assign(APP_STATE,p);}
  }catch(e){}
}
function saveState(){
  try{localStorage.setItem('kisan_state',JSON.stringify(APP_STATE));}catch(e){}
}

loadState();

// ============================================================
// SPLASH → AUTH
// ============================================================
setTimeout(()=>{
  document.getElementById('splash').classList.add('gone');
  setTimeout(()=>{
    document.getElementById('splash').style.display='none';
    document.getElementById('authScreen').style.display='block';
  },800);
},2700);

// ============================================================
// AUTH LOGIC
// ============================================================
const DEMO_MOB='03001234567', DEMO_PASS='farmer123', DEMO_OTP='123456';

// Ensure demo user exists
if(!APP_STATE.users[DEMO_MOB]){
  APP_STATE.users[DEMO_MOB]={
    name:'Ali Hassan',fname:'Muhammad Hassan',mob:DEMO_MOB,
    cnic:'36302-1234567-1',province:'Punjab',district:'Multan',
    acres:'12',crop:'Wheat',irr:'Canal Water',pass:DEMO_PASS
  };
  saveState();
}

function setLang(l,btn){
  document.querySelectorAll('.lang-btn').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
}

function atab(t){
  document.getElementById('lt').classList.toggle('on',t==='login');
  document.getElementById('rt').classList.toggle('on',t==='reg');
  document.getElementById('loginF').style.display=t==='login'?'block':'none';
  document.getElementById('regF').style.display=t==='reg'?'block':'none';
  document.getElementById('otpF').style.display='none';
}

function showErr(id,show){const f=document.getElementById(id);if(f)f.classList.toggle('show',show);}
function markInput(id,err){const el=document.getElementById(id);if(el)el.classList.toggle('err',err);}
function clearAll(ids){ids.forEach(id=>{markInput(id,false);showErr(id+'Err',false);});}

function doLogin(){
  const mob=document.getElementById('lmob').value.trim();
  const pass=document.getElementById('lpass').value;
  clearAll(['lmob','lpass']);
  let ok=true;
  if(!mob){markInput('lmob',true);showErr('lmobErr',true);document.getElementById('lmobErr').textContent='Mobile number is required';ok=false;}
  else if(!/^0\d{10}$/.test(mob)){markInput('lmob',true);showErr('lmobErr',true);document.getElementById('lmobErr').textContent='Enter valid 11-digit mobile (e.g. 0300XXXXXXX)';ok=false;}
  if(!pass){markInput('lpass',true);showErr('lpassErr',true);document.getElementById('lpassErr').textContent='Password is required';ok=false;}
  else if(pass.length<6){markInput('lpass',true);showErr('lpassErr',true);document.getElementById('lpassErr').textContent='Password must be at least 6 characters';ok=false;}
  if(!ok)return;
  const user=APP_STATE.users[mob];
  if(!user||user.pass!==pass){
    markInput('lmob',true);markInput('lpass',true);
    document.getElementById('lpassErr').textContent='❌ Mobile or password is incorrect';
    showErr('lpassErr',true);
    return;
  }
  APP_STATE.currentUser=mob;
  showLoader();
  setTimeout(()=>{hideLoader();document.getElementById('loginF').style.display='none';document.getElementById('otpF').style.display='block';},900);
}

function doRegister(){
  const fields=[
    ['rname',v=>v.length>=2,'Full name is required'],
    ['rfname',v=>v.length>=2,'Father name is required'],
    ['rmob',v=>/^0\d{10}$/.test(v),'Enter valid 11-digit mobile (e.g. 0300XXXXXXX)'],
    ['rcnic',v=>/^\d{5}-\d{7}-\d$/.test(v),'Format: 12345-1234567-1'],
    ['rprov',v=>v!=='','Please select a province'],
    ['rdist',v=>v.length>=2,'District is required'],
    ['racres',v=>parseFloat(v)>0,'Enter farm area in acres'],
    ['rcrop',v=>v!=='','Please select your main crop'],
    ['rirr',v=>v!=='','Please select irrigation source'],
    ['rpass',v=>v.length>=6,'Password must be minimum 6 characters'],
  ];
  let ok=true;
  fields.forEach(([id,fn,msg])=>{
    const val=(document.getElementById(id)||{}).value||'';
    const valid=fn(val.trim());
    markInput(id,!valid);
    const eEl=document.getElementById(id+'Err');
    if(eEl){eEl.textContent=msg;showErr(id+'Err',!valid);}
    if(!valid)ok=false;
  });
  const mob=document.getElementById('rmob').value.trim();
  if(APP_STATE.users[mob]){
    markInput('rmob',true);
    document.getElementById('rmobErr').textContent='This mobile is already registered. Please login.';
    showErr('rmobErr',true);ok=false;
  }
  const p=document.getElementById('rpass').value;
  const cp=document.getElementById('rcpass').value;
  if(p!==cp){markInput('rcpass',true);showErr('rcpassErr',true);ok=false;}
  if(!ok)return;
  // Save new user
  APP_STATE.users[mob]={
    name:document.getElementById('rname').value.trim(),
    fname:document.getElementById('rfname').value.trim(),
    mob:mob,
    cnic:document.getElementById('rcnic').value.trim(),
    province:document.getElementById('rprov').value,
    district:document.getElementById('rdist').value.trim(),
    acres:document.getElementById('racres').value.trim(),
    crop:document.getElementById('rcrop').value,
    irr:document.getElementById('rirr').value,
    pass:p
  };
  APP_STATE.currentUser=mob;
  saveState();
  showLoader();
  setTimeout(()=>{hideLoader();document.getElementById('regF').style.display='none';document.getElementById('otpF').style.display='block';},900);
}

function onext(inp,nextIdx){if(inp.value.length===1&&nextIdx<=6){const n=document.getElementById('o'+nextIdx);if(n)n.focus();}}
function oback(e,inp,prevIdx){if(e.key==='Backspace'&&inp.value===''&&prevIdx>=1){const p=document.getElementById('o'+prevIdx);if(p){p.value='';p.focus();}}}
function checkOTP(){
  const code=['o1','o2','o3','o4','o5','o6'].map(id=>(document.getElementById(id)||{}).value||'').join('');
  if(code===DEMO_OTP)document.getElementById('otpBtn').style.background='linear-gradient(135deg,#16a34a,#22c55e)';
}

function enterApp(){
  const code=['o1','o2','o3','o4','o5','o6'].map(id=>(document.getElementById(id)||{}).value||'').join('');
  if(code!==DEMO_OTP){toast('❌ Wrong OTP! Use: 1 2 3 4 5 6');return;}
  showLoader();
  setTimeout(()=>{
    hideLoader();
    document.getElementById('authScreen').style.display='none';
    document.getElementById('app').style.display='block';
    initApp();
    const u=getUser();
    toast('✅ Welcome, '+(u?u.name:'Kisan')+'!');
  },1200);
}

function getUser(){return APP_STATE.users[APP_STATE.currentUser]||null;}

function doLogout(){
  if(DC.raf){cancelAnimationFrame(DC.raf);DC.raf=null;}
  document.getElementById('app').style.display='none';
  document.getElementById('authScreen').style.display='block';
  atab('login');
  toast('👋 Logged out successfully');
}

// ============================================================
// APP INIT
// ============================================================
function initApp(){
  setGreeting();
  populateUserUI();
  renderActivities();
  renderTransactions();
  loadWeather();
  renderPrices();
  renderDroneList();
  initDroneCanvas();
  if(!APP_STATE.selectedDrone)APP_STATE.selectedDrone=DRONES[0];
  updateDroneLabel();
}

function populateUserUI(){
  const u=getUser();
  if(!u)return;
  const initials=u.name.split(' ').map(n=>n[0]).join('').substring(0,2).toUpperCase();
  document.getElementById('userAvatar').textContent=initials;
  document.getElementById('sbName').textContent=u.name;
  document.getElementById('sbCnic').textContent=(u.cnic||'--')+' • '+(u.province||'--');
  document.getElementById('sbFarm').textContent='📍 '+(u.district||'--')+', '+(u.province||'--')+' • '+(u.acres||'--')+' Acres • '+(u.crop||'--');
  document.getElementById('greetName').textContent='Assalam-o-Alaikum, '+u.name.split(' ')[0]+'! 👋';
  document.getElementById('dashAcresChip').textContent='🌾 '+(u.acres||'--')+' Acres';
  document.getElementById('dashLocChip').textContent='📍 '+(u.district||'--');
  document.getElementById('dashTotalAcres').textContent=u.acres||'--';
  const ha=parseFloat(u.acres)||12;
  document.getElementById('coveredAcresText').textContent='0/'+ha+' acres';
  document.getElementById('totalAcresText').textContent=ha+' acres';
  document.getElementById('profileName').textContent=u.name;
  document.getElementById('profileCnic').textContent='CNIC: '+(u.cnic||'--');
  document.getElementById('profileAcresChip').textContent='🌾 '+(u.acres||'--')+' Acres';
  document.getElementById('profileMob').textContent=u.mob||'--';
  document.getElementById('profileLoc').textContent=(u.district||'--')+', '+(u.province||'--');
  document.getElementById('profileFarm').textContent=(u.acres||'--')+' Acres • '+(u.crop||'--');
  document.getElementById('profileIrr').textContent=u.irr||'--';
  const ha2=parseFloat(u.acres)||12;
  const fa=Math.round(ha2*0.6),fb=Math.round(ha2*0.4);
  document.getElementById('fieldACrop').textContent=u.crop||'Wheat';
  document.getElementById('fieldBCrop').textContent=u.crop==='Cotton'?'Wheat':'Cotton';
  document.getElementById('fieldASize').textContent=fa+' Acres';
  document.getElementById('fieldBSize').textContent=fb+' Acres';
  document.getElementById('fieldALabel').textContent='FIELD A — '+fa+' Acres';
  document.getElementById('fieldBLabel').textContent='FIELD B — '+fb+' Acres';
  document.getElementById('fieldAAddr').textContent='Plot #34-B, '+u.district;
  document.getElementById('fieldBAddr').textContent='Plot #67-A, '+u.district;
  document.getElementById('mapTotalAcres').textContent=u.acres||'--';
  const aiField=document.getElementById('aiFieldA');
  if(aiField)aiField.textContent='Field A — '+(u.crop||'Wheat');
}

function setGreeting(){
  const h=new Date().getHours();
  const g=h<12?'Good Morning ☀️':h<17?'Good Afternoon 🌤️':'Good Evening 🌙';
  const el=document.getElementById('gtime');
  if(el)el.textContent=g;
}

// ============================================================
// NAVIGATION
// ============================================================
const pageTitles={dashboard:'🏡 Dashboard',drone:'🚁 Drone Control',fields:'🗺️ Field Map',weather:'🌤️ Weather',ai:'🤖 AI Advisor',resources:'💰 Resources',prices:'📈 Crop Prices',machinery:'🚜 Machinery',experts:'👨‍🌾 Experts',profile:'👤 Profile',settings:'⚙️ Settings'};

function nav(name){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('on'));
  const pg=document.getElementById('pg-'+name);
  if(pg)pg.classList.add('on');
  document.getElementById('ptitle').textContent=pageTitles[name]||name;
  document.querySelectorAll('.bni').forEach(b=>b.classList.remove('on'));
  const bn=document.getElementById('bn-'+name);
  if(bn)bn.classList.add('on');
  document.querySelectorAll('.ni').forEach(n=>n.classList.remove('on'));
  if(name==='drone')setTimeout(()=>initDroneCanvas(),100);
  if(name==='weather')loadWeather();
  if(name==='prices')renderPrices();
  if(name==='profile')populateUserUI();
  if(name==='resources')renderTransactions();
}

function toggleSB(){
  document.getElementById('sb').classList.toggle('on');
  document.getElementById('sov').classList.toggle('on');
}

// ============================================================
// TOAST / LOADER / MODAL
// ============================================================
function toast(msg){
  const t=document.getElementById('toast');
  t.textContent=msg;t.classList.add('on');
  clearTimeout(t._t);
  t._t=setTimeout(()=>t.classList.remove('on'),2800);
}
function showLoader(){document.getElementById('loader').classList.add('on');}
function hideLoader(){document.getElementById('loader').classList.remove('on');}
function openModal(id){document.getElementById(id).classList.add('on');}
function closeModal(id){document.getElementById(id).classList.remove('on');}

// ============================================================
// ACTIVITIES
// ============================================================
function openAddActivity(){
  document.getElementById('actDate').value=new Date().toISOString().slice(0,16);
  openModal('modal-activity');
}
function saveActivity(){
  const type=document.getElementById('actType').value;
  const desc=document.getElementById('actDesc').value.trim()||'Activity recorded';
  const field=document.getElementById('actField').value;
  const date=document.getElementById('actDate').value;
  const ts=date?new Date(date):new Date();
  const label=ts.toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'});
  if(!APP_STATE.activities)APP_STATE.activities=[];
  APP_STATE.activities.unshift({type,desc,field,label,ts:ts.getTime()});
  if(APP_STATE.activities.length>50)APP_STATE.activities=APP_STATE.activities.slice(0,50);
  saveState();
  renderActivities();
  closeModal('modal-activity');
  toast('✅ Activity saved!');
}
function renderActivities(){
  const list=document.getElementById('activityList');
  if(!list)return;
  const acts=APP_STATE.activities||[];
  if(acts.length===0){
    list.innerHTML='<div style="padding:18px;text-align:center;color:var(--tm);font-size:14px">No activities yet. Press + Add to begin.</div>';
    return;
  }
  const recent=acts.slice(0,8);
  const colors={
    '🚁':'var(--gpal)','💧':'var(--skyl)','🌱':'var(--gpal)','🧪':'var(--redl)',
    '🌾':'var(--goldl)','🚜':'var(--goldl)','🌧️':'var(--skyl)','📊':'var(--purl)'
  };
  list.innerHTML=recent.map(a=>`
    <div class="exp-item">
      <div class="exp-ico" style="background:${colors[a.type]||'var(--surf)'}">${a.type}</div>
      <div><div style="font-size:14px;font-weight:600">${a.desc}</div><div style="font-size:12px;color:var(--tm)">${a.field} • ${a.label}</div></div>
    </div>
  `).join('');
}

// ============================================================
// TRANSACTIONS / FINANCE
// ============================================================
function openAddTransaction(){
  document.getElementById('txDate').value=new Date().toISOString().slice(0,10);
  openModal('modal-transaction');
}
function saveTransaction(){
  const type=document.getElementById('txType').value;
  const cat=document.getElementById('txCat').value;
  const desc=document.getElementById('txDesc').value.trim();
  const amt=parseFloat(document.getElementById('txAmount').value);
  const date=document.getElementById('txDate').value;
  showErr('txAmtErr',false);
  if(!amt||amt<=0){showErr('txAmtErr',true);return;}
  if(!APP_STATE.transactions)APP_STATE.transactions=[];
  const label=date?new Date(date).toLocaleDateString('en-PK',{dateStyle:'medium'}):new Date().toLocaleDateString('en-PK',{dateStyle:'medium'});
  APP_STATE.transactions.unshift({type,cat,desc:desc||cat,amt,label,ts:Date.now()});
  saveState();
  renderTransactions();
  closeModal('modal-transaction');
  toast(type==='income'?'💰 Income added!':'📤 Expense saved!');
}
function renderTransactions(){
  const list=document.getElementById('transactionList');
  if(!list)return;
  const txs=APP_STATE.transactions||[];
  const income=txs.filter(t=>t.type==='income').reduce((s,t)=>s+t.amt,0);
  const expenses=txs.filter(t=>t.type==='expense').reduce((s,t)=>s+t.amt,0);
  const net=income-expenses;
  const fmt=v=>'₨'+v.toLocaleString('en-PK');
  document.getElementById('totalIncome').textContent=fmt(income);
  document.getElementById('totalExpenses').textContent=fmt(expenses);
  document.getElementById('netProfit').textContent=fmt(net);
  document.getElementById('dashProfit').textContent=fmt(net>0?net:0);
  const pct=income>0?Math.round((net/income)*100):0;
  document.getElementById('profitNote').textContent=net>=0?`💰 Margin: ${pct}% — ${pct>50?'Excellent':'Good'}`:'⚠️ Spending more than income';
  const laborTx=txs.filter(t=>t.cat==='Labor').reduce((s,t)=>s+t.amt,0);
  document.getElementById('resLabor').textContent=fmt(laborTx);
  const laborPct=laborTx>0?Math.min(100,Math.round((laborTx/Math.max(expenses,1))*100)):0;
  const lb=document.getElementById('laborBar');if(lb)lb.style.width=laborPct+'%';
  if(txs.length===0){
    list.innerHTML='<div style="padding:18px;text-align:center;color:var(--tm);font-size:14px">No transactions yet. Press + Add to record expenses or income.</div>';
    return;
  }
  const catIcons={
    'Crop Sale':'💰','Chemicals':'🧪','Fertilizer':'🌱','Fuel':'⛽',
    'Labor':'👷','Equipment Rental':'🚜','Drone Service':'🚁','Seeds':'🌰','Other':'📦'
  };
  const catColors={
    'Crop Sale':'var(--gpal)','Chemicals':'var(--redl)','Fertilizer':'var(--goldl)',
    'Fuel':'var(--skyl)','Labor':'var(--purl)','Equipment Rental':'var(--goldl)',
    'Drone Service':'var(--gpal)','Seeds':'var(--goldl)','Other':'var(--surf)'
  };
  list.innerHTML=txs.slice(0,15).map(t=>`
    <div class="exp-item">
      <div class="exp-ico" style="background:${catColors[t.cat]||'var(--surf)'}">${catIcons[t.cat]||'📦'}</div>
      <div style="flex:1"><div style="font-size:14px;font-weight:600">${t.desc}</div><div style="font-size:11px;color:var(--tm)">${t.cat} • ${t.label}</div></div>
      <div style="color:${t.type==='income'?'var(--gl)':'var(--red)'};font-weight:700">${t.type==='income'?'+':'-'}${fmt(t.amt)}</div>
    </div>
  `).join('');
}

// ============================================================
// EDIT PROFILE
// ============================================================
function openEditProfile(){
  const u=getUser();if(!u)return;
  document.getElementById('epName').value=u.name||'';
  document.getElementById('epFname').value=u.fname||'';
  document.getElementById('epDist').value=u.district||'';
  document.getElementById('epProv').value=u.province||'Punjab';
  document.getElementById('epAcres').value=u.acres||'';
  document.getElementById('epCrop').value=u.crop||'Wheat';
  document.getElementById('epIrr').value=u.irr||'Canal Water';
  openModal('modal-editprofile');
}
function saveProfile(){
  const u=getUser();if(!u)return;
  u.name=document.getElementById('epName').value.trim()||u.name;
  u.fname=document.getElementById('epFname').value.trim()||u.fname;
  u.district=document.getElementById('epDist').value.trim()||u.district;
  u.province=document.getElementById('epProv').value||u.province;
  u.acres=document.getElementById('epAcres').value||u.acres;
  u.crop=document.getElementById('epCrop').value||u.crop;
  u.irr=document.getElementById('epIrr').value||u.irr;
  APP_STATE.users[APP_STATE.currentUser]=u;
  saveState();
  populateUserUI();
  closeModal('modal-editprofile');
  toast('✅ Profile updated!');
}

// ============================================================
// SETTINGS
// ============================================================
function toggleSetting(el,key){
  el.classList.toggle('on');
  APP_STATE.settings[key]=el.classList.contains('on');
  saveState();
  const msgs={
    pest:'🔔 Pest alerts '+(APP_STATE.settings.pest?'ON':'OFF'),
    weather:'🌤️ Weather alerts '+(APP_STATE.settings.weather?'ON':'OFF'),
    price:'📈 Price alerts '+(APP_STATE.settings.price?'ON':'OFF'),
    drone:'🚁 Drone alerts '+(APP_STATE.settings.drone?'ON':'OFF'),
    dark:'🌙 Dark mode '+(APP_STATE.settings.dark?'ON':'OFF'),
    urdu:'🇵🇰 Urdu labels '+(APP_STATE.settings.urdu?'ON':'OFF'),
    gps:'📍 GPS '+(APP_STATE.settings.gps?'ON':'OFF'),
  };
  toast(msgs[key]||'Setting saved');
}
function clearAllData(){
  if(confirm('Clear all data? Your account will remain.')){
    APP_STATE.activities=[];APP_STATE.transactions=[];
    saveState();renderActivities();renderTransactions();
    toast('🗑️ Data cleared');
  }
}
function exportReport(){
  const u=getUser();
  const txs=APP_STATE.transactions||[];
  const income=txs.filter(t=>t.type==='income').reduce((s,t)=>s+t.amt,0);
  const expenses=txs.filter(t=>t.type==='expense').reduce((s,t)=>s+t.amt,0);
  const report=`Kisan Ka Pakistan — Farm Report\n==================\nFarmer: ${u?.name}\nCNIC: ${u?.cnic}\nFarm: ${u?.acres} Acres, ${u?.crop}\n\nFinance Summary:\nIncome: Rs ${income.toLocaleString()}\nExpenses: Rs ${expenses.toLocaleString()}\nNet Profit: Rs ${(income-expenses).toLocaleString()}\n\nTransactions: ${txs.length}\n\nGenerated: ${new Date().toLocaleString()}`;
  const blob=new Blob([report],{type:'text/plain'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='farm-report.txt';a.click();
  toast('📋 Report exported!');
}

// ============================================================
// DRONE SELECTOR
// ============================================================
function openDroneSelector(){renderDroneList();openModal('modal-drone');}
function renderDroneList(){
  const list=document.getElementById('droneList');
  if(!list)return;
  list.innerHTML=DRONES.map(d=>`
    <div class="drone-item ${APP_STATE.selectedDrone?.id===d.id?'selected':''}" onclick="selectDrone('${d.id}')">
      <div class="drone-ico">${d.icon}</div>
      <div style="flex:1">
        <div style="color:#fff;font-size:14px;font-weight:700">${d.name}</div>
        <div style="color:rgba(255,255,255,.5);font-size:12px">Tank: ${d.tank}L • Range: ${d.range}</div>
      </div>
      <div style="text-align:right">
        <div style="color:#2ecc71;font-size:13px;font-weight:700">🔋${d.bat}%</div>
        ${APP_STATE.selectedDrone?.id===d.id?'<div style="color:#2ecc71;font-size:10px;font-weight:700">CONNECTED</div>':''}
      </div>
    </div>
  `).join('');
}
function selectDrone(id){
  APP_STATE.selectedDrone=DRONES.find(d=>d.id===id)||DRONES[0];
  DC.bat=APP_STATE.selectedDrone.bat;
  DC.tank=64;
  renderDroneList();
}
function confirmDrone(){
  updateDroneLabel();
  closeModal('modal-drone');
  toast('✅ '+APP_STATE.selectedDrone.name+' connected!');
  if(!APP_STATE.activities)APP_STATE.activities=[];
  APP_STATE.activities.unshift({type:'🚁',desc:APP_STATE.selectedDrone.name+' connected',field:'All Fields',label:new Date().toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'}),ts:Date.now()});
  saveState();renderActivities();
}
function updateDroneLabel(){
  const d=APP_STATE.selectedDrone;
  if(d)document.getElementById('droneModelLabel').textContent=d.name+' • Connected';
}

// ============================================================
// MAPS
// ============================================================
function openFullMap(){
  const u=getUser();
  const loc=encodeURIComponent((u?.district||'Multan')+', '+(u?.province||'Punjab')+', Pakistan farmland agriculture');
  window.open('https://www.google.com/maps/search/'+loc+'/@30.1865,71.4911,14z/data=!3m1!4b1!4m3!2m2!5m1!4e1','_blank');
  toast('🗺️ Opening Google Maps...');
}

// ============================================================
// WEATHER — Real-time using Open-Meteo (free, no key needed)
// ============================================================
let weatherData = null;
async function loadWeather(){
  const u=getUser();
  // Coords for major Pakistani cities
  const cityCoords = {
    'Multan':{lat:30.1865,lng:71.4911},
    'Lahore':{lat:31.5204,lng:74.3587},
    'Karachi':{lat:24.8607,lng:67.0011},
    'Faisalabad':{lat:31.4504,lng:73.135},
    'Rawalpindi':{lat:33.5651,lng:73.0169},
    'Hyderabad':{lat:25.396,lng:68.3578},
    'Peshawar':{lat:34.0151,lng:71.5249},
    'Quetta':{lat:30.1798,lng:66.975},
  };
  const district=u?.district||'Multan';
  const coords=cityCoords[district]||cityCoords['Multan'];
  const cityName=district+', '+(u?.province||'Punjab');

  try {
    const url=`https://api.open-meteo.com/v1/forecast?latitude=${coords.lat}&longitude=${coords.lng}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code,uv_index&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weather_code&hourly=temperature_2m&timezone=Asia%2FKarachi&forecast_days=7`;
    const r=await fetch(url);
    const d=await r.json();
    weatherData=d;
    updateWeatherUI(d,cityName,coords);
  } catch(e) {
    // Fallback to simulated weather
    updateWeatherFallback(cityName);
  }
}

function wmoToEmoji(code){
  if(code===0)return'☀️';if(code<=2)return'🌤️';if(code<=3)return'☁️';
  if(code<=49)return'🌫️';if(code<=67)return'🌧️';if(code<=77)return'🌨️';
  if(code<=82)return'🌦️';if(code<=99)return'⛈️';return'🌤️';
}
function wmoToDesc(code){
  if(code===0)return'Clear Sky';if(code<=2)return'Partly Cloudy';if(code<=3)return'Overcast';
  if(code<=49)return'Foggy';if(code<=67)return'Rainy';if(code<=77)return'Snowy';
  if(code<=82)return'Showers';if(code<=99)return'Thunderstorm';return'Partly Cloudy';
}

function updateWeatherUI(d,cityName,coords){
  const c=d.current;
  const temp=Math.round(c.temperature_2m);
  const hum=Math.round(c.relative_humidity_2m);
  const wind=Math.round(c.wind_speed_10m);
  const uv=Math.round(c.uv_index||5);
  const code=c.weather_code;
  const emoji=wmoToEmoji(code);
  const desc=wmoToDesc(code);

  // Dashboard
  const dLoc=document.getElementById('dashWeatherLoc');
  const dTemp=document.getElementById('dashTemp');
  const dDesc=document.getElementById('dashWeatherDesc');
  const dMeta=document.getElementById('dashWeatherMeta');
  if(dLoc)dLoc.textContent='📍 '+cityName;
  if(dTemp)dTemp.textContent=temp+'°';
  if(dDesc)dDesc.textContent=emoji+' '+desc;
  if(dMeta)dMeta.innerHTML=`<div style="color:rgba(255,255,255,.85);font-size:12px">💧 ${hum}% Humidity</div><div style="color:rgba(255,255,255,.85);font-size:12px">💨 ${wind} km/h</div><div style="color:rgba(255,255,255,.85);font-size:12px">UV${uv}</div>`;

  // Weather page
  const wCity=document.getElementById('weatherCity');
  const wTemp=document.getElementById('weatherTemp');
  const wDesc=document.getElementById('weatherDesc');
  const wHum=document.getElementById('wHumidity');
  const wWind=document.getElementById('wWind');
  const wUV=document.getElementById('wUV');
  if(wCity)wCity.textContent='📍 '+cityName;
  if(wTemp)wTemp.textContent=temp+'°';
  if(wDesc)wDesc.textContent=emoji+' '+desc;
  if(wHum)wHum.textContent=hum+'%';
  if(wWind)wWind.textContent=wind;
  if(wUV)wUV.textContent='UV'+uv;

  // Spray alert
  const sa=document.getElementById('weatherSprayAlert');
  const windAlert=document.getElementById('windAlert');
  if(wind>25){
    const msg='🌬️ High wind ('+wind+' km/h) — Do NOT spray today!';
    if(sa){sa.className='alert alert-bad';sa.textContent=msg;}
    if(windAlert){windAlert.textContent=msg;}
  } else if(wind>15){
    const msg='⚠️ Wind '+wind+' km/h — Delay spraying 2 hours';
    if(sa){sa.className='alert alert-warn';sa.textContent=msg;}
    if(windAlert){windAlert.textContent=msg;}
  } else {
    const msg='✅ Wind '+wind+' km/h — Safe to spray now!';
    if(sa){sa.className='alert alert-ok';sa.textContent=msg;}
    if(windAlert){windAlert.className='alert alert-ok';windAlert.textContent=msg;}
  }
  document.getElementById('tWind').textContent=wind+'km/h';

  // 7-day forecast
  const fr=document.getElementById('forecastRow');
  if(fr&&d.daily){
    const days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    fr.innerHTML=d.daily.weather_code.slice(0,7).map((wc,i)=>{
      const dt=new Date(d.daily.time[i]);
      const dayLbl=i===0?'Today':days[dt.getDay()];
      return`<div class="fday"><div style="font-size:11px;font-weight:600;color:var(--tm)">${dayLbl}</div><div style="font-size:22px">${wmoToEmoji(wc)}</div><div style="font-size:13px;font-weight:700;margin-top:4px">${Math.round(d.daily.temperature_2m_max[i])}/${Math.round(d.daily.temperature_2m_min[i])}°</div><div style="font-size:10px;color:var(--sky);margin-top:2px">💧${d.daily.precipitation_probability_max[i]}%</div></div>`;
    }).join('');
  }

  // Spray checker
  const sc=document.getElementById('sprayCheckerList');
  if(sc){
    const windStatus=wind>25?'chip-r':wind>15?'chip-gold':'chip-g';
    const windIcon=wind>25?'🚫':wind>15?'⚠️':'✅';
    const rain=d.daily?.precipitation_probability_max[0]||0;
    const rainStatus=rain>60?'chip-r':rain>30?'chip-gold':'chip-g';
    const tempStatus=temp>38||temp<10?'chip-gold':'chip-g';
    const humStatus=hum>85?'chip-gold':'chip-g';
    sc.innerHTML=`
      <div style="display:flex;justify-content:space-between"><span style="font-size:14px">💨 Wind</span><span class="chip ${windStatus}">${windIcon} ${wind} km/h</span></div>
      <div style="display:flex;justify-content:space-between"><span style="font-size:14px">🌧️ Rain Risk</span><span class="chip ${rainStatus}">${rain>60?'🚫':rain>30?'⚠️':'✅'} ${rain}%</span></div>
      <div style="display:flex;justify-content:space-between"><span style="font-size:14px">🌡️ Temperature</span><span class="chip ${tempStatus}">${temp>38?'⚠️':'✅'} ${temp}°C</span></div>
      <div style="display:flex;justify-content:space-between"><span style="font-size:14px">💧 Humidity</span><span class="chip ${humStatus}">${hum>85?'⚠️':'✅'} ${hum}%</span></div>
      <div class="alert ${wind>25?'alert-bad':wind>15?'alert-warn':'alert-ok'}" style="margin-bottom:0">⏰ ${wind>25?'Postpone spraying today':'Best spray: 6–9 AM or after 4 PM'}</div>
    `;
  }

  // Hourly chart
  buildHourlyChart(d,temp);
}

function buildHourlyChart(d,baseTemp){
  const chart=document.getElementById('hourlyChart');
  if(!chart)return;
  const now=new Date();
  const hours=d.hourly?.time?.slice(0,24)||[];
  // Get 6 representative hours
  const indices=[6,9,12,15,18,21];
  const temps=indices.map(h=>d.hourly?.temperature_2m?.[h]||baseTemp);
  const minT=Math.min(...temps)-2,maxT=Math.max(...temps)+2;
  chart.innerHTML=temps.map((t,i)=>{
    const pct=Math.round(((t-minT)/(maxT-minT))*80)||20;
    const color=t>35?'#ef4444':t>28?'#f59e0b':'#2ecc71';
    return`<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:3px">
      <div style="font-size:10px;color:var(--ts);font-weight:600">${Math.round(t)}°</div>
      <div style="width:100%;background:${color};border-radius:4px 4px 0 0;height:${pct}%;min-height:8px;opacity:.8"></div>
    </div>`;
  }).join('');
}

function updateWeatherFallback(cityName){
  const baseTemp=32+Math.floor(Math.random()*8);
  const hum=50+Math.floor(Math.random()*30);
  const wind=10+Math.floor(Math.random()*20);
  updateWeatherUI({
    current:{temperature_2m:baseTemp,relative_humidity_2m:hum,wind_speed_10m:wind,weather_code:1,uv_index:7},
    daily:{time:['','','','','','',''],weather_code:[1,2,61,80,0,0,2],temperature_2m_max:[baseTemp+2,baseTemp-1,baseTemp-4,baseTemp,baseTemp+3,baseTemp+4,baseTemp+1],temperature_2m_min:[baseTemp-10,baseTemp-11,baseTemp-12,baseTemp-10,baseTemp-9,baseTemp-8,baseTemp-10],precipitation_probability_max:[20,30,70,60,15,10,25]},
    hourly:{time:[],temperature_2m:Array(24).fill(0).map((_,i)=>baseTemp+Math.sin(i/4)*5)}
  },cityName,{lat:30.18,lng:71.49});
}

// ============================================================
// CROP PRICES
// ============================================================
const CROP_PRICES=[
  {name:'Wheat (گندم)',emoji:'🌾',price:4200,change:3.2,positive:true,market:'Multan Grain Mandi'},
  {name:'Cotton (کپاس)',emoji:'🌿',price:8800,change:-1.5,positive:false,market:'Multan Cotton Market'},
  {name:'Maize (مکئی)',emoji:'🌽',price:2100,change:5.1,positive:true,market:'Faisalabad Market'},
  {name:'Rice (چاول)',emoji:'🍚',price:5400,change:0.8,positive:true,market:'Lahore Rice Mandi'},
  {name:'Sugarcane (گنا)',emoji:'🎋',price:420,change:-2.1,positive:false,market:'Faisalabad'},
];
function renderPrices(){
  const u=getUser();
  const list=document.getElementById('priceList');
  if(!list)return;
  const now=new Date();
  document.getElementById('priceUpdateTime').textContent='Live Mandi Prices • Updated '+now.toLocaleTimeString('en-PK',{hour:'2-digit',minute:'2-digit'});
  list.innerHTML=CROP_PRICES.map(c=>{
    const sparkPts=c.positive?'0,35 40,28 80,30 110,18 150,12 200,8':'0,10 40,14 80,8 110,18 150,22 200,28';
    const clr=c.positive?'#27ae60':'#ef4444';
    return`<div class="card" style="padding:15px">
      <div style="display:flex;align-items:center;gap:13px">
        <div style="font-size:38px">${c.emoji}</div>
        <div style="flex:1"><div style="font-size:15px;font-weight:700">${c.name}</div><div style="font-size:12px;color:var(--tm)">${c.market}</div></div>
        <div style="text-align:right">
          <div style="font-size:20px;font-weight:800">₨${c.price.toLocaleString()}</div>
          <div style="color:${clr};font-size:12px;font-weight:700">${c.positive?'▲':'▼'} ${Math.abs(c.change)}%</div>
        </div>
      </div>
      <svg viewBox="0 0 200 40" fill="none" style="width:100%;height:40px;margin-top:10px">
        <polyline points="${sparkPts}" stroke="${clr}" stroke-width="2"/>
        <polyline points="${sparkPts} 200,40 0,40" fill="${clr}11"/>
      </svg>
    </div>`;
  }).join('');
  // AI tip based on user's crop
  const crop=u?.crop||'Wheat';
  const cp=CROP_PRICES.find(c=>c.name.includes(crop))||CROP_PRICES[0];
  const tipEl=document.getElementById('priceAITip');
  if(tipEl){
    if(cp.positive)tipEl.textContent='💡 AI: '+crop+' prices rising (+'+cp.change+'%) — hold stock for better returns!';
    else tipEl.textContent='⚠️ AI: '+crop+' prices falling ('+cp.change+'%) — consider selling soon.';
  }
}

// ============================================================
// AI ADVISOR — Powered by Anthropic API
// ============================================================
let aiConversation=[];
let aiTyping=false;

async function aiSend(){
  if(aiTyping)return;
  const inp=document.getElementById('aiInp');
  const msgs=document.getElementById('aiMsgs');
  const sendBtn=document.getElementById('aiSendBtn');
  if(!inp||!msgs||!inp.value.trim())return;
  const userMsg=inp.value.trim();
  inp.value='';

  const u=getUser();
  const um=document.createElement('div');
  um.className='amsg amsg-u';
  um.innerHTML=userMsg+'<span style="display:block;font-size:10px;opacity:.7;margin-top:4px">Just now</span>';
  msgs.appendChild(um);
  msgs.scrollTop=msgs.scrollHeight;

  // Typing indicator
  const typingEl=document.createElement('div');
  typingEl.className='amsg amsg-b';
  typingEl.innerHTML='<div class="typing-dots"><span></span><span></span><span></span></div>';
  msgs.appendChild(typingEl);
  msgs.scrollTop=msgs.scrollHeight;
  aiTyping=true;
  sendBtn.style.opacity='0.5';

  aiConversation.push({role:'user',content:userMsg});

  const systemPrompt=`You are an AI farming advisor for Pakistani farmers. The farmer's details:
- Name: ${u?.name||'Farmer'}
- Location: ${u?.district||'Multan'}, ${u?.province||'Punjab'}, Pakistan
- Farm: ${u?.acres||'12'} acres, Main crop: ${u?.crop||'Wheat'}
- Irrigation: ${u?.irr||'Canal Water'}

You help with: pest control, fertilizers, irrigation, crop diseases, mandi prices, drone usage, weather-based advice, government schemes for farmers.
Always give practical, actionable advice for Pakistani conditions. 
Use Urdu words naturally (e.g., asan, theek, accha, kisan, khet).
Keep responses concise (2-4 lines). Be helpful and encouraging.
When mentioning chemicals/pesticides, give local Pakistani brand names when possible.`;

  try {
    const response=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:400,
        system:systemPrompt,
        messages:aiConversation.slice(-8)
      })
    });
    const data=await response.json();
    let reply='Sorry, could not get response. Please try again.';
    if(data.content&&data.content[0]){
      reply=data.content[0].text||reply;
      aiConversation.push({role:'assistant',content:reply});
    }
    typingEl.innerHTML=reply+'<span style="display:block;font-size:10px;opacity:.5;margin-top:4px">Just now</span>';
  } catch(e) {
    // Fallback responses for Pakistani farming
    const fallbacks=[
      u?.crop==='Cotton'?
        'Cotton mein aphid (تیلہ) ka risk hai! Imidacloprid 70% — 100g/acre spray karein. Subah 6-9 baje best time hai. 🌿':
        'Wheat ki growth ke liye Urea 50 kg/acre apply karein. Drone spraying 3x zyada effective hoti hai! 🌾',
      'Rain forecast hai — Monday tak spraying complete kar lein. Best time: Subah ya shaam. ☔',
      'Soil moisture check karein. Agar 40% se kam hai toh 1.5 ghante irrigation lagaein. 💧',
      'Multan mandi mein '+u?.crop+' prices stable hain. AI forecast: '+((Math.random()>0.5)?'agle 2 haftay mein +8-12% increase hogi.':'pichle rates par stable rahein ge. Monitor daily.'),
      'Aapka drone 87% battery pe hai. Auto-mission start karne ke liye Field A se begin karein. 🚁'
    ];
    const reply=fallbacks[Math.floor(Math.random()*fallbacks.length)];
    aiConversation.push({role:'assistant',content:reply});
    typingEl.innerHTML=reply+'<span style="display:block;font-size:10px;opacity:.5;margin-top:4px">Just now</span>';
  }

  aiTyping=false;
  sendBtn.style.opacity='1';
  msgs.scrollTop=msgs.scrollHeight;
}

function scheduleDroneSpray(){
  if(!APP_STATE.activities)APP_STATE.activities=[];
  APP_STATE.activities.unshift({
    type:'🚁',
    desc:'Spray mission scheduled — Field B Cotton (Aphid control)',
    field:'Field B',
    label:new Date().toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'}),
    ts:Date.now()
  });
  saveState();renderActivities();
  toast('🚁 Drone spray mission scheduled for Field B!');
}

// ============================================================
// DRONE ENGINE
// ============================================================
let DC={
  x:0,y:0,vx:0,vy:0,
  alt:25,bat:87,tank:64,speed:0,heading:0,
  isFlying:false,isLanded:true,
  sprayOn:false,sprayRate:5,sprayPattern:'full',
  flightMode:'idle',
  autoPath:[],autoPathIdx:0,coverage:0,
  jLX:0,jLY:0,jRX:0,jRY:0,
  canvas:null,ctx:null,raf:null,
  sprayParticles:[],exhaustParticles:[],
  rotorAngle:0,trailPoints:[],sprayedZones:[],
  W:0,H:0,fieldX:0,fieldY:0,fieldW:0,fieldH:0,
  missionStart:null,missionAcres:0,
};

function initDroneCanvas(){
  const canvas=document.getElementById('droneCanvas');
  if(!canvas)return;
  if(DC.raf){cancelAnimationFrame(DC.raf);DC.raf=null;}
  DC.canvas=canvas;DC.ctx=canvas.getContext('2d');
  const dpr=window.devicePixelRatio||1;
  const rect=canvas.getBoundingClientRect();
  DC.W=rect.width||canvas.offsetWidth||360;DC.H=320;
  canvas.width=DC.W*dpr;canvas.height=DC.H*dpr;
  canvas.style.width=DC.W+'px';canvas.style.height=DC.H+'px';
  DC.ctx.scale(dpr,dpr);
  DC.fieldX=40;DC.fieldY=30;DC.fieldW=DC.W-80;DC.fieldH=DC.H-60;
  if(DC.x===0&&DC.y===0){DC.x=DC.fieldX+DC.fieldW/2;DC.y=DC.fieldY+DC.fieldH-20;}
  if(APP_STATE.selectedDrone){DC.bat=APP_STATE.selectedDrone.bat;}
  generateAutoPath();setupJoysticks();startDroneLoop();
}

function generateAutoPath(){
  DC.autoPath=[];
  const rows=7;const step=DC.fieldH/(rows+1);
  for(let r=0;r<=rows;r++){
    const rowY=DC.fieldY+step*(r+0.5);
    if(r%2===0){DC.autoPath.push({x:DC.fieldX+10,y:rowY});DC.autoPath.push({x:DC.fieldX+DC.fieldW-10,y:rowY});}
    else{DC.autoPath.push({x:DC.fieldX+DC.fieldW-10,y:rowY});DC.autoPath.push({x:DC.fieldX+10,y:rowY});}
  }
  DC.autoPathIdx=0;
}

function startDroneLoop(){
  function loop(){DC.raf=requestAnimationFrame(loop);updateDrone();renderDrone();}
  loop();
}

function updateDrone(){
  DC.rotorAngle+=DC.isFlying?0.25:0.05;
  if(DC.flightMode==='auto'&&DC.isFlying)autoFly();
  else if(DC.flightMode==='hover'){DC.vx*=0.85;DC.vy*=0.85;}
  else if(DC.flightMode==='rtl'){
    const cx=DC.fieldX+DC.fieldW/2,cy=DC.fieldY+DC.fieldH-20;
    const dx=cx-DC.x,dy=cy-DC.y,d=Math.sqrt(dx*dx+dy*dy);
    if(d<5){DC.vx=0;DC.vy=0;DC.flightMode='hover';toast('🏠 Drone returned home!');}
    else{DC.vx+=(dx/d)*0.6;DC.vy+=(dy/d)*0.6;}
  } else if(DC.flightMode==='manual'&&DC.isFlying){
    DC.vx+=DC.jRX*3.5;DC.vy+=DC.jRY*3.5;DC.heading+=DC.jLX*3;
  }
  DC.vx*=0.88;DC.vy*=0.88;
  const spd=Math.sqrt(DC.vx*DC.vx+DC.vy*DC.vy);
  const maxSpd=DC.flightMode==='auto'?4:6;
  if(spd>maxSpd){DC.vx=DC.vx/spd*maxSpd;DC.vy=DC.vy/spd*maxSpd;}
  DC.speed=Math.round(spd*0.5*10)/10;
  if(DC.isFlying){
    DC.x+=DC.vx;DC.y+=DC.vy;
    DC.x=Math.max(DC.fieldX+8,Math.min(DC.fieldX+DC.fieldW-8,DC.x));
    DC.y=Math.max(DC.fieldY+8,Math.min(DC.fieldY+DC.fieldH-8,DC.y));
    DC.trailPoints.push({x:DC.x,y:DC.y});
    if(DC.trailPoints.length>120)DC.trailPoints.shift();
  }
  if(DC.sprayOn&&DC.isFlying){
    const numP=DC.sprayPattern==='spot'?2:DC.sprayPattern==='strip'?4:7;
    const width=DC.sprayPattern==='spot'?10:DC.sprayPattern==='strip'?20:40;
    for(let i=0;i<numP;i++){
      DC.sprayParticles.push({x:DC.x+(Math.random()-0.5)*width,y:DC.y+8,vx:(Math.random()-0.5)*0.8,vy:Math.random()*1.8+0.8,r:Math.random()*2.5+1,life:100,maxLife:100});
    }
    if(Math.random()<0.1)DC.sprayedZones.push({x:DC.x,y:DC.y,r:DC.sprayPattern==='spot'?8:DC.sprayPattern==='strip'?14:22});
    DC.tank=Math.max(0,DC.tank-0.002*DC.sprayRate);
    DC.coverage=Math.min(100,DC.coverage+0.012);
  }
  DC.sprayParticles=DC.sprayParticles.filter(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=0.05;p.life-=3;p.r*=0.98;return p.life>0;});
  if(DC.isFlying)for(let i=0;i<2;i++)DC.exhaustParticles.push({x:DC.x+(Math.random()-0.5)*30,y:DC.y+6,vx:(Math.random()-0.5)*0.5,vy:Math.random()*0.6+0.2,r:Math.random()*3+1.5,life:60});
  DC.exhaustParticles=DC.exhaustParticles.filter(p=>{p.x+=p.vx;p.y+=p.vy;p.life-=4;return p.life>0;});
  if(DC.isFlying)DC.bat=Math.max(0,DC.bat-0.001);
  updateHUD();
}

function autoFly(){
  if(DC.autoPathIdx>=DC.autoPath.length){DC.autoPathIdx=0;return;}
  const wp=DC.autoPath[DC.autoPathIdx];
  const dx=wp.x-DC.x,dy=wp.y-DC.y,d=Math.sqrt(dx*dx+dy*dy);
  if(d<8){DC.autoPathIdx++;return;}
  DC.vx+=(dx/d)*3;DC.vy+=(dy/d)*3;
  DC.heading=Math.atan2(dy,dx)*180/Math.PI+90;
}

function renderDrone(){
  const ctx=DC.ctx,W=DC.W,H=DC.H;
  ctx.clearRect(0,0,W,H);
  const bg=ctx.createLinearGradient(0,0,0,H);
  bg.addColorStop(0,'#030d03');bg.addColorStop(1,'#050f10');
  ctx.fillStyle=bg;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(46,204,113,.04)';ctx.lineWidth=1;
  for(let x=0;x<W;x+=28){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
  for(let y=0;y<H;y+=28){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
  ctx.save();ctx.strokeStyle='rgba(46,204,113,.5)';ctx.lineWidth=1.5;ctx.setLineDash([6,4]);
  ctx.strokeRect(DC.fieldX,DC.fieldY,DC.fieldW,DC.fieldH);ctx.setLineDash([]);ctx.restore();
  DC.sprayedZones.forEach(z=>{
    const g=ctx.createRadialGradient(z.x,z.y,0,z.x,z.y,z.r*2);
    g.addColorStop(0,'rgba(14,165,233,.18)');g.addColorStop(1,'rgba(14,165,233,0)');
    ctx.fillStyle=g;ctx.beginPath();ctx.arc(z.x,z.y,z.r*2,0,Math.PI*2);ctx.fill();
  });
  if(DC.flightMode==='auto'&&DC.autoPath.length>0){
    ctx.save();ctx.strokeStyle='rgba(46,204,113,.18)';ctx.lineWidth=1;ctx.setLineDash([4,6]);
    ctx.beginPath();DC.autoPath.forEach((p,i)=>{i===0?ctx.moveTo(p.x,p.y):ctx.lineTo(p.x,p.y);});
    ctx.stroke();ctx.setLineDash([]);ctx.restore();
    if(DC.autoPathIdx<DC.autoPath.length){
      const wp=DC.autoPath[DC.autoPathIdx];
      ctx.save();ctx.strokeStyle='rgba(46,204,113,.6)';ctx.lineWidth=1;
      ctx.beginPath();ctx.arc(wp.x,wp.y,6,0,Math.PI*2);ctx.stroke();ctx.restore();
    }
  }
  if(DC.trailPoints.length>1){
    ctx.save();
    for(let i=1;i<DC.trailPoints.length;i++){
      ctx.strokeStyle=`rgba(46,204,113,${i/DC.trailPoints.length*0.6})`;ctx.lineWidth=1.2;
      ctx.beginPath();ctx.moveTo(DC.trailPoints[i-1].x,DC.trailPoints[i-1].y);ctx.lineTo(DC.trailPoints[i].x,DC.trailPoints[i].y);ctx.stroke();
    }
    ctx.restore();
  }
  DC.exhaustParticles.forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(180,200,180,${p.life/60*0.12})`;ctx.fill();});
  DC.sprayParticles.forEach(p=>{
    const alpha=p.life/p.maxLife;
    const g=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r);
    g.addColorStop(0,`rgba(56,189,248,${alpha*0.9})`);g.addColorStop(1,'rgba(14,165,233,0)');
    ctx.fillStyle=g;ctx.beginPath();ctx.arc(p.x,p.y,p.r*2,0,Math.PI*2);ctx.fill();
    ctx.fillStyle=`rgba(186,230,253,${alpha})`;ctx.beginPath();ctx.arc(p.x,p.y,p.r*0.5,0,Math.PI*2);ctx.fill();
  });
  if(DC.sprayOn&&DC.isFlying){
    const fanW=DC.sprayPattern==='spot'?12:DC.sprayPattern==='strip'?28:50;
    const fanH=32;
    const g=ctx.createLinearGradient(DC.x,DC.y,DC.x,DC.y+fanH);
    g.addColorStop(0,'rgba(14,165,233,.35)');g.addColorStop(1,'rgba(14,165,233,0)');
    ctx.fillStyle=g;ctx.beginPath();ctx.moveTo(DC.x,DC.y+8);ctx.lineTo(DC.x-fanW,DC.y+fanH);ctx.lineTo(DC.x+fanW,DC.y+fanH);ctx.closePath();ctx.fill();
    for(let i=-fanW;i<=fanW;i+=8){
      const ox=DC.x+i+(Math.sin(Date.now()*0.003+i)*2);
      const oy=DC.y+fanH+Math.sin(Date.now()*0.005+i*0.3)*4;
      ctx.fillStyle='rgba(186,230,253,.5)';ctx.beginPath();ctx.arc(ox,oy,1.5,0,Math.PI*2);ctx.fill();
    }
  }
  if(DC.isFlying){
    const sh=ctx.createRadialGradient(DC.x,DC.y+30,0,DC.x,DC.y+30,25);
    sh.addColorStop(0,'rgba(0,0,0,.4)');sh.addColorStop(1,'rgba(0,0,0,0)');
    ctx.fillStyle=sh;ctx.beginPath();ctx.ellipse(DC.x,DC.y+30,25,8,0,0,Math.PI*2);ctx.fill();
  }
  ctx.save();ctx.translate(DC.x,DC.y);ctx.rotate(DC.heading*Math.PI/180);
  ctx.shadowColor='rgba(46,204,113,.6)';ctx.shadowBlur=DC.isFlying?14:4;
  ctx.strokeStyle=DC.isFlying?'#2ecc71':'#3a5a3a';ctx.lineWidth=2.5;
  [[-18,-18],[18,-18],[-18,18],[18,18]].forEach(([ax,ay])=>{ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(ax,ay);ctx.stroke();});
  ctx.shadowBlur=0;
  const bodyG=ctx.createRadialGradient(0,-2,0,0,0,10);
  bodyG.addColorStop(0,DC.isFlying?'#3ddc84':'#2d5a3a');bodyG.addColorStop(1,DC.isFlying?'#1a7a3e':'#1a3a20');
  ctx.fillStyle=bodyG;ctx.beginPath();ctx.roundRect(-9,-6,18,12,4);ctx.fill();
  if(DC.sprayOn){
    ctx.fillStyle='rgba(14,165,233,.8)';ctx.beginPath();ctx.roundRect(-3,5,6,5,2);ctx.fill();
    ctx.fillStyle='rgba(56,189,248,1)';ctx.beginPath();ctx.arc(0,10,2.5,0,Math.PI*2);
    ctx.shadowColor='rgba(14,165,233,.8)';ctx.shadowBlur=8;ctx.fill();ctx.shadowBlur=0;
  }
  [[-18,-18],[18,-18],[-18,18],[18,18]].forEach(([rx,ry])=>{
    ctx.save();ctx.translate(rx,ry);ctx.rotate(DC.rotorAngle*(rx<0?1:-1));
    ctx.fillStyle=`rgba(46,204,113,${DC.isFlying?0.65:0.25})`;
    ctx.shadowColor='rgba(46,204,113,.5)';ctx.shadowBlur=DC.isFlying?8:0;
    ctx.beginPath();ctx.ellipse(0,0,9,2.5,0,0,Math.PI*2);ctx.fill();
    ctx.rotate(Math.PI/2);ctx.beginPath();ctx.ellipse(0,0,9,2.5,0,0,Math.PI*2);ctx.fill();
    ctx.shadowBlur=0;ctx.fillStyle=DC.isFlying?'#2ecc71':'#3a5a3a';
    ctx.beginPath();ctx.arc(0,0,2.5,0,Math.PI*2);ctx.fill();ctx.restore();
  });
  ctx.fillStyle=DC.isFlying?'#ff3333':'#660000';ctx.beginPath();ctx.arc(-9,-6,2,0,Math.PI*2);ctx.fill();
  ctx.fillStyle=DC.isFlying?'#33ff99':'#006633';ctx.beginPath();ctx.arc(9,-6,2,0,Math.PI*2);ctx.fill();
  ctx.restore();
  ctx.fillStyle='rgba(46,204,113,.5)';ctx.font='600 9px JetBrains Mono,monospace';ctx.textAlign='center';
  ctx.fillText(`${DC.x.toFixed(0)},${DC.y.toFixed(0)}`,DC.x,DC.y-22);
  if(!DC.isFlying){
    ctx.fillStyle='rgba(0,0,0,.5)';ctx.fillRect(DC.fieldX,DC.fieldY+DC.fieldH/2-18,DC.fieldW,36);
    ctx.fillStyle='rgba(46,204,113,.8)';ctx.font='bold 14px Sora,sans-serif';ctx.textAlign='center';
    ctx.fillText('🛬 GROUNDED — Press TAKEOFF to fly',W/2,DC.fieldY+DC.fieldH/2+5);
  }
  if(DC.isFlying){
    const patterns={full:'🌊 FULL WIDTH',strip:'〰️ STRIP MODE',spot:'🎯 SPOT SPRAY'};
    ctx.fillStyle=DC.sprayOn?'rgba(14,165,233,.7)':'rgba(255,255,255,.2)';
    ctx.font='600 9px Sora,sans-serif';ctx.textAlign='right';
    ctx.fillText((DC.sprayOn?'💧 ':'')+patterns[DC.sprayPattern],DC.fieldX+DC.fieldW-8,DC.fieldY+14);
  }
  const modeBG={idle:'rgba(100,100,100,.6)',manual:'rgba(46,204,113,.5)',hover:'rgba(14,165,233,.5)',auto:'rgba(124,58,237,.6)',rtl:'rgba(245,158,11,.6)'};
  ctx.fillStyle=modeBG[DC.flightMode]||'rgba(100,100,100,.6)';
  const modeLabel={idle:'IDLE',manual:'MANUAL',hover:'HOVER',auto:'AUTO-MISSION',rtl:'RETURN HOME'};
  const ml=modeLabel[DC.flightMode]||DC.flightMode.toUpperCase();
  const tw=ctx.measureText(ml).width;
  ctx.beginPath();ctx.roundRect(DC.fieldX+6,DC.fieldY+6,tw+18,18,99);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='700 10px Sora,sans-serif';ctx.textAlign='left';
  ctx.fillText(ml,DC.fieldX+15,DC.fieldY+18);
  // Coverage counter
  if(DC.isFlying){
    ctx.fillStyle='rgba(0,0,0,.5)';ctx.beginPath();ctx.roundRect(DC.fieldX+DC.fieldW-70,DC.fieldY+DC.fieldH-20,64,16,99);ctx.fill();
    ctx.fillStyle='#2ecc71';ctx.font='700 9px JetBrains Mono,monospace';ctx.textAlign='center';
    ctx.fillText('COV: '+Math.round(DC.coverage)+'%',DC.fieldX+DC.fieldW-38,DC.fieldY+DC.fieldH-9);
  }
}

function updateHUD(){
  const set=(id,v)=>{const el=document.getElementById(id);if(el)el.textContent=v;};
  set('hudBat',Math.round(DC.bat)+'%');set('hudAlt',DC.alt+'m');set('hudSpd',DC.speed.toFixed(1));
  set('tankPct',Math.round(DC.tank)+'%');set('altDisplay',DC.alt+' m');
  const tb=document.getElementById('tankBar');if(tb)tb.style.width=DC.tank+'%';
  const lat=(30.1865+DC.x*0.00001).toFixed(4);const lng=(71.4911+DC.y*0.00001).toFixed(4);
  set('tGPS',lat+'N');set('tLng',lng+'E');set('tCov',Math.round(DC.coverage)+'%');
  const rem=Math.max(0,Math.round((DC.bat/100)*38));set('tTime',rem+'min');
  set('dashBat',Math.round(DC.bat)+'%');set('dashTank',Math.round(DC.tank)+'%');
  // Coverage on dashboard
  const u=getUser();const ha=parseFloat(u?.acres||12);
  const coveredAcres=(DC.coverage/100*ha).toFixed(1);
  const pct=Math.round(DC.coverage);
  const dbar=document.getElementById('dbar');const dpct=document.getElementById('dpct');
  if(dbar)dbar.style.width=Math.min(pct,100)+'%';if(dpct)dpct.textContent=pct+'%';
  set('coveredAcresText',coveredAcres+'/'+ha+' acres');
  set('mapSprayPct',pct+'%');
  // Field coverages
  const fa=document.getElementById('fieldACov');const fb=document.getElementById('fieldBCov');
  const fab=document.getElementById('fieldABar');const fbb=document.getElementById('fieldBBar');
  if(fa)fa.textContent=Math.min(pct,100)+'%';if(fb)fb.textContent=Math.max(0,pct-30)+'%';
  if(fab)fab.style.width=Math.min(pct,100)+'%';if(fbb)fbb.style.width=Math.max(0,pct-30)+'%';
  // Badge
  const badge=document.getElementById('coverageBadge');const badgeTxt=document.getElementById('coverageBadgeTxt');
  if(badge&&badgeTxt){
    if(DC.sprayOn){badge.style.background='var(--skyl)';badge.style.color='#0369a1';badgeTxt.textContent='SPRAYING';}
    else if(DC.isFlying){badge.style.background='var(--gpal)';badge.style.color='var(--gp)';badgeTxt.textContent='FLYING';}
    else{badge.style.background='var(--redl)';badge.style.color='var(--red)';badgeTxt.textContent='IDLE';}
  }
  const statusTxt=document.getElementById('hudStatusTxt');
  if(statusTxt){
    const s=!DC.isFlying?'GROUNDED — Takeoff Ready':DC.sprayOn?'SPRAYING — '+DC.sprayPattern.toUpperCase():DC.flightMode==='auto'?'AUTO MISSION':DC.flightMode.toUpperCase();
    statusTxt.textContent=s;
  }
  const chip=document.getElementById('droneStatusChip');
  if(chip)chip.textContent=DC.isFlying?(DC.sprayOn?'🚁 Spraying':'🚁 Flying'):'🚁 Drone Grounded';
}

// ============================================================
// JOYSTICK SETUP
// ============================================================
function setupJoysticks(){
  setupOneJoystick('joy-left','jkL','left');
  setupOneJoystick('joy-right','jkR','right');
}
function setupOneJoystick(joyId,knobId,side){
  const joy=document.getElementById(joyId),knob=document.getElementById(knobId);
  if(!joy||!knob)return;
  const maxR=42;let active=false,cX=0,cY=0;
  function getCenter(){const r=joy.getBoundingClientRect();return{x:r.left+r.width/2,y:r.top+r.height/2};}
  function setKnob(dx,dy){
    const dist=Math.sqrt(dx*dx+dy*dy);
    if(dist>maxR){dx=dx/dist*maxR;dy=dy/dist*maxR;}
    knob.style.transform=`translate(calc(-50% + ${dx}px), calc(-50% + ${dy}px))`;
    const nx=dx/maxR,ny=dy/maxR;
    if(side==='left'){DC.jLX=nx;DC.jLY=ny;}else{DC.jRX=nx;DC.jRY=ny;}
    if((Math.abs(nx)>0.05||Math.abs(ny)>0.05)&&DC.isFlying&&DC.flightMode!=='manual')setFlightMode('manual');
  }
  function resetKnob(){knob.style.transition='transform .18s ease';knob.style.transform='translate(-50%, -50%)';setTimeout(()=>knob.style.transition='',200);if(side==='left'){DC.jLX=0;DC.jLY=0;}else{DC.jRX=0;DC.jRY=0;}}
  function onStart(e){e.preventDefault();active=true;const c=getCenter();cX=c.x;cY=c.y;joy.style.borderColor='rgba(46,204,113,.6)';if(!DC.isFlying)toast('⚠️ Takeoff first! Press 🛫 Takeoff');}
  function onMove(e){if(!active)return;e.preventDefault();const pt=e.touches?e.touches[0]:e;setKnob(pt.clientX-cX,pt.clientY-cY);}
  function onEnd(){active=false;resetKnob();joy.style.borderColor='rgba(46,204,113,.25)';}
  joy.addEventListener('mousedown',onStart);joy.addEventListener('touchstart',onStart,{passive:false});
  document.addEventListener('mousemove',onMove);document.addEventListener('touchmove',onMove,{passive:false});
  document.addEventListener('mouseup',onEnd);document.addEventListener('touchend',onEnd);
}

// ============================================================
// DRONE FLIGHT CONTROLS
// ============================================================
function takeOffLand(){
  const btn=document.getElementById('btnTOL');
  if(DC.isLanded){
    if(!APP_STATE.selectedDrone){toast('⚠️ Select a drone first!');openDroneSelector();return;}
    DC.isFlying=true;DC.isLanded=false;DC.flightMode='hover';DC.trailPoints=[];
    DC.missionStart=Date.now();
    if(btn){btn.textContent='🛬 Land';btn.style.background='rgba(239,68,68,.2)';btn.style.borderColor='rgba(239,68,68,.5)';btn.style.color='#f87171';}
    toast('🛫 '+APP_STATE.selectedDrone.name+' taking off!');
    setFlightMode('hover');
    let lf=0;function liftAnim(){lf++;DC.y-=1;if(lf<30)requestAnimationFrame(liftAnim);}liftAnim();
    if(!APP_STATE.activities)APP_STATE.activities=[];
    APP_STATE.activities.unshift({type:'🚁',desc:APP_STATE.selectedDrone.name+' — Takeoff',field:'All Fields',label:new Date().toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'}),ts:Date.now()});
    saveState();renderActivities();
  } else {
    DC.isFlying=false;DC.isLanded=true;DC.flightMode='idle';DC.sprayOn=false;DC.vx=0;DC.vy=0;
    if(btn){btn.textContent='🛫 Takeoff';btn.style.background='rgba(46,204,113,.15)';btn.style.borderColor='rgba(46,204,113,.4)';btn.style.color='#2ecc71';}
    updateSprayUI();
    const flightMin=DC.missionStart?Math.round((Date.now()-DC.missionStart)/60000):0;
    const coveredAcres=((DC.coverage/100)*(parseFloat(getUser()?.acres)||12)).toFixed(1);
    toast('🛬 Landed safely. '+coveredAcres+' acres covered!');
    if(!APP_STATE.activities)APP_STATE.activities=[];
    APP_STATE.activities.unshift({type:'🛬',desc:'Landed — '+coveredAcres+' acres covered in '+flightMin+' min',field:'All Fields',label:new Date().toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'}),ts:Date.now()});
    saveState();renderActivities();
    document.getElementById('missionAlert').textContent='✅ Mission done — '+coveredAcres+' acres sprayed ('+Math.round(DC.coverage)+'%)';
    document.getElementById('missionAlert').className='alert alert-ok';
  }
}
function setFlightMode(mode){
  if(!DC.isFlying&&mode==='auto'){toast('⚠️ Takeoff first!');return;}
  DC.flightMode=mode;
  const chip=document.getElementById('modeChip');
  const labels={idle:'Idle',manual:'Manual Mode',hover:'Hover Mode',auto:'Auto Mission',rtl:'Return Home'};
  if(chip)chip.textContent=labels[mode]||mode;
  if(mode==='auto'){generateAutoPath();DC.autoPathIdx=0;DC.sprayOn=true;updateSprayUI();toast('🤖 Auto spray mission started!');}
  if(mode==='hover'&&DC.isFlying)toast('⏸️ Drone hovering');
  if(mode==='rtl')toast('🏠 Returning to home...');
}
function changeAlt(d){DC.alt=Math.max(5,Math.min(120,DC.alt+d*5));toast('📏 Altitude: '+DC.alt+'m');}
function emergStop(){
  DC.isFlying=false;DC.isLanded=true;DC.flightMode='idle';DC.sprayOn=false;
  DC.vx=0;DC.vy=0;DC.jLX=0;DC.jLY=0;DC.jRX=0;DC.jRY=0;
  const btn=document.getElementById('btnTOL');
  if(btn){btn.textContent='🛫 Takeoff';btn.style.background='rgba(46,204,113,.15)';btn.style.borderColor='rgba(46,204,113,.4)';btn.style.color='#2ecc71';}
  updateSprayUI();
  toast('🛑 EMERGENCY STOP — All systems halted!');
  if(!APP_STATE.activities)APP_STATE.activities=[];
  APP_STATE.activities.unshift({type:'🛑',desc:'Emergency Stop triggered',field:'All Fields',label:new Date().toLocaleString('en-PK',{dateStyle:'medium',timeStyle:'short'}),ts:Date.now()});
  saveState();renderActivities();
}

// ============================================================
// SPRAY CONTROLS
// ============================================================
function toggleSpray(){
  if(!DC.isFlying){toast('⚠️ Drone must be flying to spray!');return;}
  DC.sprayOn=!DC.sprayOn;updateSprayUI();
  toast(DC.sprayOn?'💧 Spraying started!':'🚫 Spray stopped');
}
function setSprayPattern(p){
  DC.sprayPattern=p;
  ['spFull','spStrip','spSpot'].forEach(id=>{
    const el=document.getElementById(id);
    if(el){el.style.background='rgba(14,165,233,.08)';el.style.borderColor='rgba(14,165,233,.25)';}
  });
  const map={full:'spFull',strip:'spStrip',spot:'spSpot'};
  const active=document.getElementById(map[p]);
  if(active){active.style.background='rgba(14,165,233,.3)';active.style.borderColor='#0ea5e9';}
  toast({full:'🌊 Full width spray',strip:'〰️ Strip spray mode',spot:'🎯 Spot spray mode'}[p]);
}
function updateSprayRate(v){DC.sprayRate=parseInt(v);const el=document.getElementById('sprayRateVal');if(el)el.textContent=v+' L/ha';}
function updateSprayUI(){
  const btn=document.getElementById('sprayToggleBtn'),txt=document.getElementById('sprayBtnTxt');
  if(btn){
    if(DC.sprayOn){btn.style.background='rgba(14,165,233,.3)';btn.style.borderColor='#0ea5e9';btn.style.boxShadow='0 0 14px rgba(14,165,233,.35)';}
    else{btn.style.background='rgba(14,165,233,.08)';btn.style.borderColor='rgba(14,165,233,.25)';btn.style.boxShadow='none';}
  }
  if(txt)txt.textContent=DC.sprayOn?'💧 Spray ON':'Spray OFF';
}

// Initialize
loadWeather();
renderPrices();
</script>
</body>
</html>""")

# 2. Create a side-by-side layout
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Input")
    # Text area for the user to paste their code
    html_input = st.text_area(
        "Paste your code here:",
        height=500,
        placeholder="""<h1 style="color: blue;">Hello World!</h1>\n<p>This is a custom HTML preview.</p>"""
    )

with col2:
    st.header("🖥️ Preview")
    # 3. Render the HTML if the user has entered anything
    if html_input:
        # We wrap the output in a container to match the height of the text area
        with st.container():
            components.html(html_input, height=500, scrolling=True)
    else:
        st.info("Awaiting code... Paste some HTML on the left to see it live here.")
