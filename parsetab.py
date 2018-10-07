
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BLUE BOOL CIRCLE COLOR COMMA CTE_BOOL CTE_FLOAT CTE_INT CTE_STRING DAVINCI DIVIDE ELSE EQUAL EXPRESSION FALSE FLOAT GREATER GREATEROREQUAL GREEN ID IF INT LBRACE LBRACKET LESSER LESSEROREQUAL LPAREN MINUS NOT NOTEQUAL OR PENBACK PENFORWARD PENOFF PENON PENSIZE PINK PLUS POLIGON PROGRAM PURPLE RBRACE RBRACKET RECTANGLE RED RETURN ROTATE RPAREN SEMICOLON SIZE SQUARE STRING ST_CTE TERM TIMES TRIANGLE TRUE VAR VOID WHILE YELLOWprogram : PROGRAM ID SEMICOLON program1 DAVINCI blockprogram1 : funcs\n\t| vars\n\t| funcs vars\n\t| vars funcs\n\t| emptyblock : LBRACE b1 RBRACEb1 : vars b2 \n\t| b2b2 : statute\n\t| statute b2\n\t| emptyvars : VAR vars2vars2 : type vars3 SEMICOLON vars2\n\t| type vars3 SEMICOLONvars3 : ID ASSIGN expression vars4\n\t| ID list vars4\n\t| ID vars4vars4 : COMMA vars3\n\t| emptylist : LBRACKET expression RBRACKETstatute : assignment\n\t | call\n\t | condition\n\t | triangle\n\t | rectangle\n\t | square\n\t | circle\n\t | poligon\n\t | color\n\t | pensize\n\t | penforward\n\t | penback\n\t | rotate\n\t | WHILE\n\t | return\n\t | penon\n\t | penoffassignment : ID ASSIGN expression SEMICOLON\n\t | ID LBRACKET exp RBRACKET ASSIGN expression SEMICOLONcolor_cte : RED\n\t\t| BLUE\n\t\t| YELLOW\n\t\t| GREEN\n\t\t| PINK\n\t\t| PURPLEst_cte : STRING\n\t\t| cte_boolfuncs : type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3\n\t| VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3 funcs1 : COMMA type ID funcs1\n\t| emptyfuncs2 : vars\n\t| vars statute\n\t| statute vars\n\t| statute\n\t| empty funcs3 : funcs\n\t| emptycolor : COLOR LPAREN color_cte RPAREN SEMICOLONcircle : CIRCLE LPAREN exp RPAREN SEMICOLONsquare : SQUARE LPAREN exp RPAREN SEMICOLONtriangle : TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLONrectangle : RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLONpoligon : POLIGON LPAREN exp COMMA exp RPAREN SEMICOLONrotate : ROTATE LPAREN exp RPAREN SEMICOLON\n\t| ROTATE LPAREN CTE_STRING RPAREN SEMICOLONpensize : PENSIZE LPAREN exp RPAREN SEMICOLONpenforward : PENFORWARD LPAREN exp RPAREN SEMICOLONpenback : PENBACK LPAREN exp RPAREN SEMICOLONpenon : PENON LPAREN RPAREN SEMICOLONpenoff : PENOFF LPAREN RPAREN SEMICOLONtype : INT\n\t\t| FLOAT\n\t\t| STRING\n\t\t| BOOLcte_bool : TRUE\n\t\t\t\t| FALSEvar_cte : ID var_cte1\n\t\t\t\t| CTE_INT\n\t\t\t\t| CTE_FLOAT\n\t\t\t\t| CTE_BOOL\n\t\t\t\t| callvar_cte1 : LBRACKET exp RBRACKET\n\t\t\t\t | LPAREN exp RPAREN\n\t\t\t\t | emptycondition : IF LPAREN EXPRESSION RPAREN block condition1 SEMICOLONcondition1 : ELSE block\n\t| emptyexpression : exp expression1expression1 : LESSER exp\n\t| GREATER exp\n\t| EQUAL exp\n\t| NOTEQUAL exp\n\t| GREATEROREQUAL exp\n    | LESSEROREQUAL exp\n    | emptyexp : term exp1exp1 : MINUS exp\n\t| PLUS exp\n\t| emptyfactor : LPAREN EXPRESSION RPAREN\n\t| var_cte\n\t| factor1 var_ctefactor1 : MINUS \n\t| PLUS\n\t| emptyterm : factor term1term1 : DIVIDE term\n\t\t| TIMES term\n\t\t| emptycall : ID LPAREN call1 RPAREN SEMICOLONcall1 : ID COMMA call1\n\t| exp\n\t| st_ctereturn : RETURN var_cte SEMICOLON\n\t\t\t| RETURN st_cte SEMICOLONempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,23,75,],[0,-1,-7,]),'ID':([2,9,10,12,13,14,15,21,22,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,63,66,67,68,69,72,73,78,79,80,82,83,84,85,86,88,89,90,91,107,114,115,116,117,145,146,148,149,159,160,161,162,163,164,167,168,171,172,177,179,182,183,186,195,196,198,211,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[3,19,20,-73,-74,-75,-76,-13,28,51,51,51,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,94,105,106,-15,94,94,28,94,94,123,94,94,94,94,94,94,94,94,94,-14,94,-105,-106,-107,-116,-117,123,94,94,94,94,94,94,94,94,94,94,94,-39,123,94,94,94,-71,-72,229,94,-112,-62,-61,-60,-68,-69,-70,-66,-67,51,51,51,-40,-87,-63,-64,-65,]),'SEMICOLON':([3,27,28,70,71,74,75,92,93,94,95,96,97,98,99,100,101,102,108,109,110,111,113,118,120,121,147,150,151,152,157,158,165,166,169,170,173,175,176,180,184,185,187,188,189,190,191,192,200,201,202,203,204,205,206,207,208,209,210,213,214,226,227,231,232,234,235,236,237,246,],[4,68,-118,-18,-118,-20,-7,145,146,-118,-80,-81,-82,-83,-47,-48,-77,-78,-118,-118,-118,-118,-103,-17,-19,177,-79,-86,195,196,-16,-90,-97,-98,-101,-108,-111,-104,-21,213,217,218,220,221,222,223,224,225,-91,-92,-93,-94,-95,-96,-99,-100,-109,-110,-102,-112,-118,-85,-84,244,245,-89,247,248,249,-88,]),'VOID':([4,7,21,68,107,250,253,],[10,10,-13,-15,-14,10,10,]),'VAR':([4,6,24,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,240,244,245,247,248,249,250,253,254,255,256,257,],[11,11,11,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,11,11,11,-40,-87,-63,-64,-65,-118,-118,-49,-58,-59,-50,]),'DAVINCI':([4,5,6,7,8,17,18,21,68,107,250,253,254,255,256,257,],[-118,16,-2,-3,-6,-4,-5,-13,-15,-14,-118,-118,-49,-58,-59,-50,]),'INT':([4,7,11,21,25,26,68,107,154,250,253,],[12,12,12,-13,12,12,12,-14,12,12,12,]),'FLOAT':([4,7,11,21,25,26,68,107,154,250,253,],[13,13,13,-13,13,13,13,-14,13,13,13,]),'STRING':([4,7,11,21,25,26,63,68,80,107,148,154,179,250,253,],[14,14,14,-13,14,14,99,14,99,-14,99,14,99,14,14,]),'BOOL':([4,7,11,21,25,26,68,107,154,250,253,],[15,15,15,-13,15,15,15,-14,15,15,15,]),'LBRACE':([16,181,197,199,233,],[24,24,228,230,24,]),'LPAREN':([19,20,51,52,53,54,55,56,57,58,59,60,61,62,64,65,69,72,78,79,80,82,83,84,85,86,88,89,90,91,94,123,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[25,26,80,81,82,83,84,85,86,87,88,89,90,91,103,104,112,112,112,112,112,112,112,112,112,112,112,112,112,112,148,148,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'WHILE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,47,47,47,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,47,47,47,-40,-87,-63,-64,-65,]),'IF':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,52,52,52,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,52,52,52,-40,-87,-63,-64,-65,]),'TRIANGLE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,53,53,53,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,53,53,53,-40,-87,-63,-64,-65,]),'RECTANGLE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,54,54,54,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,54,54,54,-40,-87,-63,-64,-65,]),'SQUARE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,55,55,55,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,55,55,55,-40,-87,-63,-64,-65,]),'CIRCLE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,56,56,56,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,56,56,56,-40,-87,-63,-64,-65,]),'POLIGON':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,57,57,57,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,57,57,57,-40,-87,-63,-64,-65,]),'COLOR':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,58,58,58,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,58,58,58,-40,-87,-63,-64,-65,]),'PENSIZE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,59,59,59,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,59,59,59,-40,-87,-63,-64,-65,]),'PENFORWARD':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,60,60,60,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,60,60,60,-40,-87,-63,-64,-65,]),'PENBACK':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,61,61,61,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,61,61,61,-40,-87,-63,-64,-65,]),'ROTATE':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,62,62,62,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,62,62,62,-40,-87,-63,-64,-65,]),'RETURN':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,63,63,63,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,63,63,63,-40,-87,-63,-64,-65,]),'PENON':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,64,64,64,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,64,64,64,-40,-87,-63,-64,-65,]),'PENOFF':([21,24,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,239,244,245,247,248,249,],[-13,65,65,65,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,65,65,65,-40,-87,-63,-64,-65,]),'RBRACE':([21,24,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,76,77,107,145,146,177,195,196,213,217,218,220,221,222,223,224,225,228,230,238,239,240,241,243,244,245,247,248,249,251,252,],[-13,-118,75,-118,-9,-10,-12,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-15,-8,-11,-14,-116,-117,-39,-71,-72,-112,-62,-61,-60,-68,-69,-70,-66,-67,-118,-118,250,-53,-56,-57,253,-40,-87,-63,-64,-65,-54,-55,]),'ASSIGN':([28,51,178,],[69,78,211,]),'LBRACKET':([28,51,94,123,],[72,79,149,149,]),'COMMA':([28,71,94,95,96,97,98,105,106,108,109,110,111,113,123,128,129,132,147,150,158,165,166,169,170,173,175,176,200,201,202,203,204,205,206,207,208,209,210,213,226,227,229,],[73,73,-118,-80,-81,-82,-83,154,154,73,-118,-118,-118,-103,179,182,183,186,-79,-86,-90,-97,-98,-101,-108,-111,-104,-21,-91,-92,-93,-94,-95,-96,-99,-100,-109,-110,-102,-112,-85,-84,154,]),'CTE_INT':([63,69,72,78,79,80,82,83,84,85,86,88,89,90,91,114,115,116,117,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,-105,-106,-107,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'CTE_FLOAT':([63,69,72,78,79,80,82,83,84,85,86,88,89,90,91,114,115,116,117,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,-105,-106,-107,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'CTE_BOOL':([63,69,72,78,79,80,82,83,84,85,86,88,89,90,91,114,115,116,117,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,-105,-106,-107,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'TRUE':([63,80,148,179,],[101,101,101,101,]),'FALSE':([63,80,148,179,],[102,102,102,102,]),'MINUS':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,94,95,96,97,98,110,111,113,123,147,148,149,150,159,160,161,162,163,164,167,168,170,171,172,173,175,179,182,183,186,208,209,210,211,213,226,227,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,-118,-80,-81,-82,-83,167,-118,-103,-118,-79,115,115,-86,115,115,115,115,115,115,115,115,-108,115,115,-111,-104,115,115,115,115,-109,-110,-102,115,-112,-85,-84,]),'PLUS':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,94,95,96,97,98,110,111,113,123,147,148,149,150,159,160,161,162,163,164,167,168,170,171,172,173,175,179,182,183,186,208,209,210,211,213,226,227,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,-118,-80,-81,-82,-83,168,-118,-103,-118,-79,116,116,-86,116,116,116,116,116,116,116,116,-108,116,116,-111,-104,116,116,116,116,-109,-110,-102,116,-112,-85,-84,]),'ELSE':([75,214,],[-7,233,]),'EXPRESSION':([81,112,],[127,174,]),'RED':([87,],[134,]),'BLUE':([87,],[135,]),'YELLOW':([87,],[136,]),'GREEN':([87,],[137,]),'PINK':([87,],[138,]),'PURPLE':([87,],[139,]),'CTE_STRING':([91,],[144,]),'DIVIDE':([94,95,96,97,98,111,113,123,147,150,175,210,213,226,227,],[-118,-80,-81,-82,-83,171,-103,-118,-79,-86,-104,-102,-112,-85,-84,]),'TIMES':([94,95,96,97,98,111,113,123,147,150,175,210,213,226,227,],[-118,-80,-81,-82,-83,172,-103,-118,-79,-86,-104,-102,-112,-85,-84,]),'LESSER':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,159,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'GREATER':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,160,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'EQUAL':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,161,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'NOTEQUAL':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,162,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'GREATEROREQUAL':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,163,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'LESSEROREQUAL':([94,95,96,97,98,109,110,111,113,147,150,166,169,170,173,175,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,164,-118,-118,-103,-79,-86,-98,-101,-108,-111,-104,-99,-100,-109,-110,-102,-112,-85,-84,]),'RBRACKET':([94,95,96,97,98,109,110,111,113,119,122,147,150,158,165,166,169,170,173,175,194,200,201,202,203,204,205,206,207,208,209,210,213,226,227,],[-118,-80,-81,-82,-83,-118,-118,-118,-103,176,178,-79,-86,-90,-97,-98,-101,-108,-111,-104,227,-91,-92,-93,-94,-95,-96,-99,-100,-109,-110,-102,-112,-85,-84,]),'RPAREN':([94,95,96,97,98,99,100,101,102,103,104,105,106,110,111,113,123,124,125,126,127,130,131,133,134,135,136,137,138,139,140,141,142,143,144,147,150,153,155,156,166,169,170,173,174,175,193,206,207,208,209,210,212,213,215,216,219,226,227,229,242,],[-118,-80,-81,-82,-83,-47,-48,-77,-78,151,152,-118,-118,-118,-118,-103,-118,180,-114,-115,181,184,185,187,-41,-42,-43,-44,-45,-46,188,189,190,191,192,-79,-86,197,-52,199,-98,-101,-108,-111,210,-104,226,-99,-100,-109,-110,-102,-113,-112,235,236,237,-85,-84,-118,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program1':([4,],[5,]),'funcs':([4,7,250,253,],[6,18,255,255,]),'vars':([4,6,24,228,230,240,],[7,17,30,239,239,252,]),'empty':([4,24,28,30,32,69,71,72,78,79,80,82,83,84,85,86,88,89,90,91,94,105,106,108,109,110,111,123,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,214,228,229,230,250,253,],[8,33,74,33,33,117,74,117,117,117,117,117,117,117,117,117,117,117,117,117,150,155,155,74,165,169,173,150,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,234,241,155,241,256,256,]),'type':([4,7,11,25,26,68,154,250,253,],[9,9,22,66,67,22,198,9,9,]),'vars2':([11,68,],[21,107,]),'block':([16,181,233,],[23,214,246,]),'vars3':([22,73,],[27,120,]),'b1':([24,],[29,]),'b2':([24,30,32,],[31,76,77,]),'statute':([24,30,32,228,230,239,],[32,32,32,240,240,251,]),'assignment':([24,30,32,228,230,239,],[34,34,34,34,34,34,]),'call':([24,30,32,63,69,72,78,79,80,82,83,84,85,86,88,89,90,91,114,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,228,230,239,],[35,35,35,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,35,35,35,]),'condition':([24,30,32,228,230,239,],[36,36,36,36,36,36,]),'triangle':([24,30,32,228,230,239,],[37,37,37,37,37,37,]),'rectangle':([24,30,32,228,230,239,],[38,38,38,38,38,38,]),'square':([24,30,32,228,230,239,],[39,39,39,39,39,39,]),'circle':([24,30,32,228,230,239,],[40,40,40,40,40,40,]),'poligon':([24,30,32,228,230,239,],[41,41,41,41,41,41,]),'color':([24,30,32,228,230,239,],[42,42,42,42,42,42,]),'pensize':([24,30,32,228,230,239,],[43,43,43,43,43,43,]),'penforward':([24,30,32,228,230,239,],[44,44,44,44,44,44,]),'penback':([24,30,32,228,230,239,],[45,45,45,45,45,45,]),'rotate':([24,30,32,228,230,239,],[46,46,46,46,46,46,]),'return':([24,30,32,228,230,239,],[48,48,48,48,48,48,]),'penon':([24,30,32,228,230,239,],[49,49,49,49,49,49,]),'penoff':([24,30,32,228,230,239,],[50,50,50,50,50,50,]),'vars4':([28,71,108,],[70,118,157,]),'list':([28,],[71,]),'var_cte':([63,69,72,78,79,80,82,83,84,85,86,88,89,90,91,114,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[92,113,113,113,113,113,113,113,113,113,113,113,113,113,113,175,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'st_cte':([63,80,148,179,],[93,126,126,126,]),'cte_bool':([63,80,148,179,],[100,100,100,100,]),'expression':([69,72,78,211,],[108,119,121,231,]),'exp':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,148,149,159,160,161,162,163,164,167,168,179,182,183,186,211,],[109,109,109,122,125,128,129,130,131,132,140,141,142,143,193,194,200,201,202,203,204,205,206,207,125,215,216,219,109,]),'term':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,208,209,110,110,110,110,110,]),'factor':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'factor1':([69,72,78,79,80,82,83,84,85,86,88,89,90,91,148,149,159,160,161,162,163,164,167,168,171,172,179,182,183,186,211,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'call1':([80,148,179,],[124,124,212,]),'color_cte':([87,],[133,]),'var_cte1':([94,123,],[147,147,]),'funcs1':([105,106,229,],[153,156,242,]),'expression1':([109,],[158,]),'exp1':([110,],[166,]),'term1':([111,],[170,]),'condition1':([214,],[232,]),'funcs2':([228,230,],[238,243,]),'funcs3':([250,253,],[254,257,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON program1 DAVINCI block','program',6,'p_program','parser.py',8),
  ('program1 -> funcs','program1',1,'p_program1','parser.py',12),
  ('program1 -> vars','program1',1,'p_program1','parser.py',13),
  ('program1 -> funcs vars','program1',2,'p_program1','parser.py',14),
  ('program1 -> vars funcs','program1',2,'p_program1','parser.py',15),
  ('program1 -> empty','program1',1,'p_program1','parser.py',16),
  ('block -> LBRACE b1 RBRACE','block',3,'p_block','parser.py',19),
  ('b1 -> vars b2','b1',2,'p_b1','parser.py',22),
  ('b1 -> b2','b1',1,'p_b1','parser.py',23),
  ('b2 -> statute','b2',1,'p_b2','parser.py',26),
  ('b2 -> statute b2','b2',2,'p_b2','parser.py',27),
  ('b2 -> empty','b2',1,'p_b2','parser.py',28),
  ('vars -> VAR vars2','vars',2,'p_vars','parser.py',31),
  ('vars2 -> type vars3 SEMICOLON vars2','vars2',4,'p_vars2','parser.py',34),
  ('vars2 -> type vars3 SEMICOLON','vars2',3,'p_vars2','parser.py',35),
  ('vars3 -> ID ASSIGN expression vars4','vars3',4,'p_vars3','parser.py',38),
  ('vars3 -> ID list vars4','vars3',3,'p_vars3','parser.py',39),
  ('vars3 -> ID vars4','vars3',2,'p_vars3','parser.py',40),
  ('vars4 -> COMMA vars3','vars4',2,'p_vars4','parser.py',43),
  ('vars4 -> empty','vars4',1,'p_vars4','parser.py',44),
  ('list -> LBRACKET expression RBRACKET','list',3,'p_list','parser.py',47),
  ('statute -> assignment','statute',1,'p_statute','parser.py',50),
  ('statute -> call','statute',1,'p_statute','parser.py',51),
  ('statute -> condition','statute',1,'p_statute','parser.py',52),
  ('statute -> triangle','statute',1,'p_statute','parser.py',53),
  ('statute -> rectangle','statute',1,'p_statute','parser.py',54),
  ('statute -> square','statute',1,'p_statute','parser.py',55),
  ('statute -> circle','statute',1,'p_statute','parser.py',56),
  ('statute -> poligon','statute',1,'p_statute','parser.py',57),
  ('statute -> color','statute',1,'p_statute','parser.py',58),
  ('statute -> pensize','statute',1,'p_statute','parser.py',59),
  ('statute -> penforward','statute',1,'p_statute','parser.py',60),
  ('statute -> penback','statute',1,'p_statute','parser.py',61),
  ('statute -> rotate','statute',1,'p_statute','parser.py',62),
  ('statute -> WHILE','statute',1,'p_statute','parser.py',63),
  ('statute -> return','statute',1,'p_statute','parser.py',64),
  ('statute -> penon','statute',1,'p_statute','parser.py',65),
  ('statute -> penoff','statute',1,'p_statute','parser.py',66),
  ('assignment -> ID ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',69),
  ('assignment -> ID LBRACKET exp RBRACKET ASSIGN expression SEMICOLON','assignment',7,'p_assignment','parser.py',70),
  ('color_cte -> RED','color_cte',1,'p_color_cte','parser.py',73),
  ('color_cte -> BLUE','color_cte',1,'p_color_cte','parser.py',74),
  ('color_cte -> YELLOW','color_cte',1,'p_color_cte','parser.py',75),
  ('color_cte -> GREEN','color_cte',1,'p_color_cte','parser.py',76),
  ('color_cte -> PINK','color_cte',1,'p_color_cte','parser.py',77),
  ('color_cte -> PURPLE','color_cte',1,'p_color_cte','parser.py',78),
  ('st_cte -> STRING','st_cte',1,'p_st_cte','parser.py',81),
  ('st_cte -> cte_bool','st_cte',1,'p_st_cte','parser.py',82),
  ('funcs -> type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3','funcs',11,'p_funcs','parser.py',85),
  ('funcs -> VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3','funcs',11,'p_funcs','parser.py',86),
  ('funcs1 -> COMMA type ID funcs1','funcs1',4,'p_funcs1','parser.py',89),
  ('funcs1 -> empty','funcs1',1,'p_funcs1','parser.py',90),
  ('funcs2 -> vars','funcs2',1,'p_funcs2','parser.py',93),
  ('funcs2 -> vars statute','funcs2',2,'p_funcs2','parser.py',94),
  ('funcs2 -> statute vars','funcs2',2,'p_funcs2','parser.py',95),
  ('funcs2 -> statute','funcs2',1,'p_funcs2','parser.py',96),
  ('funcs2 -> empty','funcs2',1,'p_funcs2','parser.py',97),
  ('funcs3 -> funcs','funcs3',1,'p_funcs3','parser.py',100),
  ('funcs3 -> empty','funcs3',1,'p_funcs3','parser.py',101),
  ('color -> COLOR LPAREN color_cte RPAREN SEMICOLON','color',5,'p_color','parser.py',104),
  ('circle -> CIRCLE LPAREN exp RPAREN SEMICOLON','circle',5,'p_circle','parser.py',107),
  ('square -> SQUARE LPAREN exp RPAREN SEMICOLON','square',5,'p_square','parser.py',110),
  ('triangle -> TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON','triangle',7,'p_triangle','parser.py',113),
  ('rectangle -> RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON','rectangle',7,'p_rectangle','parser.py',116),
  ('poligon -> POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON','poligon',7,'p_poligon','parser.py',119),
  ('rotate -> ROTATE LPAREN exp RPAREN SEMICOLON','rotate',5,'p_rotate','parser.py',122),
  ('rotate -> ROTATE LPAREN CTE_STRING RPAREN SEMICOLON','rotate',5,'p_rotate','parser.py',123),
  ('pensize -> PENSIZE LPAREN exp RPAREN SEMICOLON','pensize',5,'p_pensize','parser.py',126),
  ('penforward -> PENFORWARD LPAREN exp RPAREN SEMICOLON','penforward',5,'p_penforward','parser.py',129),
  ('penback -> PENBACK LPAREN exp RPAREN SEMICOLON','penback',5,'p_penback','parser.py',132),
  ('penon -> PENON LPAREN RPAREN SEMICOLON','penon',4,'p_penon','parser.py',135),
  ('penoff -> PENOFF LPAREN RPAREN SEMICOLON','penoff',4,'p_penoff','parser.py',138),
  ('type -> INT','type',1,'p_type','parser.py',141),
  ('type -> FLOAT','type',1,'p_type','parser.py',142),
  ('type -> STRING','type',1,'p_type','parser.py',143),
  ('type -> BOOL','type',1,'p_type','parser.py',144),
  ('cte_bool -> TRUE','cte_bool',1,'p_cte_bool','parser.py',147),
  ('cte_bool -> FALSE','cte_bool',1,'p_cte_bool','parser.py',148),
  ('var_cte -> ID var_cte1','var_cte',2,'p_var_cte','parser.py',151),
  ('var_cte -> CTE_INT','var_cte',1,'p_var_cte','parser.py',152),
  ('var_cte -> CTE_FLOAT','var_cte',1,'p_var_cte','parser.py',153),
  ('var_cte -> CTE_BOOL','var_cte',1,'p_var_cte','parser.py',154),
  ('var_cte -> call','var_cte',1,'p_var_cte','parser.py',155),
  ('var_cte1 -> LBRACKET exp RBRACKET','var_cte1',3,'p_var_cte1','parser.py',158),
  ('var_cte1 -> LPAREN exp RPAREN','var_cte1',3,'p_var_cte1','parser.py',159),
  ('var_cte1 -> empty','var_cte1',1,'p_var_cte1','parser.py',160),
  ('condition -> IF LPAREN EXPRESSION RPAREN block condition1 SEMICOLON','condition',7,'p_condition','parser.py',163),
  ('condition1 -> ELSE block','condition1',2,'p_condition1','parser.py',166),
  ('condition1 -> empty','condition1',1,'p_condition1','parser.py',167),
  ('expression -> exp expression1','expression',2,'p_expression','parser.py',170),
  ('expression1 -> LESSER exp','expression1',2,'p_expression1','parser.py',173),
  ('expression1 -> GREATER exp','expression1',2,'p_expression1','parser.py',174),
  ('expression1 -> EQUAL exp','expression1',2,'p_expression1','parser.py',175),
  ('expression1 -> NOTEQUAL exp','expression1',2,'p_expression1','parser.py',176),
  ('expression1 -> GREATEROREQUAL exp','expression1',2,'p_expression1','parser.py',177),
  ('expression1 -> LESSEROREQUAL exp','expression1',2,'p_expression1','parser.py',178),
  ('expression1 -> empty','expression1',1,'p_expression1','parser.py',179),
  ('exp -> term exp1','exp',2,'p_exp','parser.py',182),
  ('exp1 -> MINUS exp','exp1',2,'p_exp1','parser.py',185),
  ('exp1 -> PLUS exp','exp1',2,'p_exp1','parser.py',186),
  ('exp1 -> empty','exp1',1,'p_exp1','parser.py',187),
  ('factor -> LPAREN EXPRESSION RPAREN','factor',3,'p_factor','parser.py',190),
  ('factor -> var_cte','factor',1,'p_factor','parser.py',191),
  ('factor -> factor1 var_cte','factor',2,'p_factor','parser.py',192),
  ('factor1 -> MINUS','factor1',1,'p_factor1','parser.py',195),
  ('factor1 -> PLUS','factor1',1,'p_factor1','parser.py',196),
  ('factor1 -> empty','factor1',1,'p_factor1','parser.py',197),
  ('term -> factor term1','term',2,'p_term','parser.py',200),
  ('term1 -> DIVIDE term','term1',2,'p_term1','parser.py',203),
  ('term1 -> TIMES term','term1',2,'p_term1','parser.py',204),
  ('term1 -> empty','term1',1,'p_term1','parser.py',205),
  ('call -> ID LPAREN call1 RPAREN SEMICOLON','call',5,'p_call','parser.py',208),
  ('call1 -> ID COMMA call1','call1',3,'p_call1','parser.py',211),
  ('call1 -> exp','call1',1,'p_call1','parser.py',212),
  ('call1 -> st_cte','call1',1,'p_call1','parser.py',213),
  ('return -> RETURN var_cte SEMICOLON','return',3,'p_return','parser.py',216),
  ('return -> RETURN st_cte SEMICOLON','return',3,'p_return','parser.py',217),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',220),
]
