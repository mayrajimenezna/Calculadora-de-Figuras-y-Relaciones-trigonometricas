import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://web.resource.org/cc/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="200"
   height="200"
   id="svg2"
   sodipodi:version="0.32"
   inkscape:version="0.44"
   version="1.0"
   sodipodi:docbase="D:\"
   sodipodi:docname="Triángulo equilátero.svg">
  <defs
     id="defs4">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient3670">
      <stop
         style="stop-color:#b7ff43;stop-opacity:1;"
         offset="0"
         id="stop3672" />
      <stop
         style="stop-color:#b7ff43;stop-opacity:0;"
         offset="1"
         id="stop3674" />
    </linearGradient>
    <marker
       inkscape:stockid="Arrow2Mend"
       orient="auto"
       refY="0"
       refX="0"
       id="Arrow2Mend"
       style="overflow:visible">
      <path
         id="path15482"
         style="font-size:12px;fill-rule:evenodd;stroke-width:0.625;stroke-linejoin:round"
         d="M 8.7185878,4.0337352 L -2.2072895,0.016013256 L 8.7185884,-4.0017078 C 6.97309,-1.6296469 6.9831476,1.6157441 8.7185878,4.0337352 z "
         transform="scale(-0.6,-0.6)" />
    </marker>
    <marker
       inkscape:stockid="Arrow1Lend"
       orient="auto"
       refY="0"
       refX="0"
       id="Arrow1Lend"
       style="overflow:visible">
      <path
         id="path15506"
         d="M 0,0 L 5,-5 L -12.5,0 L 5,5 L 0,0 z "
         style="fill-rule:evenodd;stroke:black;stroke-width:1pt;marker-start:none"
         transform="matrix(-0.8,0,0,-0.8,-10,0)" />
    </marker>
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient3670"
       id="linearGradient3676"
       x1="5.7683712e-007"
       y1="63.499996"
       x2="199.99998"
       y2="63.499996"
       gradientUnits="userSpaceOnUse"
       gradientTransform="translate(-1.054972e-5,2.538617e-6)" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient3670"
       id="linearGradient3697"
       gradientUnits="userSpaceOnUse"
       x1="-0.50507569"
       y1="199.87059"
       x2="199.4949"
       y2="0.87053877"
       gradientTransform="translate(0,-2.395504e-5)" />
  </defs>
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="1.979899"
     inkscape:cx="59.096322"
     inkscape:cy="125.61511"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     width="200px"
     height="200px"
     showgrid="true"
     gridspacingx="10px"
     gridspacingy="10px"
     inkscape:showpageshadow="false"
     showborder="true"
     borderlayer="false"
     inkscape:window-width="1239"
     inkscape:window-height="881"
     inkscape:window-x="29"
     inkscape:window-y="-4"
     showguides="true"
     inkscape:guide-bbox="false"
     inkscape:object-paths="false"
     inkscape:grid-points="false"
     inkscape:grid-bbox="false"
     gridtolerance="50" />
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Capa 1"
     inkscape:groupmode="layer"
     id="layer1">
    <path
       style="fill:url(#linearGradient3697);fill-opacity:1;fill-rule:evenodd;stroke:blue;stroke-width:2.99999857;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="M 31.499999,158.50009 L 168.50007,158.50009 L 100.24429,31.500088 L 31.499999,158.50009 z "
       id="path1876"
       sodipodi:nodetypes="cccc" />
  </g>
</svg>

# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")
