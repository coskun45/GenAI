var _JUPYTERLAB;(()=>{"use strict";var e,r,t,n,a,o,i,f,l,u,s,d,c,p,h,v,b,g,m,y,w,j,P,S={7045:(e,r,t)=>{var n={"./index":()=>Promise.all([t.e(87),t.e(687),t.e(274),t.e(976),t.e(509)]).then((()=>()=>t(8509))),"./extension":()=>Promise.all([t.e(87),t.e(687),t.e(274),t.e(976)]).then((()=>()=>t(4122)))},a=(e,r)=>(t.R=r,r=t.o(n,e)?n[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var n="default",a=t.S[n];if(a&&a!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[n]=e,t.I(n,r)}};t.d(r,{get:()=>a,init:()=>o})}},E={};function k(e){var r=E[e];if(void 0!==r)return r.exports;var t=E[e]={id:e,exports:{}};return S[e].call(t.exports,t,t.exports,k),t.exports}k.m=S,k.c=E,k.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return k.d(r,{a:r}),r},k.d=(e,r)=>{for(var t in r)k.o(r,t)&&!k.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},k.f={},k.e=e=>Promise.all(Object.keys(k.f).reduce(((r,t)=>(k.f[t](e,r),r)),[])),k.u=e=>e+"."+{87:"217810693c458384fc44",144:"309a8b41e6b459907eac",165:"3364319a56043af5093a",274:"2951175d6d9e8013fc6f",372:"a5fa17133e025d17edc4",481:"bf62897987c628ce913f",509:"2e7e0fce1e73911c3dad",687:"5264c3ea1d1c4f6bbd06",743:"f51284935b839eb42a38",772:"05c8cd35ef5fc3855b04",853:"2aa0697cc36938a7c7df",893:"1b5079b3c2ec2aeb3cdc",976:"a672a82a17dcbbd19d26"}[e]+".js?v="+{87:"217810693c458384fc44",144:"309a8b41e6b459907eac",165:"3364319a56043af5093a",274:"2951175d6d9e8013fc6f",372:"a5fa17133e025d17edc4",481:"bf62897987c628ce913f",509:"2e7e0fce1e73911c3dad",687:"5264c3ea1d1c4f6bbd06",743:"f51284935b839eb42a38",772:"05c8cd35ef5fc3855b04",853:"2aa0697cc36938a7c7df",893:"1b5079b3c2ec2aeb3cdc",976:"a672a82a17dcbbd19d26"}[e],k.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),k.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="yfiles-jupyter-graphs:",k.l=(t,n,a,o)=>{if(e[t])e[t].push(n);else{var i,f;if(void 0!==a)for(var l=document.getElementsByTagName("script"),u=0;u<l.length;u++){var s=l[u];if(s.getAttribute("src")==t||s.getAttribute("data-webpack")==r+a){i=s;break}}i||(f=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,k.nc&&i.setAttribute("nonce",k.nc),i.setAttribute("data-webpack",r+a),i.src=t),e[t]=[n];var d=(r,n)=>{i.onerror=i.onload=null,clearTimeout(c);var a=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),a&&a.forEach((e=>e(n))),r)return r(n)},c=setTimeout(d.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=d.bind(null,i.onerror),i.onload=d.bind(null,i.onload),f&&document.head.appendChild(i)}},k.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{k.S={};var e={},r={};k.I=(t,n)=>{n||(n=[]);var a=r[t];if(a||(a=r[t]={}),!(n.indexOf(a)>=0)){if(n.push(a),e[t])return e[t];k.o(k.S,t)||(k.S[t]={});var o=k.S[t],i="yfiles-jupyter-graphs",f=(e,r,t,n)=>{var a=o[e]=o[e]||{},f=a[r];(!f||!f.loaded&&(!n!=!f.eager?n:i>f.from))&&(a[r]={get:t,from:i,eager:!!n})},l=[];if("default"===t)f("@ctrl/tinycolor","3.6.1",(()=>k.e(372).then((()=>()=>k(4372))))),f("@mdi/js","6.9.96",(()=>k.e(165).then((()=>()=>k(9165))))),f("leaflet","1.9.4",(()=>k.e(481).then((()=>()=>k(3481))))),f("vue-json-viewer","2.2.22",(()=>Promise.all([k.e(743),k.e(144)]).then((()=>()=>k(6743))))),f("vue","2.7.16",(()=>k.e(893).then((()=>()=>k(2893))))),f("yfiles-jupyter-graphs","1.8.1",(()=>Promise.all([k.e(87),k.e(687),k.e(274),k.e(976),k.e(509)]).then((()=>()=>k(8509))))),f("yfiles","26.0.4-jupyter-widget+eval",(()=>Promise.all([k.e(87),k.e(687),k.e(853)]).then((()=>()=>k(3853)))));return l.length?e[t]=Promise.all(l).then((()=>e[t]=1)):e[t]=1}}})(),(()=>{var e;k.g.importScripts&&(e=k.g.location+"");var r=k.g.document;if(!e&&r&&(r.currentScript&&"SCRIPT"===r.currentScript.tagName.toUpperCase()&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var n=t.length-1;n>-1&&(!e||!/^http(s?):/.test(e));)e=t[n--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),k.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),n=t[1]?r(t[1]):[];return t[2]&&(n.length++,n.push.apply(n,r(t[2]))),t[3]&&(n.push([]),n.push.apply(n,r(t[3]))),n},n=(e,r)=>{e=t(e),r=t(r);for(var n=0;;){if(n>=e.length)return n<r.length&&"u"!=(typeof r[n])[0];var a=e[n],o=(typeof a)[0];if(n>=r.length)return"u"==o;var i=r[n],f=(typeof i)[0];if(o!=f)return"o"==o&&"n"==f||"s"==f||"u"==o;if("o"!=o&&"u"!=o&&a!=i)return a<i;n++}},a=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var n=1,o=1;o<e.length;o++)n--,t+="u"==(typeof(f=e[o]))[0]?"-":(n>0?".":"")+(n=2,f);return t}var i=[];for(o=1;o<e.length;o++){var f=e[o];i.push(0===f?"not("+l()+")":1===f?"("+l()+" || "+l()+")":2===f?i.pop()+" "+i.pop():a(f))}return l();function l(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var n=e[0],a=n<0;a&&(n=-n-1);for(var i=0,f=1,l=!0;;f++,i++){var u,s,d=f<e.length?(typeof e[f])[0]:"";if(i>=r.length||"o"==(s=(typeof(u=r[i]))[0]))return!l||("u"==d?f>n&&!a:""==d!=a);if("u"==s){if(!l||"u"!=d)return!1}else if(l)if(d==s)if(f<=n){if(u!=e[f])return!1}else{if(a?u>e[f]:u<e[f])return!1;u!=e[f]&&(l=!1)}else if("s"!=d&&"n"!=d){if(a||f<=n)return!1;l=!1,f--}else{if(f<=n||s<d!=a)return!1;l=!1}else"s"!=d&&"n"!=d&&(l=!1,f--)}}var c=[],p=c.pop.bind(c);for(i=1;i<e.length;i++){var h=e[i];c.push(1==h?p()|p():2==h?p()&p():h?o(h,r):!p())}return!!p()},i=(e,r)=>e&&k.o(e,r),f=e=>(e.loaded=1,e.get()),l=e=>Object.keys(e).reduce(((r,t)=>(e[t].eager&&(r[t]=e[t]),r)),{}),u=(e,r,t,a)=>{var i=a?l(e[r]):e[r];return(r=Object.keys(i).reduce(((e,r)=>!o(t,r)||e&&!n(e,r)?e:r),0))&&i[r]},s=(e,r,t)=>{var a=t?l(e[r]):e[r];return Object.keys(a).reduce(((e,r)=>!e||!a[e].loaded&&n(e,r)?r:e),0)},d=(e,r,t,n)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+a(n)+")",c=(e,r,t,n,o)=>{var i=e[t];return"No satisfying version ("+a(n)+")"+(o?" for eager consumption":"")+" of shared module "+t+" found in shared scope "+r+".\nAvailable versions: "+Object.keys(i).map((e=>e+" from "+i[e].from)).join(", ")},p=e=>{throw new Error(e)},h=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},b=(e,r,t)=>t?t():((e,r)=>p("Shared module "+r+" doesn't exist in shared scope "+e))(e,r),g=(v=e=>function(r,t,n,a,o){var i=k.I(r);return i&&i.then&&!n?i.then(e.bind(e,r,k.S[r],t,!1,a,o)):e(r,k.S[r],t,n,a,o)})(((e,r,t,n,a,o)=>{if(!i(r,t))return b(e,t,o);var l=u(r,t,a,n);return l?f(l):o?o():void p(c(r,e,t,a,n))})),m=v(((e,r,t,n,a,l)=>{if(!i(r,t))return b(e,t,l);var u=s(r,t,n);return o(a,u)||h(d(r,t,u,a)),f(r[t][u])})),y={},w={1103:()=>g("default","yfiles",!1,[0],(()=>k.e(853).then((()=>()=>k(3853))))),1224:()=>g("default","leaflet",!1,[1,1,9,4],(()=>k.e(481).then((()=>()=>k(3481))))),3289:()=>g("default","vue-json-viewer",!1,[1,2,2,19],(()=>Promise.all([k.e(743),k.e(144)]).then((()=>()=>k(6743))))),3983:()=>m("default","@jupyter-widgets/base",!1,[,[1,6],[1,5],[1,4],[1,3],[1,2],[1,1,1,10],1,1,1,1,1]),4339:()=>g("default","@ctrl/tinycolor",!1,[1,3,4,1],(()=>k.e(372).then((()=>()=>k(4372))))),5712:()=>g("default","vue",!1,[1,2,6,14],(()=>k.e(893).then((()=>()=>k(2893))))),9384:()=>g("default","@mdi/js",!1,[1,6,5,95],(()=>k.e(165).then((()=>()=>k(9165))))),3144:()=>g("default","vue",!1,[1,2,6,9],(()=>k.e(893).then((()=>()=>k(2893)))))},j={144:[3144],976:[1103,1224,3289,3983,4339,5712,9384]},P={},k.f.consumes=(e,r)=>{k.o(j,e)&&j[e].forEach((e=>{if(k.o(y,e))return r.push(y[e]);if(!P[e]){var t=r=>{y[e]=0,k.m[e]=t=>{delete k.c[e],t.exports=r()}};P[e]=!0;var n=r=>{delete y[e],k.m[e]=t=>{throw delete k.c[e],r}};try{var a=w[e]();a.then?r.push(y[e]=a.then(t).catch(n)):t(a)}catch(e){n(e)}}}))},(()=>{k.b=document.baseURI||self.location.href;var e={277:0};k.f.j=(r,t)=>{var n=k.o(e,r)?e[r]:void 0;if(0!==n)if(n)t.push(n[2]);else if(144!=r){var a=new Promise(((t,a)=>n=e[r]=[t,a]));t.push(n[2]=a);var o=k.p+k.u(r),i=new Error;k.l(o,(t=>{if(k.o(e,r)&&(0!==(n=e[r])&&(e[r]=void 0),n)){var a=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+a+": "+o+")",i.name="ChunkLoadError",i.type=a,i.request=o,n[1](i)}}),"chunk-"+r,r)}else e[r]=0};var r=(r,t)=>{var n,a,[o,i,f]=t,l=0;if(o.some((r=>0!==e[r]))){for(n in i)k.o(i,n)&&(k.m[n]=i[n]);if(f)f(k)}for(r&&r(t);l<o.length;l++)a=o[l],k.o(e,a)&&e[a]&&e[a][0](),e[a]=0},t=self.webpackChunkyfiles_jupyter_graphs=self.webpackChunkyfiles_jupyter_graphs||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),k.nc=void 0;var T=k(7045);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["yfiles-jupyter-graphs"]=T})();