
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BLOCK BLUE BOOL CALL CIRCLE COLOR COLOR_CTE COMMA CONDITION CTE_BOOL CTE_FLOAT CTE_INT CTE_STRING DAVINCI DIVIDE ELSE EQUAL EXP EXPRESSION FACTOR FALSE FLOAT GREATER GREATEROREQUAL GREEN ID IF INT LBRACE LBRACKET LESSER LESSEROREQUAL LPAREN MINUS NOT NOTEQUAL OR PENBACK PENFORWARD PENOFF PENON PENSIZE PINK PLUS POLIGON PROGRAM PURPLE RBRACE RBRACKET RECTANGLE RED RETURN ROTATE RPAREN SEMICOLON SIZE SQUARE STATUTE STRING ST_CTE TERM TIMES TRIANGLE TRUE TYPE VAR VAR VAR_CTE VOID WHILE YELLOWprogram : PROGRAM ID SEMICOLON program1 DAVINCI blockprogram1 : funcs\n\t| vars\n\t| funcs vars\n\t| vars funcs\n\t| emptyblock : LBRACE b1 RBRACEb1 : vars b2 \n\t| b2b2 : statute\n\t| statute b2\n\t| emptyvars : VAR vars2vars2 : type ID vars3 SEMICOLON vars2\n\t| type ID vars3 SEMICOLON\n\t| type assignment\n\t| type assignment vars2vars3 : COMMA ID vars3 \n\t| list vars3\n\t| list COMMA ID vars3 \n\t| emptylist : LBRACKET exp RBRACKETstatute : assignment\n\t | call\n\t | condition\n\t | triangle\n\t | rectangle\n\t | square\n\t | circle\n\t | poligon\n\t | color\n\t | pensize\n\t | penforward\n\t | penback\n\t | rotate\n\t | WHILE\n\t | return\n\t | penon\n\t | penoffassignment : ID ASSIGN expression SEMICOLON\n\t | ID LBRACKET exp RBRACKET ASSIGN expression SEMICOLONcolor_cte : RED\n\t\t| BLUE\n\t\t| YELLOW\n\t\t| GREEN\n\t\t| PINK\n\t\t| PURPLEst_cte : STRING SEMICOLON\n\t\t| CTE_BOOL SEMICOLONfuncs : type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3\n\t| VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3 funcs1 : COMMA type ID funcs1\n\t| emptyfuncs2 : vars\n\t| vars statute\n\t| statute vars\n\t| statute\n\t| empty funcs3 : funcs\n\t| emptycolor : COLOR LPAREN color_cte RPAREN SEMICOLONcircle : CIRCLE LPAREN exp RPAREN SEMICOLONsquare : SQUARE LPAREN exp RPAREN SEMICOLONtriangle : TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLONrectangle : RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLONpoligon : POLIGON LPAREN exp COMMA exp RPAREN SEMICOLONrotate : ROTATE LPAREN exp RPAREN SEMICOLON\n\t| ROTATE LPAREN CTE_STRING RPAREN SEMICOLONpensize : PENSIZE LPAREN exp RPAREN SEMICOLONpenforward : PENFORWARD LPAREN exp RPAREN SEMICOLONpenback : PENBACK LPAREN exp RPAREN SEMICOLONpenon : PENON LPAREN RPAREN SEMICOLONpenoff : PENOFF LPAREN RPAREN SEMICOLONtype : INT\n\t\t| FLOAT\n\t\t| STRING\n\t\t| BOOLcte_bool : TRUE\n\t\t\t\t| FALSEvar_cte : ID var_cte1\n\t\t\t\t| CTE_INT\n\t\t\t\t| CTE_FLOAT\n\t\t\t\t| callvar_cte1 : LBRACKET exp RBRACKET\n\t\t\t\t | LPAREN exp RPAREN\n\t\t\t\t | emptycondition : IF LPAREN EXPRESSION RPAREN block condition1 SEMICOLONcondition1 : ELSE block\n\t| emptyexpression : exp expression1 IDexpression1 : expression2 expression2 : LESSER \n\t| GREATER \n\t| EQUAL \n\t| NOTEQUAL\n\t| GREATEROREQUAL\n    | LESSEROREQUALexp : term exp1exp1 : MINUS term exp1\n\t| PLUS term exp1\n\t| emptyfactor : LPAREN EXPRESSION RPAREN\n\t| var_cte\n\t| factor1 var_ctefactor1 : MINUS \n\t| PLUSterm : DIVIDE \n\t| TIMES \n\t| factorcall : ID LPAREN call1 RPAREN SEMICOLONcall1 : ID COMMA call1\n\t| exp\n\t| ST_CTEreturn : RETURN var_cte SEMICOLON\n\t\t\t| RETURN st_cte SEMICOLONempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,23,75,],[0,-1,-7,]),'ID':([2,9,10,12,13,14,15,21,22,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,63,66,67,69,70,71,74,78,79,81,82,83,84,85,87,88,89,90,103,112,113,114,118,119,143,144,146,147,157,158,159,160,161,162,163,164,165,166,168,169,178,181,182,185,194,195,197,203,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[3,19,20,-74,-75,-76,-77,-13,27,51,-16,51,51,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,93,101,102,93,93,116,-17,93,121,93,93,93,93,93,93,93,93,93,-15,93,-105,-106,175,93,-114,-115,121,93,-14,-40,199,-91,-92,-93,-94,-95,-96,-97,93,93,121,93,93,93,-72,-73,223,93,-110,-63,-62,-61,-69,-70,-71,-67,-68,51,51,51,-41,-87,-64,-65,-66,]),'SEMICOLON':([3,27,68,72,73,75,91,92,93,94,95,96,97,98,104,116,117,145,148,149,150,151,152,173,174,175,179,183,184,186,187,188,189,190,191,199,204,205,207,208,220,221,227,228,230,231,232,233,242,],[4,-116,103,-116,-21,-7,143,144,-116,-81,-82,-83,149,150,158,-116,-19,-80,-86,-48,-49,194,195,-22,-18,-116,207,211,212,214,215,216,217,218,219,-90,-18,-22,-110,-116,-85,-84,240,241,-89,243,244,245,-88,]),'VOID':([4,7,21,28,74,103,157,158,240,246,249,],[10,10,-13,-16,-17,-15,-14,-40,-41,10,10,]),'VAR':([4,6,24,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,143,144,158,194,195,207,211,212,214,215,216,217,218,219,222,224,236,240,241,243,244,245,246,249,250,251,252,253,],[11,11,11,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-114,-115,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,11,11,11,-41,-87,-64,-65,-66,-116,-116,-50,-59,-60,-51,]),'DAVINCI':([4,5,6,7,8,17,18,21,28,74,103,157,158,240,246,249,250,251,252,253,],[-116,16,-2,-3,-6,-4,-5,-13,-16,-17,-15,-14,-40,-41,-116,-116,-50,-59,-60,-51,]),'INT':([4,7,11,21,25,26,28,74,103,154,157,158,240,246,249,],[12,12,12,-13,12,12,12,-17,12,12,-14,-40,-41,12,12,]),'FLOAT':([4,7,11,21,25,26,28,74,103,154,157,158,240,246,249,],[13,13,13,-13,13,13,13,-17,13,13,-14,-40,-41,13,13,]),'STRING':([4,7,11,21,25,26,28,63,74,103,154,157,158,240,246,249,],[14,14,14,-13,14,14,14,97,-17,14,14,-14,-40,-41,14,14,]),'BOOL':([4,7,11,21,25,26,28,74,103,154,157,158,240,246,249,],[15,15,15,-13,15,15,15,-17,15,15,-14,-40,-41,15,15,]),'LBRACE':([16,180,196,198,229,],[24,24,222,224,24,]),'LPAREN':([19,20,51,52,53,54,55,56,57,58,59,60,61,62,64,65,69,70,78,79,81,82,83,84,85,87,88,89,90,93,119,121,146,147,168,169,178,181,182,185,203,],[25,26,79,80,81,82,83,84,85,86,87,88,89,90,99,100,110,110,110,110,110,110,110,110,110,110,110,110,110,146,110,146,110,110,110,110,110,110,110,110,110,]),'WHILE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,47,-16,47,47,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,47,47,47,-41,-87,-64,-65,-66,]),'IF':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,52,-16,52,52,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,52,52,52,-41,-87,-64,-65,-66,]),'TRIANGLE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,53,-16,53,53,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,53,53,53,-41,-87,-64,-65,-66,]),'RECTANGLE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,54,-16,54,54,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,54,54,54,-41,-87,-64,-65,-66,]),'SQUARE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,55,-16,55,55,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,55,55,55,-41,-87,-64,-65,-66,]),'CIRCLE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,56,-16,56,56,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,56,56,56,-41,-87,-64,-65,-66,]),'POLIGON':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,57,-16,57,57,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,57,57,57,-41,-87,-64,-65,-66,]),'COLOR':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,58,-16,58,58,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,58,58,58,-41,-87,-64,-65,-66,]),'PENSIZE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,59,-16,59,59,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,59,59,59,-41,-87,-64,-65,-66,]),'PENFORWARD':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,60,-16,60,60,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,60,60,60,-41,-87,-64,-65,-66,]),'PENBACK':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,61,-16,61,61,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,61,61,61,-41,-87,-64,-65,-66,]),'ROTATE':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,62,-16,62,62,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,62,62,62,-41,-87,-64,-65,-66,]),'RETURN':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,63,-16,63,63,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,63,63,63,-41,-87,-64,-65,-66,]),'PENON':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,64,-16,64,64,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,64,64,64,-41,-87,-64,-65,-66,]),'PENOFF':([21,24,28,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,235,240,241,243,244,245,],[-13,65,-16,65,65,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,65,65,65,-41,-87,-64,-65,-66,]),'RBRACE':([21,24,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,74,76,77,103,143,144,157,158,194,195,207,211,212,214,215,216,217,218,219,222,224,234,235,236,237,239,240,241,243,244,245,247,248,],[-13,-116,-16,75,-116,-9,-10,-12,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-17,-8,-11,-15,-114,-115,-14,-40,-72,-73,-110,-63,-62,-61,-69,-70,-71,-67,-68,-116,-116,246,-54,-57,-58,249,-41,-87,-64,-65,-66,-55,-56,]),'ASSIGN':([27,51,173,177,],[69,69,203,203,]),'LBRACKET':([27,51,72,93,116,121,173,175,205,],[70,78,119,147,119,147,-22,119,-22,]),'COMMA':([27,72,93,94,95,96,101,102,106,107,108,109,111,116,121,126,127,130,145,148,167,170,172,173,175,200,201,202,205,207,220,221,223,225,226,],[71,118,-116,-81,-82,-83,154,154,-116,-107,-108,-109,-103,71,178,181,182,185,-80,-86,-98,-101,-104,-22,71,-116,-116,-102,-22,-110,-85,-84,154,-99,-100,]),'CTE_INT':([63,69,70,78,79,81,82,83,84,85,87,88,89,90,112,113,114,119,146,147,168,169,178,181,182,185,203,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,-105,-106,94,94,94,94,94,94,94,94,94,94,]),'CTE_FLOAT':([63,69,70,78,79,81,82,83,84,85,87,88,89,90,112,113,114,119,146,147,168,169,178,181,182,185,203,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,-105,-106,95,95,95,95,95,95,95,95,95,95,]),'CTE_BOOL':([63,],[98,]),'DIVIDE':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,168,169,178,181,182,185,203,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'TIMES':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,168,169,178,181,182,185,203,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'MINUS':([69,70,78,79,81,82,83,84,85,87,88,89,90,93,94,95,96,106,107,108,109,111,119,121,145,146,147,148,168,169,172,178,181,182,185,200,201,202,203,207,220,221,],[113,113,113,113,113,113,113,113,113,113,113,113,113,-116,-81,-82,-83,168,-107,-108,-109,-103,113,-116,-80,113,113,-86,113,113,-104,113,113,113,113,168,168,-102,113,-110,-85,-84,]),'PLUS':([69,70,78,79,81,82,83,84,85,87,88,89,90,93,94,95,96,106,107,108,109,111,119,121,145,146,147,148,168,169,172,178,181,182,185,200,201,202,203,207,220,221,],[114,114,114,114,114,114,114,114,114,114,114,114,114,-116,-81,-82,-83,169,-107,-108,-109,-103,114,-116,-80,114,114,-86,114,114,-104,114,114,114,114,169,169,-102,114,-110,-85,-84,]),'ELSE':([75,208,],[-7,229,]),'ST_CTE':([79,146,178,],[124,124,124,]),'EXPRESSION':([80,110,],[125,171,]),'RED':([86,],[132,]),'BLUE':([86,],[133,]),'YELLOW':([86,],[134,]),'GREEN':([86,],[135,]),'PINK':([86,],[136,]),'PURPLE':([86,],[137,]),'CTE_STRING':([90,],[142,]),'LESSER':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,161,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'GREATER':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,162,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'EQUAL':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,163,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'NOTEQUAL':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,164,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'GREATEROREQUAL':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,165,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'LESSEROREQUAL':([93,94,95,96,105,106,107,108,109,111,145,148,167,170,172,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,166,-116,-107,-108,-109,-103,-80,-86,-98,-101,-104,-116,-116,-102,-110,-85,-84,-99,-100,]),'RBRACKET':([93,94,95,96,106,107,108,109,111,115,120,145,148,167,170,172,176,193,200,201,202,207,220,221,225,226,],[-116,-81,-82,-83,-116,-107,-108,-109,-103,173,177,-80,-86,-98,-101,-104,205,221,-116,-116,-102,-110,-85,-84,-99,-100,]),'RPAREN':([93,94,95,96,99,100,101,102,106,107,108,109,111,121,122,123,124,125,128,129,131,132,133,134,135,136,137,138,139,140,141,142,145,148,153,155,156,167,170,171,172,192,200,201,202,206,207,209,210,213,220,221,223,225,226,238,],[-116,-81,-82,-83,151,152,-116,-116,-116,-107,-108,-109,-103,-116,179,-112,-113,180,183,184,186,-42,-43,-44,-45,-46,-47,187,188,189,190,191,-80,-86,196,-53,198,-98,-101,202,-104,220,-116,-116,-102,-111,-110,231,232,233,-85,-84,-116,-99,-100,-52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program1':([4,],[5,]),'funcs':([4,7,246,249,],[6,18,251,251,]),'vars':([4,6,24,222,224,236,],[7,17,30,235,235,248,]),'empty':([4,24,27,30,32,72,93,101,102,106,116,121,175,200,201,208,222,223,224,246,249,],[8,33,73,33,33,73,148,155,155,170,73,148,73,170,170,230,237,155,237,252,252,]),'type':([4,7,11,25,26,28,103,154,246,249,],[9,9,22,66,67,22,22,197,9,9,]),'vars2':([11,28,103,],[21,74,157,]),'block':([16,180,229,],[23,208,242,]),'assignment':([22,24,30,32,222,224,235,],[28,34,34,34,34,34,34,]),'b1':([24,],[29,]),'b2':([24,30,32,],[31,76,77,]),'statute':([24,30,32,222,224,235,],[32,32,32,236,236,247,]),'call':([24,30,32,63,69,70,78,79,81,82,83,84,85,87,88,89,90,112,119,146,147,168,169,178,181,182,185,203,222,224,235,],[35,35,35,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,35,35,35,]),'condition':([24,30,32,222,224,235,],[36,36,36,36,36,36,]),'triangle':([24,30,32,222,224,235,],[37,37,37,37,37,37,]),'rectangle':([24,30,32,222,224,235,],[38,38,38,38,38,38,]),'square':([24,30,32,222,224,235,],[39,39,39,39,39,39,]),'circle':([24,30,32,222,224,235,],[40,40,40,40,40,40,]),'poligon':([24,30,32,222,224,235,],[41,41,41,41,41,41,]),'color':([24,30,32,222,224,235,],[42,42,42,42,42,42,]),'pensize':([24,30,32,222,224,235,],[43,43,43,43,43,43,]),'penforward':([24,30,32,222,224,235,],[44,44,44,44,44,44,]),'penback':([24,30,32,222,224,235,],[45,45,45,45,45,45,]),'rotate':([24,30,32,222,224,235,],[46,46,46,46,46,46,]),'return':([24,30,32,222,224,235,],[48,48,48,48,48,48,]),'penon':([24,30,32,222,224,235,],[49,49,49,49,49,49,]),'penoff':([24,30,32,222,224,235,],[50,50,50,50,50,50,]),'vars3':([27,72,116,175,],[68,117,174,204,]),'list':([27,72,116,175,],[72,72,72,72,]),'var_cte':([63,69,70,78,79,81,82,83,84,85,87,88,89,90,112,119,146,147,168,169,178,181,182,185,203,],[91,111,111,111,111,111,111,111,111,111,111,111,111,111,172,111,111,111,111,111,111,111,111,111,111,]),'st_cte':([63,],[92,]),'expression':([69,203,],[104,227,]),'exp':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,178,181,182,185,203,],[105,115,120,123,126,127,128,129,130,138,139,140,141,176,192,193,123,209,210,213,105,]),'term':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,168,169,178,181,182,185,203,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,200,201,106,106,106,106,106,]),'factor':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,168,169,178,181,182,185,203,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'factor1':([69,70,78,79,81,82,83,84,85,87,88,89,90,119,146,147,168,169,178,181,182,185,203,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'call1':([79,146,178,],[122,122,206,]),'color_cte':([86,],[131,]),'var_cte1':([93,121,],[145,145,]),'funcs1':([101,102,223,],[153,156,238,]),'expression1':([105,],[159,]),'expression2':([105,],[160,]),'exp1':([106,200,201,],[167,225,226,]),'condition1':([208,],[228,]),'funcs2':([222,224,],[234,239,]),'funcs3':([246,249,],[250,253,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON program1 DAVINCI block','program',6,'p_program','parser.py',8),
  ('program1 -> funcs','program1',1,'p_program1','parser.py',11),
  ('program1 -> vars','program1',1,'p_program1','parser.py',12),
  ('program1 -> funcs vars','program1',2,'p_program1','parser.py',13),
  ('program1 -> vars funcs','program1',2,'p_program1','parser.py',14),
  ('program1 -> empty','program1',1,'p_program1','parser.py',15),
  ('block -> LBRACE b1 RBRACE','block',3,'p_block','parser.py',18),
  ('b1 -> vars b2','b1',2,'p_b1','parser.py',21),
  ('b1 -> b2','b1',1,'p_b1','parser.py',22),
  ('b2 -> statute','b2',1,'p_b2','parser.py',25),
  ('b2 -> statute b2','b2',2,'p_b2','parser.py',26),
  ('b2 -> empty','b2',1,'p_b2','parser.py',27),
  ('vars -> VAR vars2','vars',2,'p_vars','parser.py',30),
  ('vars2 -> type ID vars3 SEMICOLON vars2','vars2',5,'p_vars2','parser.py',33),
  ('vars2 -> type ID vars3 SEMICOLON','vars2',4,'p_vars2','parser.py',34),
  ('vars2 -> type assignment','vars2',2,'p_vars2','parser.py',35),
  ('vars2 -> type assignment vars2','vars2',3,'p_vars2','parser.py',36),
  ('vars3 -> COMMA ID vars3','vars3',3,'p_vars3','parser.py',39),
  ('vars3 -> list vars3','vars3',2,'p_vars3','parser.py',40),
  ('vars3 -> list COMMA ID vars3','vars3',4,'p_vars3','parser.py',41),
  ('vars3 -> empty','vars3',1,'p_vars3','parser.py',42),
  ('list -> LBRACKET exp RBRACKET','list',3,'p_list','parser.py',45),
  ('statute -> assignment','statute',1,'p_statute','parser.py',48),
  ('statute -> call','statute',1,'p_statute','parser.py',49),
  ('statute -> condition','statute',1,'p_statute','parser.py',50),
  ('statute -> triangle','statute',1,'p_statute','parser.py',51),
  ('statute -> rectangle','statute',1,'p_statute','parser.py',52),
  ('statute -> square','statute',1,'p_statute','parser.py',53),
  ('statute -> circle','statute',1,'p_statute','parser.py',54),
  ('statute -> poligon','statute',1,'p_statute','parser.py',55),
  ('statute -> color','statute',1,'p_statute','parser.py',56),
  ('statute -> pensize','statute',1,'p_statute','parser.py',57),
  ('statute -> penforward','statute',1,'p_statute','parser.py',58),
  ('statute -> penback','statute',1,'p_statute','parser.py',59),
  ('statute -> rotate','statute',1,'p_statute','parser.py',60),
  ('statute -> WHILE','statute',1,'p_statute','parser.py',61),
  ('statute -> return','statute',1,'p_statute','parser.py',62),
  ('statute -> penon','statute',1,'p_statute','parser.py',63),
  ('statute -> penoff','statute',1,'p_statute','parser.py',64),
  ('assignment -> ID ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',67),
  ('assignment -> ID LBRACKET exp RBRACKET ASSIGN expression SEMICOLON','assignment',7,'p_assignment','parser.py',68),
  ('color_cte -> RED','color_cte',1,'p_color_cte','parser.py',71),
  ('color_cte -> BLUE','color_cte',1,'p_color_cte','parser.py',72),
  ('color_cte -> YELLOW','color_cte',1,'p_color_cte','parser.py',73),
  ('color_cte -> GREEN','color_cte',1,'p_color_cte','parser.py',74),
  ('color_cte -> PINK','color_cte',1,'p_color_cte','parser.py',75),
  ('color_cte -> PURPLE','color_cte',1,'p_color_cte','parser.py',76),
  ('st_cte -> STRING SEMICOLON','st_cte',2,'p_st_cte','parser.py',79),
  ('st_cte -> CTE_BOOL SEMICOLON','st_cte',2,'p_st_cte','parser.py',80),
  ('funcs -> type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3','funcs',11,'p_funcs','parser.py',83),
  ('funcs -> VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3','funcs',11,'p_funcs','parser.py',84),
  ('funcs1 -> COMMA type ID funcs1','funcs1',4,'p_funcs1','parser.py',87),
  ('funcs1 -> empty','funcs1',1,'p_funcs1','parser.py',88),
  ('funcs2 -> vars','funcs2',1,'p_funcs2','parser.py',91),
  ('funcs2 -> vars statute','funcs2',2,'p_funcs2','parser.py',92),
  ('funcs2 -> statute vars','funcs2',2,'p_funcs2','parser.py',93),
  ('funcs2 -> statute','funcs2',1,'p_funcs2','parser.py',94),
  ('funcs2 -> empty','funcs2',1,'p_funcs2','parser.py',95),
  ('funcs3 -> funcs','funcs3',1,'p_funcs3','parser.py',98),
  ('funcs3 -> empty','funcs3',1,'p_funcs3','parser.py',99),
  ('color -> COLOR LPAREN color_cte RPAREN SEMICOLON','color',5,'p_color','parser.py',102),
  ('circle -> CIRCLE LPAREN exp RPAREN SEMICOLON','circle',5,'p_circle','parser.py',105),
  ('square -> SQUARE LPAREN exp RPAREN SEMICOLON','square',5,'p_square','parser.py',108),
  ('triangle -> TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON','triangle',7,'p_triangle','parser.py',111),
  ('rectangle -> RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON','rectangle',7,'p_rectangle','parser.py',114),
  ('poligon -> POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON','poligon',7,'p_poligon','parser.py',117),
  ('rotate -> ROTATE LPAREN exp RPAREN SEMICOLON','rotate',5,'p_rotate','parser.py',120),
  ('rotate -> ROTATE LPAREN CTE_STRING RPAREN SEMICOLON','rotate',5,'p_rotate','parser.py',121),
  ('pensize -> PENSIZE LPAREN exp RPAREN SEMICOLON','pensize',5,'p_pensize','parser.py',124),
  ('penforward -> PENFORWARD LPAREN exp RPAREN SEMICOLON','penforward',5,'p_penforward','parser.py',127),
  ('penback -> PENBACK LPAREN exp RPAREN SEMICOLON','penback',5,'p_penback','parser.py',130),
  ('penon -> PENON LPAREN RPAREN SEMICOLON','penon',4,'p_penon','parser.py',133),
  ('penoff -> PENOFF LPAREN RPAREN SEMICOLON','penoff',4,'p_penoff','parser.py',136),
  ('type -> INT','type',1,'p_type','parser.py',139),
  ('type -> FLOAT','type',1,'p_type','parser.py',140),
  ('type -> STRING','type',1,'p_type','parser.py',141),
  ('type -> BOOL','type',1,'p_type','parser.py',142),
  ('cte_bool -> TRUE','cte_bool',1,'p_cte_bool','parser.py',145),
  ('cte_bool -> FALSE','cte_bool',1,'p_cte_bool','parser.py',146),
  ('var_cte -> ID var_cte1','var_cte',2,'p_var_cte','parser.py',149),
  ('var_cte -> CTE_INT','var_cte',1,'p_var_cte','parser.py',150),
  ('var_cte -> CTE_FLOAT','var_cte',1,'p_var_cte','parser.py',151),
  ('var_cte -> call','var_cte',1,'p_var_cte','parser.py',152),
  ('var_cte1 -> LBRACKET exp RBRACKET','var_cte1',3,'p_var_cte1','parser.py',155),
  ('var_cte1 -> LPAREN exp RPAREN','var_cte1',3,'p_var_cte1','parser.py',156),
  ('var_cte1 -> empty','var_cte1',1,'p_var_cte1','parser.py',157),
  ('condition -> IF LPAREN EXPRESSION RPAREN block condition1 SEMICOLON','condition',7,'p_condition','parser.py',160),
  ('condition1 -> ELSE block','condition1',2,'p_condition1','parser.py',163),
  ('condition1 -> empty','condition1',1,'p_condition1','parser.py',164),
  ('expression -> exp expression1 ID','expression',3,'p_expression','parser.py',167),
  ('expression1 -> expression2','expression1',1,'p_expression1','parser.py',170),
  ('expression2 -> LESSER','expression2',1,'p_expression2','parser.py',173),
  ('expression2 -> GREATER','expression2',1,'p_expression2','parser.py',174),
  ('expression2 -> EQUAL','expression2',1,'p_expression2','parser.py',175),
  ('expression2 -> NOTEQUAL','expression2',1,'p_expression2','parser.py',176),
  ('expression2 -> GREATEROREQUAL','expression2',1,'p_expression2','parser.py',177),
  ('expression2 -> LESSEROREQUAL','expression2',1,'p_expression2','parser.py',178),
  ('exp -> term exp1','exp',2,'p_exp','parser.py',181),
  ('exp1 -> MINUS term exp1','exp1',3,'p_exp1','parser.py',184),
  ('exp1 -> PLUS term exp1','exp1',3,'p_exp1','parser.py',185),
  ('exp1 -> empty','exp1',1,'p_exp1','parser.py',186),
  ('factor -> LPAREN EXPRESSION RPAREN','factor',3,'p_factor','parser.py',189),
  ('factor -> var_cte','factor',1,'p_factor','parser.py',190),
  ('factor -> factor1 var_cte','factor',2,'p_factor','parser.py',191),
  ('factor1 -> MINUS','factor1',1,'p_factor1','parser.py',194),
  ('factor1 -> PLUS','factor1',1,'p_factor1','parser.py',195),
  ('term -> DIVIDE','term',1,'p_term','parser.py',198),
  ('term -> TIMES','term',1,'p_term','parser.py',199),
  ('term -> factor','term',1,'p_term','parser.py',200),
  ('call -> ID LPAREN call1 RPAREN SEMICOLON','call',5,'p_call','parser.py',203),
  ('call1 -> ID COMMA call1','call1',3,'p_call1','parser.py',206),
  ('call1 -> exp','call1',1,'p_call1','parser.py',207),
  ('call1 -> ST_CTE','call1',1,'p_call1','parser.py',208),
  ('return -> RETURN var_cte SEMICOLON','return',3,'p_return','parser.py',211),
  ('return -> RETURN st_cte SEMICOLON','return',3,'p_return','parser.py',212),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',215),
]