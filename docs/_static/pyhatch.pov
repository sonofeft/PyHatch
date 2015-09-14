// Persistence of Vision Ray Tracer Scene Description File
// File: ?.pov
// Vers: 3.6
// Desc: Basic TTF font Example
// Date: mm/dd/yy
// Auth: ?
//

#version 3.7;      

#include "glass.inc"
#include "colors.inc"                       

#declare BackColv1 = rgb <.1255,.29,.5294>;
#declare BackCol = rgb <1,1,1>;
#declare PlaneCol = rgb <.2,.4,.6>;            



global_settings {
  assumed_gamma 1.0
}

// ----------------------------------------

sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 color BackCol ]
      [1.0 color rgb 1]
    }
  }
}

light_source {
  <0, 0, 0>            // light's position (translated below)
  color rgb <1, 1, 1>  // light's color
  translate <-40, 120, -120>
}

light_source {
  <0, 0, 0>            // light's position (translated below)
  color rgb <1, 1, 1>  // light's color
  translate <-30, 300, -10>
}

light_source {
  <0, 0, 0>            // light's position (translated below)
  color rgb <1, 1, 1>  // light's color
  translate <300, 300, -300>  

}

// ----------------------------------------

#declare Text_Tex = texture {
  pigment { OrangeRed  }
  finish { specular 0.3 ambient 0.2  }        
}


text {
  ttf "snap____.ttf", "PyHatch",       //beesknee.ttf Pristina.ttf  matisse_.ttf harlowsi.ttf
  1, // depth
  0  // spacing
  scale <0.75, 2.5, 1> // stretch it taller
  texture { Text_Tex }
  translate <-1, 0, 0>
  //rotate <30*sin(clock*4*pi), 20*sin(clock*2*pi), 0>
  translate <-2, 0, 3>
}


camera {
  location  <-0.85, 0.0, -1.5>
  direction 1.5*z
  right     4/3*x
  look_at   <-0.95, 0.15,  0.0>
}

plane { y, -2 pigment { PlaneCol } 
  finish {  diffuse albedo 0.0 ambient PlaneCol  }        

}

