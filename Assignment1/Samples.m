ber = 1 - 2*binornd(1,.5,10,10);
goe = 2*randn(10);
S=eig(ber);
T=eig(goe);
disp(S);
disp(S/sqrt(10));
disp(T);
