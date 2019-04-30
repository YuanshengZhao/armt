# hand
# glf, Xheight, itaslope
import math

def gen(htc,ita):
    global enc,encd,lim,glfdat
    while(enc<=encd):
        nm=("u%X" % (enc))
        if(nm[-1]=="A" or nm[-1]=="B" or nm[-1]=="C" or nm[-1]=="D" or nm[-1]=="E" or nm[-1]=="F"):
            nm=nm[:-1]+"_"+nm[-1]
        if(enc<lim): 
            ht=-1
        else:
            ht=htc
        glfdat=glfdat+[[nm, ht, ita]]
        enc=enc+1


glfdat=[# Latin
    ["_A"        , -1    , 0      ],
    ["_B"        , -1    , 0      ],
    ["_C"        , -1    , 0      ],
    ["_D"        , -1    , 0      ],
    ["_E"        , -1    , 0      ],
    ["_F"        , -1    , 0      ],
    ["_G"        , -1    , 0      ],
    ["_H"        , -1    , 0      ],
    ["_I"        , -1    , 0      ],
    ["_J"        , -1    , 0      ],
    ["_K"        , -1    , 0      ],
    ["_L"        , -1    , 0      ],
    ["_M"        , -1    , 0      ],
    ["_N"        , -1    , 0      ],
    ["_O"        , -1    , 0      ],
    ["_P"        , -1    , 0      ],
    ["_Q"        , -1    , 0      ],
    ["_R"        , -1    , 0      ],
    ["_S"        , -1    , 0      ],
    ["_T"        , -1    , 0      ],
    ["_U"        , -1    , 0      ],
    ["_V"        , -1    , 0      ],
    ["_W"        , -1    , 0      ],
    ["_X"        , -1    , 0      ],
    ["_Y"        , -1    , 0      ],
    ["_Z"        , -1    , 0      ],
    ["a"         , 450   , 0      ],
    ["b"         , 450   , 0      ],
    ["c"         , 450   , 0      ],
    ["d"         , 450   , 0      ],
    ["e"         , 450   , 0      ],
    ["f"         , 450   , 0      ],
    ["g"         , 450   , 0      ],
    ["h"         , 450   , 0      ],
    ["i"         , 450   , 0      ],
    ["j"         , 450   , 0      ],
    ["k"         , 450   , 0      ],
    ["l"         , 450   , 0      ],
    ["m"         , 450   , 0      ],
    ["n"         , 450   , 0      ],
    ["o"         , 450   , 0      ],
    ["p"         , 450   , 0      ],
    ["q"         , 450   , 0      ],
    ["r"         , 450   , 0      ],
    ["s"         , 450   , 0      ],
    ["t"         , 450   , 0      ],
    ["u"         , 450   , 0      ],
    ["v"         , 450   , 0      ],
    ["w"         , 450   , 0      ],
    ["x"         , 450   , 0      ],
    ["y"         , 450   , 0      ],
    ["z"         , 450   , 0      ],
    ["dotlessi"  , 450   , 0      ],
    ["uni0237"   , 450   , 0      ]
]

glfdat+=[# Greek
    ["_Gamma"     , -1    , 0      ],
    ["uni0394"    , -1    , 0      ],
    ["_Theta"     , -1    , 0      ],
    ["_Lambda"    , -1    , 0      ],
    ["_Xi"        , -1    , 0      ],
    ["_Pi"        , -1    , 0      ],
    ["_Sigma"     , -1    , 0      ],
    ["_Upsilon"   , -1    , 0      ],
    ["_Phi"       , -1    , 0      ],
    ["_Psi"       , -1    , 0      ],
    ["_Omega"     , -1    , 0      ],
    ["alpha"      , 450   , 0      ],
    ["beta"       , 450   , 0      ],
    ["gamma"      , 450   , 0      ],
    ["delta"      , 450   , 0      ],
    ["epsilon"    , 450   , 0      ],
    ["zeta"       , 450   , 0      ],
    ["eta"        , 450   , 0      ],
    ["theta"      , 450   , 0      ],
    ["iota"       , 450   , 0      ],
    ["kappa"      , 450   , 0      ],
    ["lambda"     , 450   , 0      ],
    ["mu"         , 450   , 0      ],
    ["nu"         , 450   , 0      ],
    ["xi"         , 450   , 0      ],
    ["pi"         , 450   , 0      ],
    ["rho"        , 450   , 0      ],
    ["sigma1"     , 450   , 0      ],
    ["sigma"      , 450   , 0      ],
    ["tau"        , 450   , 0      ],
    ["upsilon"    , 450   , 0      ],
    ["phi"        , 450   , 0      ],
    ["chi"        , 450   , 0      ],
    ["psi"        , 450   , 0      ],
    ["omega"      , 450   , 0      ],
    ["theta1"     , 450   , 0      ],
    ["phi1"       , 450   , 0      ],
    ["omega1"     , 450   , 0      ],
    ["uni03DC"    , -1    , 0      ],# Digamma
    ["uni03F0"    , 450   , 0      ],
    ["uni03F1"    , 450   , 0      ],
    ["uni03F5"    , 450   , 0      ],
    ["uni03F6"    , 450   , 0      ],
    ["gradient"   , -1    , 0      ]

]


# bf it ltn
enc= int("1D400",base=16);
encd=int("1D433",base=16);
lim= int("1D41A",base=16);
gen(461,0)

# it ltn
slp=math.tan(15.5*math.pi/180.0)
enc= int("1D434",base=16);
encd=int("1D467",base=16);
lim= int("1D44E",base=16);
glfdat+=[# Italic Latin
    ["uni210E"   , 450   , slp    ],
    ["uni210F"   , 450   , slp    ],
    # ["u1D456"    , 450   , slp    ], # h
    ["u1D6A4"    , 450   , slp    ], # dotless i
    ["u1D6A5"    , 450   , slp    ],
]
gen(450,slp)


# bf it ltn
slp=math.tan(15.3*math.pi/180.0)
enc= int("1D468",base=16);
encd=int("1D49B",base=16);
lim= int("1D482",base=16);
gen(461,slp)

# scr ltn
slp=math.tan(15.5*math.pi/180.0)
enc= int("1D49C",base=16);
encd=int("1D4CF",base=16);
lim= int("1D4B6",base=16);
glfdat+=[
    ["uni212C"   , -1    , slp   ],
    # ["u1D49_D"   , -1    , slp   ], # B
    ["uni2130"   , -1    , slp   ],
    # ["u1D4A0"    , -1    , slp   ], # E
    ["uni2131"   , -1    , slp   ],
    # ["u1D4A1"    , -1    , slp   ], # F
    ["uni210B"   , -1    , slp   ],
    # ["u1D4A3"    , -1    , slp   ], # H
    ["uni2110"   , -1    , slp   ],
    # ["u1D4A4"    , -1    , slp   ], # I
    ["uni2112"   , -1    , slp   ],
    # ["u1D4A7"    , -1    , slp   ], # L
    ["uni2133"   , -1    , slp   ],
    # ["u1D4A8"    , -1    , slp   ], # M
    ["uni211B"   , -1    , slp   ],
    # ["u1D4A_D"   , -1    , slp   ], # R
    ["uni2113"   , 450   , slp   ], # l
]
gen(450,slp)

# bf scr ltn
slp=math.tan(15.3*math.pi/180.0)
enc= int("1D4D0",base=16);
encd=int("1D503",base=16);
lim= int("1D4EA",base=16);
gen(450,slp)

# frk ltn
enc= int("1D504",base=16);
encd=int("1D537",base=16);
lim= int("1D51E",base=16);
glfdat+=[
    ["uni212D"   , -1    , 0      ],
    # ["u1D506"    , -1    , 0      ], # C
    ["uni210C"   , -1    , 0      ],
    # ["u1D50_B"   , -1    , 0      ], # H
    ["_Ifraktur"  , -1    , 0      ],
    # ["u1D50_C"   , -1    , 0      ], # I
    ["_Rfraktur"  , -1    , 0      ],
    # ["u1D515"    , -1    , 0      ], # R
    ["uni2128"   , -1    , 0      ],
    # ["u1D51_D"   , -1    , 0      ], # Z
]
gen(478,0)


# bb ltn
enc= int("1D538",base=16);
encd=int("1D56B",base=16);
lim= int("1D552",base=16);
glfdat+=[
    ["uni2102"   , -1    , 0      ],
    # ["u1D53_A"   , -1    , 0      ], # C
    ["uni210D"   , -1    , 0      ],
    # ["u1D53_F"   , -1    , 0      ], # H
    ["uni2115"   , -1    , 0      ],
    # ["u1D545"    , -1    , 0      ], # N
    ["uni2119"   , -1    , 0      ],
    # ["u1D547"    , -1    , 0      ], # P
    ["uni211A"   , -1    , 0      ],
    # ["u1D548"    , -1    , 0      ], # Q
    ["uni211D"   , -1    , 0      ],
    # ["u1D549"    , -1    , 0      ], # R
    ["uni2124"   , -1    , 0      ],
    # ["u1D551"    , -1    , 0      ], # Z
]
gen(450,0)

# bf frk ltn
enc= int("1D56C",base=16);
encd=int("1D59F",base=16);
lim= int("1D586",base=16);
gen(510,0)

# sf ltn
enc= int("1D5A0",base=16);
encd=int("1D5D3",base=16);
lim= int("1D5BA",base=16);
gen(524,0)

# bf sf ltn
enc= int("1D5D4",base=16);
encd=int("1D607",base=16);
lim= int("1D5EE",base=16);
gen(540,0)

# it sf ltn
slp=math.tan(12.0*math.pi/180.0)
enc= int("1D608",base=16);
encd=int("1D63B",base=16);
lim= int("1D622",base=16);
gen(524,slp)

# bf it sf ltn
enc= int("1D63C",base=16);
encd=int("1D66F",base=16);
lim= int("1D656",base=16);
gen(540,slp)

# tt ltn
enc= int("1D670",base=16);
encd=int("1D6A3",base=16);
lim=int("1D68A",base=16);
gen(417,0)

# bf grk
enc= int("1D6A8",base=16);
encd=int("1D6E1",base=16);
lim=int("1D6C2",base=16);
gen(461,0)

# it grk
slp=math.tan(15.5*math.pi/180.0)
enc= int("1D6E2",base=16);
encd=int("1D71B",base=16);
lim=int("1D6FC",base=16);
gen(450,slp)

# bf it grk
slp=math.tan(15.3*math.pi/180.0)
enc= int("1D71C",base=16);
encd=int("1D755",base=16);
lim=int("1D736",base=16);
gen(461,slp)

# bf sf grk
enc= int("1D756",base=16);
encd=int("1D76E",base=16);
lim=int("1D76E",base=16);
gen(450,0)

# digits
enc= int("1D7CE",base=16);
encd=int("1D7FF",base=16);
lim= int("1D7FF",base=16);
glfdat+=[
    ["zero"       , -1    , 0      ],
    ["one"        , -1    , 0      ],
    ["two"        , -1    , 0      ],
    ["three"      , -1    , 0      ],
    ["four"       , -1    , 0      ],
    ["five"       , -1    , 0      ],
    ["six"        , -1    , 0      ],
    ["seven"      , -1    , 0      ],
    ["eight"      , -1    , 0      ],
    ["nine"       , -1    , 0      ],
]
gen(450,0)

# print(len(glfdat))