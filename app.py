import streamlit as st
import unicodedata

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="La Geopolítica de China",
    page_icon="🌏",
    layout="wide"
)

st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #8B0000, #C62828, #E53935);
        color: white;
        padding: 26px;
        border-radius: 20px;
        margin: 10px 0 18px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    }
    .hero h1 { margin: 0; font-size: 34px; }
    .hero p { margin-top: 10px; font-size: 16px; }
    .subhero {
        background: linear-gradient(135deg, #0D47A1, #1976D2);
        color: white;
        padding: 18px;
        border-radius: 16px;
        margin: 10px 0 18px 0;
        box-shadow: 0 6px 14px rgba(0,0,0,0.18);
    }
    .card {
        background: #ffffff;
        border-left: 8px solid #1565C0;
        padding: 16px;
        margin: 12px 0;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
    }
    .card-red {
        background: #fff5f5;
        border-left: 8px solid #C62828;
        padding: 16px;
        margin: 12px 0;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
    }
    .card-green {
        background: #f1fff5;
        border-left: 8px solid #2E7D32;
        padding: 16px;
        margin: 12px 0;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
    }
    .card-gold {
        background: #fff9e6;
        border-left: 8px solid #F9A825;
        padding: 16px;
        margin: 12px 0;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
    }
    .score-box {
        background: linear-gradient(135deg, #1B5E20, #43A047);
        color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.2);
        margin-top: 12px;
    }
    .footer-box {
        background: #f3f8ff;
        border-left: 8px solid #1976D2;
        padding: 15px;
        border-radius: 14px;
        margin-top: 18px;
    }
    .tag {
        display: inline-block;
        background: #1565C0;
        color: white;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 12px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATOS
# ============================================================

CONCEPTOS_AVANZADOS = {
    "Trampa de Tucídides": "Idea de que una potencia emergente puede entrar en conflicto con una potencia dominante cuando cambia el equilibrio de poder.",
    "Multipolaridad": "Mundo donde existen varias potencias importantes y no solo una con dominio absoluto.",
    "Decoupling": "Separación económica y tecnológica entre países o bloques para reducir dependencia mutua.",
    "Sharp power": "Influencia política indirecta mediante medios, cultura, economía, información o tecnología.",
    "Diplomacia de deuda": "Influencia generada cuando un país presta dinero o financia proyectos y eso crea dependencia.",
    "Seguridad económica": "Protección de industrias clave como energía, chips, alimentos, puertos, datos y tecnología."
}

TRIVIA_PREGUNTAS = [
    {
        "pregunta": "¿Qué país es el principal rival estratégico de China?",
        "respuesta_mostrada": "Estados Unidos",
        "validas": ["estados unidos", "usa", "eeuu", "eua", "estadosunidos"],
        "explicacion": "China y Estados Unidos compiten en comercio, tecnología, poder militar e influencia global."
    },
    {
        "pregunta": "¿Por qué Taiwán es importante geopolíticamente?",
        "respuesta_mostrada": "Por su producción de semiconductores avanzados",
        "validas": ["semiconductores avanzados", "chips avanzados", "por su produccion de semiconductores avanzados", "por los chips", "semiconductores"],
        "explicacion": "Taiwán ocupa una posición crítica en la fabricación de chips avanzados usados en múltiples industrias."
    },
    {
        "pregunta": "¿Qué busca la Ruta de la Seda?",
        "respuesta_mostrada": "Expandir la influencia china mediante infraestructura, comercio y financiamiento",
        "validas": ["expandir la influencia china", "infraestructura comercio y financiamiento", "expandir influencia con infraestructura", "influencia china"],
        "explicacion": "China utiliza infraestructura y financiamiento como herramientas de proyección internacional."
    },
    {
        "pregunta": "¿Qué empresa china es famosa por el 5G?",
        "respuesta_mostrada": "Huawei",
        "validas": ["huawei"],
        "explicacion": "Huawei es una empresa clave en telecomunicaciones y redes 5G."
    },
    {
        "pregunta": "¿Qué significa multipolaridad?",
        "respuesta_mostrada": "Un mundo donde existen varias potencias importantes",
        "validas": ["varias potencias importantes", "mundo con varias potencias", "un mundo con varias potencias", "varias potencias"],
        "explicacion": "La multipolaridad describe un sistema internacional menos concentrado en una sola superpotencia."
    }
]

ESCENARIOS = {
    "A": {
        "titulo": "China invade Taiwán",
        "consecuencias": [
            "Crisis mundial de semiconductores.",
            "Posible respuesta militar o económica de Estados Unidos.",
            "Caída de bolsas internacionales.",
            "Afectación a celulares, autos, IA y computadoras.",
            "Empresas buscarían proveedores alternativos."
        ],
        "impacto": "Sería uno de los shocks económicos y tecnológicos más graves del siglo. La seguridad económica se volvería prioridad absoluta."
    },
    "B": {
        "titulo": "Estados Unidos bloquea chips avanzados a China",
        "consecuencias": [
            "China acelera su autosuficiencia tecnológica.",
            "Empresas chinas enfrentan retrasos.",
            "Aumenta la tensión comercial.",
            "Otros países ganan importancia en cadenas de suministro."
        ],
        "impacto": "El decoupling tecnológico se profundizaría y las empresas tendrían que rediseñar compras, producción y alianzas."
    },
    "C": {
        "titulo": "México aumenta su comercio con China",
        "consecuencias": [
            "Más importaciones baratas.",
            "Oportunidades para consumidores y empresas.",
            "Riesgo de presión política de Estados Unidos.",
            "Competencia para fabricantes mexicanos.",
            "Posibilidad de atraer inversión china."
        ],
        "impacto": "México ganaría margen comercial, pero también debería equilibrar cuidadosamente su relación con Washington."
    },
    "D": {
        "titulo": "China controla rutas marítimas estratégicas",
        "consecuencias": [
            "Mayor influencia sobre comercio global.",
            "Riesgo para países dependientes de esas rutas.",
            "Aumento en costos de transporte y seguros.",
            "Mayor presión sobre Estados Unidos y sus aliados."
        ],
        "impacto": "El control marítimo elevaría el poder geoeconómico chino y afectaría cadenas logísticas mundiales."
    }
}

TEMAS = {
    "1. Objetivo geopolítico de China": {
        "titulo": "1. OBJETIVO GEOPOLÍTICO DE CHINA",
        "resumen": "China busca convertirse en una potencia global en lo económico, tecnológico, militar y diplomático. Su estrategia está ligada al rejuvenecimiento nacional impulsado por Xi Jinping.",
        "importancia": "Esto cambia el equilibrio mundial porque China ya no acepta un sistema internacional dominado por completo por Estados Unidos.",
        "impacto": "Las empresas deben considerar a China como mercado, proveedor, competidor y riesgo geopolítico al mismo tiempo.",
        "dato": "China combina capitalismo de mercado con fuerte control estatal.",
        "reflexion": "¿Puede una economía crecer más rápido cuando el Estado dirige estratégicamente sus industrias?",
        "conceptos": ["Multipolaridad", "Sharp power", "Seguridad económica"]
    },
    "2. Relación China - Estados Unidos": {
        "titulo": "2. RELACIÓN CHINA - ESTADOS UNIDOS",
        "resumen": "China y Estados Unidos son socios comerciales, pero también rivales estratégicos en comercio, tecnología, IA, chips e influencia global.",
        "importancia": "Es una de las rivalidades más importantes del siglo XXI.",
        "impacto": "Las empresas enfrentan aranceles, sanciones, restricciones tecnológicas y cambios en cadenas de suministro.",
        "dato": "Aunque compiten, sus economías siguen profundamente conectadas.",
        "reflexion": "¿Es posible que dos países sean enemigos estratégicos y socios económicos al mismo tiempo?",
        "conceptos": ["Trampa de Tucídides", "Decoupling"]
    },
    "3. Taiwán y el riesgo de conflicto": {
        "titulo": "3. TAIWÁN Y EL RIESGO DE CONFLICTO",
        "resumen": "China considera a Taiwán parte de su territorio, mientras Taiwán funciona con gobierno propio y apoyo político-militar de Estados Unidos.",
        "importancia": "Un conflicto en Taiwán afectaría la economía mundial por su papel central en semiconductores avanzados.",
        "impacto": "Podría provocar escasez de chips para celulares, autos, computadoras, inteligencia artificial y equipos médicos.",
        "dato": "Taiwán es pequeño en territorio, pero enorme en importancia tecnológica.",
        "reflexion": "¿Qué pasaría con las empresas si se detiene la producción de chips?",
        "conceptos": ["Seguridad económica", "Decoupling"]
    },
    "4. Ruta de la Seda / Belt and Road Initiative": {
        "titulo": "4. RUTA DE LA SEDA / BELT AND ROAD INITIATIVE",
        "resumen": "China financia y construye infraestructura en otros países para expandir rutas comerciales y su influencia política y económica.",
        "importancia": "Le permite ganar acceso a recursos, puertos, carreteras, trenes y aliados estratégicos.",
        "impacto": "Abre oportunidades de inversión y comercio, pero también puede crear dependencia financiera.",
        "dato": "China muchas veces influye más mediante deuda, comercio e infraestructura que mediante fuerza militar.",
        "reflexion": "¿La inversión china es una oportunidad o una forma de dependencia?",
        "conceptos": ["Diplomacia de deuda", "Sharp power"]
    },
    "5. Tecnología: IA, chips, 5G y Huawei": {
        "titulo": "5. TECNOLOGÍA: IA, CHIPS, 5G Y HUAWEI",
        "resumen": "China busca liderar inteligencia artificial, telecomunicaciones 5G, autos eléctricos, vigilancia digital y semiconductores.",
        "importancia": "La tecnología define quién tendrá más poder económico y militar en el futuro.",
        "impacto": "Las empresas dependen cada vez más de datos, conectividad, chips y plataformas digitales.",
        "dato": "La guerra tecnológica no se pelea con tanques, sino con chips, algoritmos y restricciones comerciales.",
        "reflexion": "¿Quién controla más el futuro: el país con más petróleo o el país con mejores chips?",
        "conceptos": ["Seguridad económica", "Decoupling"]
    },
    "6. China en América Latina y México": {
        "titulo": "6. CHINA EN AMÉRICA LATINA Y MÉXICO",
        "resumen": "China ha aumentado su presencia en América Latina mediante comercio, inversión, financiamiento e infraestructura.",
        "importancia": "La región puede beneficiarse, pero también volverse dependiente de productos y capital chino.",
        "impacto": "México puede aprovechar el nearshoring, pero también compite con China en manufactura.",
        "dato": "México está en una posición estratégica porque comercia con China, pero depende mucho de Estados Unidos.",
        "reflexion": "¿México debería acercarse más a China o cuidar más su relación con Estados Unidos?",
        "conceptos": ["Sharp power", "Seguridad económica"]
    },
    "7. Mar del Sur de China": {
        "titulo": "7. MAR DEL SUR DE CHINA",
        "resumen": "Es una zona estratégica por donde pasan rutas comerciales esenciales y donde China ha construido islas artificiales con infraestructura militar.",
        "importancia": "Controlar esa zona significa influir sobre una parte enorme del comercio marítimo mundial.",
        "impacto": "Una crisis ahí puede afectar transporte marítimo, seguros, petróleo, comercio y cadenas de suministro.",
        "dato": "A veces una isla artificial puede tener más valor estratégico que una ciudad.",
        "reflexion": "¿Por qué controlar el mar puede ser tan importante como controlar tierra?",
        "conceptos": ["Multipolaridad", "Seguridad económica"]
    },
    "8. China y Rusia": {
        "titulo": "8. CHINA Y RUSIA",
        "resumen": "China y Rusia mantienen una relación estratégica basada en oposición a la influencia occidental, aunque no son aliados perfectos.",
        "importancia": "Su relación puede fortalecer un bloque alternativo frente a Estados Unidos y Europa.",
        "impacto": "Afecta mercados de energía, sanciones, comercio internacional y rutas financieras.",
        "dato": "China puede beneficiarse de Rusia sin depender completamente de ella.",
        "reflexion": "¿China y Rusia son verdaderos aliados o solo socios por conveniencia?",
        "conceptos": ["Multipolaridad", "Sharp power"]
    },
    "9. Riesgos económicos internos de China": {
        "titulo": "9. RIESGOS ECONÓMICOS INTERNOS DE CHINA",
        "resumen": "China enfrenta desaceleración económica, envejecimiento poblacional, crisis inmobiliaria, desempleo juvenil y deuda local.",
        "importancia": "Si China se desacelera, afecta a todo el mundo porque es una pieza central del comercio global.",
        "impacto": "Puede bajar la demanda de materias primas, afectar exportaciones y modificar inversiones globales.",
        "dato": "El mayor reto de China podría no ser Estados Unidos, sino sus propios problemas internos.",
        "reflexion": "¿Una potencia puede ser fuerte hacia afuera pero vulnerable por dentro?",
        "conceptos": ["Seguridad económica"]
    },
}

# ============================================================
# HELPERS
# ============================================================

def normalizar(texto):
    texto = texto.strip().lower()
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")

def hero(titulo, subtitulo):
    st.markdown(f'<div class="hero"><h1>🌏 {titulo}</h1><p>{subtitulo}</p></div>', unsafe_allow_html=True)

def subhero(titulo, subtitulo):
    st.markdown(f'<div class="subhero"><h2 style="margin:0;">{titulo}</h2><p style="margin:8px 0 0 0;">{subtitulo}</p></div>', unsafe_allow_html=True)

def tarjeta(titulo, contenido, clase="card"):
    st.markdown(f'<div class="{clase}"><h3 style="margin-top:0;">{titulo}</h3><p style="margin-bottom:0;line-height:1.6;">{contenido}</p></div>', unsafe_allow_html=True)

def mostrar_conceptos(claves):
    items = "".join([f"<li><b>{c}:</b> {CONCEPTOS_AVANZADOS.get(c,'')}</li>" for c in claves])
    st.markdown(f'<div class="card-green"><h3 style="margin-top:0;">📘 Conceptos avanzados relacionados</h3><ul style="line-height:1.7;margin-bottom:0;">{items}</ul></div>', unsafe_allow_html=True)

# ============================================================
# ESTADO
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
if "trivia_idx" not in st.session_state:
    st.session_state.trivia_idx = 0
if "trivia_puntaje" not in st.session_state:
    st.session_state.trivia_puntaje = 0
if "trivia_respondida" not in st.session_state:
    st.session_state.trivia_respondida = False
if "trivia_feedback" not in st.session_state:
    st.session_state.trivia_feedback = None

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("### 🌏 Navegación")
    if st.button("🏠 Inicio", use_container_width=True):
        st.session_state.pagina = "inicio"
        st.rerun()
    st.markdown("**📚 Temas**")
    for nombre in TEMAS:
        if st.button(nombre, use_container_width=True, key=f"btn_{nombre}"):
            st.session_state.pagina = nombre
            st.rerun()
    st.markdown("**🎮 Actividades**")
    if st.button("🎯 Trivia geopolítica", use_container_width=True):
        st.session_state.pagina = "trivia"
        st.session_state.trivia_idx = 0
        st.session_state.trivia_puntaje = 0
        st.session_state.trivia_respondida = False
        st.session_state.trivia_feedback = None
        st.rerun()
    if st.button("🧪 Simulador ¿Qué pasaría si...?", use_container_width=True):
        st.session_state.pagina = "simulador"
        st.rerun()
    st.markdown("---")
    st.caption("Desarrollado por: Samuel Izquierdo Cuervo")

# ============================================================
# PÁGINAS
# ============================================================

pagina = st.session_state.pagina

# INICIO
if pagina == "inicio":
    hero("LA GEOPOLÍTICA DE CHINA", "Mini centro interactivo de análisis geopolítico • Modo analista activado")
    tarjeta("🚀 Bienvenido/a",
        "Este programa es una mini página web interactiva para explorar tensiones globales, relaciones estratégicas, "
        "riesgos económicos, tecnología, trivia y escenarios internacionales relacionados con China.",
        "card-gold")
    st.markdown("""
    <div class="footer-box">
        <b>🧭 Qué puedes hacer aquí:</b><br>
        • Consultar temas estratégicos desde el menú lateral<br>
        • Responder una trivia geopolítica<br>
        • Explorar el simulador internacional<br>
        • Navegar libremente entre secciones
    </div>
    """, unsafe_allow_html=True)

# TEMAS
elif pagina in TEMAS:
    t = TEMAS[pagina]
    hero(t["titulo"], "Reporte estratégico generado")
    tarjeta("📌 Resumen", t["resumen"], "card")
    tarjeta("🌐 Importancia", t["importancia"], "card-red")
    tarjeta("💼 Impacto en negocios", t["impacto"], "card")
    tarjeta("✨ Dato interesante", t["dato"], "card-gold")
    mostrar_conceptos(t["conceptos"])
    tarjeta("🧠 Pregunta de reflexión", t["reflexion"], "card-green")

# TRIVIA
elif pagina == "trivia":
    idx = st.session_state.trivia_idx
    total = len(TRIVIA_PREGUNTAS)

    if idx >= total:
        puntaje = st.session_state.trivia_puntaje
        hero("🏁 RESULTADO FINAL", "Reporte estratégico generado")
        if puntaje == 5:
            msg = f"Tu puntaje fue: <b>{puntaje} de {total}</b><br><br>🏆 Nivel excelente: visión geopolítica de alto nivel."
        elif puntaje >= 3:
            msg = f"Tu puntaje fue: <b>{puntaje} de {total}</b><br><br>🌟 Buen nivel: tienes una base sólida."
        else:
            msg = f"Tu puntaje fue: <b>{puntaje} de {total}</b><br><br>📚 Nivel inicial: sigue explorando el centro de análisis."
        st.markdown(f'<div class="score-box"><h2 style="margin-top:0;">Resultado</h2><p style="margin-bottom:0;line-height:1.7;">{msg}</p></div>', unsafe_allow_html=True)
        if st.button("🔄 Intentar de nuevo"):
            st.session_state.trivia_idx = 0
            st.session_state.trivia_puntaje = 0
            st.session_state.trivia_respondida = False
            st.session_state.trivia_feedback = None
            st.rerun()
    else:
        subhero(f"Pregunta {idx+1} de {total}", "Procesando conocimiento geopolítico...")
        p = TRIVIA_PREGUNTAS[idx]
        tarjeta("❓ Pregunta", p["pregunta"], "card")

        if not st.session_state.trivia_respondida:
            respuesta = st.text_input("Tu respuesta:", key=f"resp_{idx}")
            if st.button("✅ Responder"):
                r_norm = normalizar(respuesta)
                validas_n = [normalizar(v) for v in p["validas"]]
                if r_norm in validas_n:
                    st.session_state.trivia_puntaje += 1
                    st.session_state.trivia_feedback = "correcto"
                else:
                    st.session_state.trivia_feedback = "incorrecto"
                st.session_state.trivia_respondida = True
                st.rerun()
        else:
            fb = st.session_state.trivia_feedback
            if fb == "correcto":
                tarjeta("✅ Correcto", "Muy buena respuesta. Tu radar geopolítico está funcionando correctamente.", "card-green")
            else:
                tarjeta("❌ Incorrecto", f"Respuesta esperada: <b>{p['respuesta_mostrada']}</b>", "card-red")
            tarjeta("📘 Explicación", p["explicacion"], "card")
            if st.button("➡️ Siguiente pregunta"):
                st.session_state.trivia_idx += 1
                st.session_state.trivia_respondida = False
                st.session_state.trivia_feedback = None
                st.rerun()

# SIMULADOR
elif pagina == "simulador":
    hero("🧪 SIMULADOR ¿QUÉ PASARÍA SI...?", "Explora escenarios internacionales de alto impacto")
    cols = st.columns(2)
    opciones = list(ESCENARIOS.keys())
    for i, clave in enumerate(opciones):
        with cols[i % 2]:
            e = ESCENARIOS[clave]
            if st.button(f"**{clave}. {e['titulo']}**", use_container_width=True, key=f"esc_{clave}"):
                st.session_state.escenario_sel = clave
                st.rerun()

    if "escenario_sel" in st.session_state:
        clave = st.session_state.escenario_sel
        e = ESCENARIOS[clave]
        st.markdown("---")
        subhero(f"🔮 {e['titulo']}", "Procesando escenario internacional...")
        cons_html = "".join([f"<li>{c}</li>" for c in e["consecuencias"]])
        st.markdown(f'<div class="card-red"><h3 style="margin-top:0;">⚠️ Consecuencias posibles</h3><ul style="line-height:1.8;margin-bottom:0;">{cons_html}</ul></div>', unsafe_allow_html=True)
        tarjeta("💼 Lectura estratégica", e["impacto"], "card-gold")
