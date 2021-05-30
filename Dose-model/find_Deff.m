syms u v x y x0 y0 a b
eqns = [u == x/(1+a*((v/y0)/(1+v/y0))), v == y/(1+b*((u/x0)/(1+u/x0)))];
S = solve(eqns, [u,v])