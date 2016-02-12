function answer_16()
n = 300;
score = [];
for alpha=5:50
    for beta=1:50
        p = (alpha * log(n))/n;
        q = (beta * log(n))/n;
        meanOverlap = 0;
        if p>=q
           for i=1:20
               I = eye(n);
               ix = randperm (n);
               T = I(ix,:);
               overlp = answer_15(p,q,n,T);
               meanOverlap = meanOverlap + overlp;
           end
           score(alpha,beta) =  meanOverlap/20;
        end 
    end
end
imagesc(score);
colorbar;
colormap(gray);
hold on;
for b=1:50
    p = [1 -(0.3506 +(2*b)) -(0.3506*b)+(b*b)];
    r = roots(p);
    X(b) = r(1);
end
plot(1:b,X,'r','LineWidth',3)